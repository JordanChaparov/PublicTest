IMPORTANT ===> The script runs with chromedriver for Chrome Version 90.0.4430.212 <===
If you have another version of Chrome, please download the webdriver from "https://chromedriver.chromium.org/downloads".
Make sure to unzip the webdriver into the chromedriver folder!

The CreepyCrawler class is used only to log in to my steam account (please don't abuse it...) using the information from
users_info.csv file. Now the right way to do this is with virtual environment, but hey... I'm not a mainstream guy.

NOTE: If you change the information into the users_info.csv you can log with your steam account only if you use an email
from abv.bg. Other sites won't work because they are made with other html code so... yeah.
NOTE2: If the guys from abv.bg or steam change their html code something might not work because its fine tuned, but I
should update my code if something changes... generally that's how the crawlers work... they run and you chase.

The WebScrape class uses the Chrome web browser to load steam's most sold games page, scrolls down the given number of
pages, scrapes various information(game names, links and etc), downloads it to scrape_info.csv file.

The WebWeaver class uses the information from scrape_info.csv file to display the downloaded data from steam in custom
table. The class uses PyQt5, Matplotlib modules and some sprinkle of css code.

NOTE: Images can be loaded in the GameImage column only if the guys from steam don't deny the access to the image paths.
So if you are lucky and they forget at some point you might actually see images loaded in the labels. I'll upload an
image file as proof the my code works as intended though.
NOTE2: DB_Crawler.py works with database instead of csv file, but there is just a plain old excel table to see.
NOTE3: If something doesn't work its YOU... haha... just make sure you have chrome and the webdriver supports your
chrome browser version and all be fine... trust me, I've already crashed this script a thousand times.

CREDITS: Bate Da4ko - your friendly neighbour sociopath.