import pytest
import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#Задаем функцию, проверяющую наличие кнопки "Добавить в корзину"
def test_btn_add_basket_language(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button_basket = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    time.sleep(5)
    #time sleep для проверки смены языка
    assert button_basket, 'Кнопка не найдена'
    