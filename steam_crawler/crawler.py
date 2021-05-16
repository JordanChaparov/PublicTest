from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap, QMovie, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QVBoxLayout, QMessageBox, QPushButton, \
    QLabel, QGridLayout, QDesktopWidget, QScrollArea, QDialog
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from csv import reader, writer
import time
import os
from urllib.error import HTTPError
from urllib import request
import re
import matplotlib.pyplot as plt
import pandas as pd
import textwrap


Style_sheets = """
    QLabel {background-color: #FFFFFF;
                         border-width: 2px;
                         border-style: solid;
                         border-radius: 4px;
                         border-color: #FABB4C}
    QPushButton {background-color: #BC2313;
                 color: #000000}
    QPushButton:pressed {background-color: #BDAAE0;
                         border-radius: 12px;
                         color: #DFD8D7}
    """


class CreepyCrawler:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.WEB_DRIVER_PATH = "../steam_crawler/chromedriver/chromedriver.exe"
        self.chrome = webdriver.Chrome(self.WEB_DRIVER_PATH, options=options)
        self.load_user_info()
        self.steam_login()

    def load_user_info(self):
        """
        Reads information from users_info.csv file and loads it into variables, which are later used to login into
        steam and email websites.
        """
        with open("users_info.csv", mode="r") as f:
            reader1 = reader(f, delimiter=",")
            for row in reader1:
                self.steam_username = row[0].strip()
                self.steam_password = row[1].strip()
                self.email_username = row[2].strip()
                self.email_password = row[3].strip()

    def steam_login(self):
        """
        Loads the steam page.
        Clicks login button on the steam page, then looks for steam username and password fields and inputs
        the username and password and clicks the login button to enter the selected profile.
        After the steam guard pops up, this function opens a new window (https://www.abv.bg) and focuses it.
        It waits a couple of seconds to receive email from the steam guard on the user's email address.
        Then it looks, selects and inputs username and password into the proper fields and logs into the user's email.
        After that it clicks on the last received email (from steam guard) and opens it. It reads the message, saves
        the received code from the steam guard on steam_code variable and closes the email window.
        Finally it focuses back on the steam website, looks for the authenticator field, inputs and verifies,
        the code and logs in into the user's steam account.
        """
        # loads steam page
        self.chrome.get("https://store.steampowered.com/search/?filter=topsellers")
        # clicks the login button on top of the steam page.
        self.chrome.find_element_by_tag_name("a.global_action_link").send_keys(Keys.RETURN)
        # searches for the username field in the loaded page and inputs the given username.
        self.enter_username = self.chrome.find_elements_by_css_selector("input#input_username.text_field")[0]
        self.enter_username.send_keys(self.steam_username)
        time.sleep(1)

        # searches for the password field in the loaded page and inputs the given password, then moves to the
        # login button and clicks it to log the user in, BUT steam guard appears.
        self.enter_password = self.chrome.find_elements_by_css_selector("input#input_password.text_field")[0]
        self.enter_password.send_keys(self.steam_password + Keys.TAB + Keys.RETURN)
        time.sleep(1)

        # opens a new tab in the chrome browser, loads the given address, switches focus to it and waits 15 seconds
        # to receive email on the user's mail address from steam guard.
        self.chrome.execute_script("window.open('https://www.abv.bg')")
        self.chrome.switch_to.window(self.chrome.window_handles[1])
        time.sleep(15)

        # searches and selects the email's username and password fields, inputs the given username and password
        # and clicks the login button to log in the user into his email.
        self.input_abv_fields = self.chrome.find_elements_by_tag_name("input#username.abv-LoginField")[0]
        self.input_abv_fields.send_keys(self.email_username + Keys.TAB + self.email_password + Keys.RETURN)
        time.sleep(1)

        # clicks on the inbox button
        self.chrome.find_elements_by_css_selector("td.foldersCell")[0].click()
        time.sleep(1)

        # clicks on the last received email (it will be from steam guard)
        self.chrome.find_elements_by_css_selector(
            "td.inbox-cellTableCell.GG3HBNKBDI.inbox-cellTableSecondColumn")[0].click()
        time.sleep(1)

        # selects the sent steam code from steam guard from the received message and saves its value
        self.steam_code = self.chrome.find_elements_by_css_selector("td")[-19].text
        print(self.steam_code)
        time.sleep(1)

        # closes the email tab and switches focus on the awaiting steam page
        self.chrome.execute_script("window.close('https://www.abv.bg')")
        self.chrome.switch_to.window(self.chrome.window_handles[0])

        # searches for the authenticator text field and clicks it
        self.authenticator = self.chrome.find_elements_by_css_selector(
            "input#authcode.authcode_entry_input.authcode_placeholder")[0]
        self.authenticator.click()

        # inputs the code it received on the given email and successfully logs in onto the user's steam account
        self.authenticator.send_keys(self.steam_code + Keys.RETURN)
        time.sleep(2)
        self.chrome.find_element_by_css_selector("a#success_continue_btn.auth_button").send_keys(Keys.RETURN)
        self.chrome.maximize_window()
        time.sleep(10)
        self.chrome.close()


