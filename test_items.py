from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_form(browser):
    try:
        browser.get(link)

        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
            "form#add_to_basket_form"))
        )
    except TimeoutException:
        # print("Failed:(")
        assert False
    else:
        # print(button)
        assert True
    finally:
        time.sleep(30)
        browser.quit()
