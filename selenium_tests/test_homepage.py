from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# waiting time for elements to load
waitingTime = 2

options = webdriver.ChromeOptions()
# options.add_argument('--headless=new') # For Chrome 109+

service = Service(executable_path="chromedriver.exe")

def setup():
    driver = webdriver.Chrome(options=options, service=service) 
    try:
        driver.get("http://127.0.0.1:5000/")
        print("Driver title: " + driver.title)
        initial_url = driver.current_url
        print("Current url: " + initial_url)

    except Exception as e: # perhaps the application is not running well on localhost
        print(f"Localhost cannot be loaded: {str(e)}")

    finally:
        return driver

def teardown(driver):
    driver.quit()
    print("Browser closed.")


def test_signup_button():
    try:
        driver = setup()
        # Find the button element using its class and href attributes
        button_register = WebDriverWait(driver, waitingTime).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@href="/register" and contains(@class, "btn")]')
            )
        )
        # Assert that the buttons exist and contain the desired text
        assert button_register.text.lower() in "sign up", "Sign Up button is not present on the page"
        print("Sign Up button is present on the homepage.")

        button_register.click()
        assert driver.current_url.split('/')[-1] == "register", "Clicking on signup does not open registering page."

        form_register = WebDriverWait(driver, waitingTime).until(
            EC.presence_of_element_located(
                (By.XPATH, '//form[@action="/register"]')
            )
        )
        assert form_register.is_displayed(), "Registration form is not present on the page"
        print(f"Registration form is present on page {driver.current_url}.")
        time.sleep(waitingTime)

    except Exception as e:
        print(f"TEST FAILED: {str(e)}")
    
    finally:
        teardown(driver)
        

def test_login_button():
    try:
        driver = setup()
        # Find the button element using its class and href attributes
        button_login = WebDriverWait(driver, waitingTime).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@href="/login" and contains(@class, "btn")]')
            )
        )
        # Assert that the buttons exist and contain the desired text
        assert button_login.text.lower() in "login", "Login button is not present on the page"
        print("Login button is present on the homepage.")

        button_login.click()
        assert driver.current_url.split('/')[-1] == "login", "Clicking on login button does not open login page."
        time.sleep(waitingTime)

    except Exception as e:
        print(f"TEST FAILED: {str(e)}")
    
    finally:
        teardown(driver)

if __name__ == "__main__":
    test_signup_button()
    test_login_button()