class WebScrape:
    def __init__(self, rows_num):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.WEB_DRIVER_PATH = "../steam_crawler/chromedriver/chromedriver.exe"
        self.chrome = webdriver.Chrome(self.WEB_DRIVER_PATH, options=options)
        self.rows_num = rows_num
        self.web_scraping()
        self.write_file()

    def web_scraping(self):
        """
        Uses the Chrome web browser to load steam's most sold games page, scrolls down the given number of pages,
        scrapes various information(game names, links and etc) and appends it to the appropriate list.
        """
        self.game_names = []
        self.game_release = []
        self.game_images = []
        self.game_urls = []
        self.game_ratings = []
        self.game_prices = []

        # load steam page, scroll down and search for game names, images, links etc. in the source code of the page
        self.chrome.get("https://store.steampowered.com/search/?filter=topsellers")
        time.sleep(3)
        body = self.chrome.find_element_by_tag_name("body")
        num_pages = int(self.rows_num / 20)
        while num_pages > 0:
            body.send_keys(Keys.PAGE_DOWN)

            for i in range(0, self.rows_num):
                self.search_name = self.chrome.find_elements_by_tag_name('span.title')[i].text
                self.search_release = self.chrome.find_elements_by_tag_name(
                    "div.col.search_released.responsive_secondrow")[i].text
                self.search_image = self.chrome.find_elements_by_css_selector("div#search_resultsRows [src]")[i]
                self.search_url = self.chrome.find_elements_by_css_selector("div#search_resultsRows [href]")[i]
                self.search_rating = self.chrome.find_elements_by_tag_name("div.col.search_reviewscore")[i]
                self.search_price = self.chrome.find_elements_by_tag_name(
                    "div.col.search_price_discount_combined.responsive_secondrow")[i].text

                self.game_names.append(self.search_name)
                self.game_release.append(self.search_release)
                self.game_images.append(self.search_image.get_attribute("src"))
                self.game_urls.append(self.search_url.get_attribute("href"))
                if not self.search_rating.find_elements_by_tag_name("span"):
                    self.game_ratings.append("None")
                else:
                    text_rating = str(
                        self.search_rating.find_element_by_tag_name("span").get_attribute("data-tooltip-html"))
                    self.game_ratings.append(text_rating.replace("<br>", ". "))
                game_price = str(self.search_price).replace("\n", "|")
                self.game_prices.append(game_price)

            time.sleep(2)
            num_pages -= 1
        time.sleep(2)
        self.chrome.close()

    def write_file(self):
        """
        Checks if the file already exists. If it exists it deletes it.
        Then it saves the scraped data from steam in a csv file.
        """
        if os.path.exists("scrape_info.csv"):
            os.remove("scrape_info.csv")

        with open("scrape_info.csv", mode="w", newline="", encoding="utf-8") as g:
            writer1 = writer(g, delimiter=",")
            for row in range(0, self.rows_num):
                row_list = [self.game_names[row], self.game_release[row], self.game_images[row], self.game_urls[row],
                            self.game_ratings[row], self.game_prices[row]]
                writer1.writerow(row_list)


