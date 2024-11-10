from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep

class ReviewsPage:
    BASE_URL = "https://skillbox.ru/otzyvy/?direction=code"
    REVIEWS_PATH = "/html/body/div[1]/div/div/main/section[2]/div[2]"
    PAGE_TITLE = "Skillbox | Отзывы"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.BASE_URL)

    def is_loaded(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.REVIEWS_PATH))
        )

    def get_reviews(self):
        reviews_element = self.driver.find_element(By.XPATH, self.REVIEWS_PATH)
        return reviews_element.find_elements(By.XPATH, "./*")

    def has_reviews(self):
        return len(self.get_reviews()) > 0

    def check_reviews_presence(self):
        assert self.has_reviews(), "Отзывы отсутствуют на странице"
