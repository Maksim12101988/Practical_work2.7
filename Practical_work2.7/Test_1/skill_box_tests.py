from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Test_1.page_object import SkillBoxPage

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        skill_box_page = SkillBoxPage(driver)
        driver.get("https://skillbox.ru/code")
        print(f"Title of the initial page: {skill_box_page.title}")

        skill_box_page.click_search_button()
        skill_box_page.navigate_to_faculty_page()

        first_section_texts = skill_box_page.get_first_section_texts()
        second_section_texts = skill_box_page.get_second_section_texts()

        print("First section elements:")
        for text in first_section_texts:
            print(text)

        print("\nSecond section elements:")
        for text in second_section_texts:
            print(text)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
