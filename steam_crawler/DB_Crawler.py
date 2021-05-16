import sys
from csv import reader
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlRelationalTableModel, QSqlRelationalDelegate, QSqlDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QHeaderView, QVBoxLayout, QMessageBox
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///steamcrawler.db", echo=True)
Base = declarative_base()

steam_data = Table("steamcrawler.db", Base.metadata,
                   Column("game_id", Integer, ForeignKey("steam_data.id")),
                   Column("game_name", String, ForeignKey("steam_data.game_name")),
                   Column("game_date", String, ForeignKey("steam_data.game_date")),
                   Column("game_img", String, ForeignKey("steam_data.game_img")),
                   Column("game_url", String, ForeignKey("steam_data.game_url")),
                   Column("game_rating", String, ForeignKey("steam_data.game_rating")),
                   Column("game_price", Integer, ForeignKey("steam_data.game_price"))
                   )


class Game(Base):
    __tablename__ = "steam_data"
    id = Column(Integer, primary_key=True)
    game_name = Column(String(120), index=True)
    game_date = Column(String(20))
    game_img = Column(String(250))
    game_url = Column(String(250))
    game_rating = Column(String(150))
    game_price = Column(Integer)

    def __init__(self, game_name, game_date, game_img, game_url, game_rating, game_price):
        self.game_name = game_name
        self.game_date = game_date
        self.game_img = game_img
        self.game_url = game_url
        self.game_rating = game_rating
        self.game_price = game_price

    def __str__(self):
        return self.game_name, self.game_date, self.game_img, self.game_url, self.game_rating, self.game_price


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class ScrapedData(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_web()

    def initialize_web(self):
        self.setGeometry(0, 0, 1000, 700)
        self.setWindowTitle("CreepyCrawler")
        self.setWindowIcon(QIcon("images/window_icon.jpg"))
        self.create_connection()
        self.set_up_widget()
        self.show()

    def create_connection(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("steamcrawler.db")
        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1)
        tables_needed = {'steam_data'}
        tables_not_found = tables_needed - set(database.tables())
        if tables_not_found:
            QMessageBox.critical(None, "Error",
                                 f"The following tables are missing from the database: {tables_not_found}")
            sys.exit(1)

    def set_up_widget(self):
        try:
            with open("scrape_info.csv", "r", newline="", encoding="utf-8") as r:
                reader4 = reader(r)
                for row in reader4:
                    game = Game(row[0], row[1], row[2], row[3], row[4], row[5])
                    session.add(game)
                    session.commit()
        except FileNotFoundError:
            print("u fucked")
        self.model = QSqlRelationalTableModel()
        self.model.setTable('steam_data')
        self.model.setHeaderData(self.model.fieldIndex('id'), Qt.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex('game_name'), Qt.Horizontal, "Game Name")
        self.model.setHeaderData(self.model.fieldIndex('release_date'), Qt.Horizontal, "Game Date")
        self.model.setHeaderData(self.model.fieldIndex('game_img'), Qt.Horizontal, "Game Image")
        self.model.setHeaderData(self.model.fieldIndex('game_url'), Qt.Horizontal, "Game URL")
        self.model.setHeaderData(self.model.fieldIndex('game_rating'), Qt.Horizontal, "Game Rating")
        self.model.setHeaderData(self.model.fieldIndex('game_price'), Qt.Horizontal, "Game Price")
        self.model.select()

        self.table_view2 = QTableView()
        self.table_view2.setModel(self.model)
        self.table_view2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view2.setSelectionMode(QTableView.SingleSelection)
        self.table_view2.setSelectionBehavior(QTableView.SelectRows)
        delegate = QSqlRelationalDelegate(self.table_view2)
        self.table_view2.setItemDelegate(delegate)
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.table_view2)
        self.setLayout(main_v_box)


app = QApplication(sys.argv)
window = ScrapedData()
sys.exit(app.exec_())
