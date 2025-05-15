from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# waiting time for elements to load
waitingTime = 1

options = webdriver.ChromeOptions()
options.add_argument('--headless=new') # For Chrome 109+
options.add_argument('--start-maximized') # without maximising the window error message appears

service = Service(executable_path="chromedriver.exe")

def setup():
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(waitingTime)
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

        # driver.implicitly_wait(waitingTime)
        button_register.click()
        assert driver.current_url.split('/')[-1] == "register", "Clicking on signup does not open registering page."
        print("Sign Up button is clicked.")

        form_register = WebDriverWait(driver, waitingTime).until(
            EC.presence_of_element_located(
                (By.XPATH, '//form[@action="/register"]')
            )
        )
        assert form_register.is_displayed(), "Registration form is not present on the page"
        print(f"The registering page is open on {driver.current_url} and the registration form is present on.")

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
        print(f"Login button is clicked and login page shows up on {driver.current_url}")

    except Exception as e:
        print(f"TEST FAILED: {str(e)}")
    
    finally:
        teardown(driver)

def test_explanation_display():
    try:
        driver = setup()
        
        # Check if upload, analyze and improve exist in the page
        upload = driver.find_element(By.XPATH, '//h3[contains(text(), "1. Upload")]')
        analyse = driver.find_element(By.XPATH, '//h3[contains(text(), "2. Analyze")]')
        improve = driver.find_element(By.XPATH, '//h3[contains(text(), "3. Improve")]')

        assert upload.is_displayed(), "Upload is not present on the page"
        print("Upload is present on the page")

        assert analyse.is_displayed(), "Analyze is not present on the page"
        print("Analyze is present on the page")
        
        assert improve.is_displayed(), "Improve is not present on the page"
        print("Improve is present on the page")

    except Exception as e:
        print(f"Test fails because: {str(e)}")
    
    finally:
        teardown(driver)


if __name__ == "__main__":
    test_signup_button()
    test_login_button()
    test_explanation_display()