class WebWeaver(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_web()

    def initialize_web(self):
        self.setGeometry(0, 0, 1000, 700)
        self.setWindowTitle("CreepyCrawler")
        self.setWindowIcon(QIcon("images/window_icon.jpg"))
        self.table_cols = 0
        self.table_rows = 0
        self.set_up_widgets()
        self.show()

    def load_table(self):
        """Reads the scraped info from a scv file (scraped_info.csv) and loads it into a table."""
        try:
            with open("scrape_info.csv", "r", newline="", encoding="utf-8") as h:
                reader2 = reader(h)
                headers = ["GAME NAME", "GAME RELEASE DATE", "GAME IMAGE", "GAME URL", "GAME RATING", "GAME PRICE"]
                self.model.setHorizontalHeaderLabels(headers)
                for i, row in enumerate(reader2):
                    items = [QStandardItem(item) for item in row]
                    self.model.insertRow(i, items)
                    self.table_rows = i
                self.teble_cols = len(headers)
        except FileNotFoundError:
            QMessageBox().warning(self, "File not found message", "The table file was not found!",
                                  QMessageBox.Ok, QMessageBox.Ok)

    def set_up_widgets(self):
        """Creates widgets and layouts and arranges them into the window."""

        self.main_label = QLabel(self)
        bw_label = QLabel(self)
        elise_label = QLabel(self)
        cocoons_label = QLabel(self)
        title_label = QLabel(self)

        images_list = ["images/web.jpg", "images/s-l400.jpg", "images/th.jpg", "images/cocoons.jpg", "images/title.jpg"]
        labels_list = [self.main_label, bw_label, elise_label, cocoons_label, title_label]

        try:
            for i in range(0, len(images_list)):
                with open(images_list[i]):
                    pixmap = QPixmap(images_list[i])
                    labels_list[i].setPixmap(pixmap)
                    labels_list[i].setAlignment(Qt.AlignCenter)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error Message", "Image file can't be found", QMessageBox.Ok, QMessageBox.Ok)

        movie = QMovie("images/spider_animation.gif")
        crawler_label = QLabel(self)
        crawler_label.setMovie(movie)
        movie.start()

        login_button = QPushButton("Log in", self)
        login_button.setFont(QFont("Arial", 16))
        login_button.setFixedSize(150, 25)
        login_button.clicked.connect(self.login_acc)
        scrape_steam_button = QPushButton("Scrape Steam", self)
        scrape_steam_button.setFont(QFont("Arial", 16))
        scrape_steam_button.setFixedSize(150, 25)
        scrape_steam_button.clicked.connect(self.scrape)
        img_view_button = QPushButton("Image Scrape", self)
        img_view_button.setFont(QFont("Arial", 16))
        img_view_button.setFixedSize(150, 25)
        img_view_button.clicked.connect(self.scrape_images)
        show_diagram_button = QPushButton("Show Diagram", self)
        show_diagram_button.setFont(QFont("Arial", 16))
        show_diagram_button.setFixedSize(150, 25)
        show_diagram_button.clicked.connect(self.show_diagram)
        quit_button = QPushButton("Quit", self)
        quit_button.setFont(QFont("Arial", 16))
        quit_button.setFixedSize(150, 25)
        quit_button.clicked.connect(self.close)

        button_v_box = QVBoxLayout()
        button_v_box.addWidget(login_button)
        button_v_box.addWidget(scrape_steam_button)
        button_v_box.addWidget(img_view_button)
        button_v_box.addWidget(show_diagram_button)
        button_v_box.addWidget(quit_button)
        button_v_box.addStretch()
        button_v_box.setContentsMargins(50, 10, 10, 10)

        self.model = QStandardItemModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.model.setRowCount(self.table_rows)
        self.model.setColumnCount(self.table_cols)

        self.not_quite_grid = QGridLayout()
        self.not_quite_grid.setContentsMargins(5, 5, 5, 5)
        self.not_quite_grid.addWidget(self.main_label)

        main_grid = QGridLayout()
        main_grid.setObjectName("grid")
        main_grid.addWidget(title_label, 0, 1)
        main_grid.addWidget(elise_label, 0, 2)
        main_grid.addWidget(bw_label, 1, 0)
        main_grid.addLayout(self.not_quite_grid, 1, 1)
        main_grid.addLayout(button_v_box, 1, 2)
        main_grid.addWidget(cocoons_label, 2, 1)
        main_grid.addWidget(crawler_label, 2, 2)
        self.setLayout(main_grid)

    def login_acc(self):
        """Uses the CreepyCrawler class to log into the steam website."""
        CreepyCrawler()

    def scrape(self):
        """Uses the WebScrape class to scrape data from steam website. Then it loads the table with the scraped data."""
        WebScrape(25)
        self.load_table()
        self.not_quite_grid.replaceWidget(self.main_label, self.table_view)
        self.main_label.close()
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setColumnWidth(0, 250)
        self.table_view.setColumnWidth(1, 130)
        self.table_view.setColumnWidth(2, 130)
        self.table_view.setColumnWidth(3, 280)
        self.table_view.setColumnWidth(4, 322)
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width()-10, screen.height()-100)
        self.repaint()

    def scrape_images(self):
        """THE DREAM!!!
        Scrapes data from steam and creates labels to load the data. Labels can be designed to look however we like and
        they can also load pictures. That way we can design our GUI to the specifics of the user and not just output
        a plain old excel table."""
        WebScrape(25)
        self.main_label.close()
        self.table_view.close()
        data_list = []
        headers = ["GAME NAME", "GAME RELEASE DATE", "GAME IMAGE", "GAME URL", "GAME RATING", "GAME PRICE"]
        self.label_names = []

        dialog1 = QDialog()
        dialog1.layout = self.not_quite_grid

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.mini_grid = QGridLayout(self.scrollAreaWidgetContents)
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        dialog1.layout.addWidget(self.scroll)

        self.game_name = QLabel()
        self.game_release = QLabel()
        self.game_image = QLabel(self)
        self.game_url = QLabel()
        self.game_rating = QLabel()
        self.game_price = QLabel()

        self.game_name.setText(headers[0])
        self.game_name.setAlignment(Qt.AlignCenter)
        self.game_release.setText(headers[1])
        self.game_release.setAlignment(Qt.AlignCenter)
        self.game_image.setText(headers[2])
        self.game_image.setAlignment(Qt.AlignCenter)
        self.game_url.setText(headers[3])
        self.game_url.setAlignment(Qt.AlignCenter)
        self.game_rating.setText(headers[4])
        self.game_rating.setAlignment(Qt.AlignCenter)
        self.game_price.setText(headers[5])
        self.game_price.setAlignment(Qt.AlignCenter)

        self.mini_grid.addWidget(self.game_name, 0, 0)
        self.mini_grid.addWidget(self.game_release, 0, 1)
        self.mini_grid.addWidget(self.game_image, 0, 2)
        self.mini_grid.addWidget(self.game_url, 0, 3)
        self.mini_grid.addWidget(self.game_rating, 0, 4)
        self.mini_grid.addWidget(self.game_price, 0, 5)

        try:
            with open("scrape_info.csv", "r", newline="", encoding="utf-8") as h:
                reader2 = reader(h)
                for i, row in enumerate(reader2):
                    data_list.append(row)
                    self.label_names.append("name" + str(i))
                    self.label_names.append("release" + str(i))
                    self.label_names.append("image" + str(i))
                    self.label_names.append("url" + str(i))
                    self.label_names.append("rating" + str(i))
                    self.label_names.append("price" + str(i))

                    self.label_names[i] = QLabel()
                    self.label_names[i].setText(row[0])

                    self.label_names[i+1] = QLabel()
                    self.label_names[i+1].setText(row[1])

                    self.label_names[i+2] = QLabel(self)
                    pixmap = QPixmap()
                    url = row[2]
                    try:
                        data = request.urlopen(url).read()
                    except HTTPError as err:
                        print(err.code)

                    if HTTPError:
                        self.label_names[i+2].setText("None")
                    else:
                        pixmap.loadFromData(data)
                        self.label_names[i+2].setPixmap(pixmap)

                    self.label_names[i+3] = QLabel()
                    url_link = "<a href=\""+row[3]+"\"><font face=verdana size=12 color=black>LINK</font></a>"
                    self.label_names[i+3].setText(url_link)
                    self.label_names[i+3].setAlignment(Qt.AlignCenter)

                    self.label_names[i+4] = QLabel()
                    self.label_names[i+4].setText(row[4])
                    self.label_names[i+5] = QLabel()
                    self.label_names[i+5].setText(row[5])

                    self.mini_grid.addWidget(self.label_names[i], i+1, 0)
                    self.mini_grid.addWidget(self.label_names[i+1], i+1, 1)
                    self.mini_grid.addWidget(self.label_names[i+2], i+1, 2)
                    self.mini_grid.addWidget(self.label_names[i+3], i+1, 3)
                    self.mini_grid.addWidget(self.label_names[i+4], i+1, 4)
                    self.mini_grid.addWidget(self.label_names[i+5], i+1, 5)
        except FileNotFoundError:
            QMessageBox().warning(self, "File not found message", "The table file was not found!",
                                  QMessageBox.Ok, QMessageBox.Ok)
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width() - 10, screen.height() - 100)
        self.repaint()

    def show_diagram(self):
        """Show diagram of the game ratings."""
        pattern1 = r"(\d.)%"
        ratings = []

        try:
            with open("scrape_info.csv", "r", newline="", encoding="utf-8") as i:
                reader3 = reader(i)
                for row in reader3:
                    rating = re.findall(pattern1, row[4])
                    if not rating:
                        ratings.append(0)
                    else:
                        ratings.append(int(rating[0]))

        except FileNotFoundError:
            QMessageBox().warning(self, "File not found message", "The table file was not found!",
                                  QMessageBox.Ok, QMessageBox.Ok)

        df = pd.read_csv("scrape_info.csv", ",", names=["game", "date", "img", "url", "rating", "price", "percentage"])
        df["percentage"] = ratings

        plt.style.use("ggplot")
        fig, ax = plt.subplots()
        df.plot(kind="barh", y="percentage", x="game", ax=ax, figsize=(20, 9))
        ax.set_xticks(range(0, 100, 5))
        f = lambda x: textwrap.fill(x.get_text(), 35)
        ax.set_yticklabels(map(f, ax.get_yticklabels()))
        ax.set(title="Steam Game Ratings", xlabel="Percentage", ylabel="Games")
        plt.tight_layout()
        plt.show()


app = QApplication(sys.argv)
app.setStyleSheet(Style_sheets)
window = WebWeaver()
sys.exit(app.exec_())
