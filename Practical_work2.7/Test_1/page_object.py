from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SkillBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    @property
    def title(self):
        return self.driver.title

    @property
    def search_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div/div[1]/div[1]/div[1]/a[2]")

    @property
    def faculty_page_url(self):
        return "https://skillbox.ru/code/faculty/backend-development/"

    @property
    def first_section_elements(self):
        return self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div/div[2]/div/section[1]/div[2]/*")

    @property
    def second_section_elements(self):
        return self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[2]/div/div[2]/div/section[2]/div[2]/*")

    def click_search_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_button))
        self.actions.click(self.search_button).perform()

    def navigate_to_faculty_page(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains(self.faculty_page_url))
        self.driver.get(self.faculty_page_url)

    def get_first_section_texts(self):
        return [element.text for element in self.first_section_elements]

    def get_second_section_texts(self):
        return [element.text for element in self.second_section_elements]
