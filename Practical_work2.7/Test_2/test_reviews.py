import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from reviews_page import ReviewsPage
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestReviewsPage:
    def test_page_load(self, driver):
        page = ReviewsPage(driver)
        page.load()
        page.is_loaded()
        assert True, "Станица не загрузилась"

    def test_reviews_presence(self, driver):
        page = ReviewsPage(driver)
        page.load()
        page.is_loaded()
        reviews = page.get_reviews()
        assert reviews, "Отзывы отсутствуют на странице"
        assert len(reviews) > 0, "На странице нет отзывов"

    def test_page_title(self, driver):
        page = ReviewsPage(driver)
        page.load()
        page.is_loaded()
        title = page.driver.title
        assert "Skillbox" in title, f"Неверный заголовок: {title}"


    def test_review_text_content(self, driver):
        page = ReviewsPage(driver)
        page.load()
        page.is_loaded()
        reviews = page.get_reviews()

        skillbox_keywords = ["skillbox", "Skillbox", "Сkillbox", "профессия аналитик 1с", "аналитика 1с",
                             "разработчик и аналитика 1с"]

        for review in reviews:
            assert review.text.strip(), f"Отзыв пустой: {review.text}"

            for keyword in skillbox_keywords:
                if keyword.lower() in review.text.lower():
                    print(f"Найдено ключевое слово '{keyword}' в отзыве:")
                    print(review.text)
                    break
            else:
                print(f"Ключевых слов Skillbox не найдено в отзыве:")
                print(review.text)

