import email
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote import webelement
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
        driver.get("http://127.0.0.1:5000/login")
        print("Driver title: " + driver.title)
        initial_url = driver.current_url
        print("Current url: " + initial_url)

    except Exception as e: # perhaps the application is not running well on localhost
        print(f"Localhost cannot be loaded: {str(e)}")

    finally:
        return driver

def teardown(driver):
    time.sleep(waitingTime)
    driver.quit()
    print("Browser closed.")


def test_login_form_exists():
    try:
        driver = setup()

        # Find the form element using its action attribute
        form_login = WebDriverWait(driver, waitingTime).until(
            EC.presence_of_element_located(
                (By.XPATH, '//form[@action="/login"]')
            )
        )
        assert form_login.is_displayed(), "Login form is not present on the page"
        print(f"Login form is present on page {driver.current_url}.")
        time.sleep(waitingTime)

    except Exception as e:
        print(f"TEST FAILED: {str(e)}")
    
    finally:
        return driver
        

def test_invalid_email(driver):
    try:
        # Find the email input box
        # By this time email input field should have been present for a few seconds, no need to wait for it to show up 
        email_field = driver.find_element(By.ID, 'email')
        assert email_field.is_displayed(), "Email input field is not present on the page"

        password_field = driver.find_element(By.ID, 'password')
        assert password_field.is_displayed(), "Password input field is not present on the page"

        email_field.send_keys("John Doe")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.ENTER)
        print("Input is provided in the fields and ENTER key is pressed")

        invalid_feedback = WebDriverWait(driver, waitingTime).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Invalid email address')]")
            )
        )

        # Assert that the buttons exist and contain the desired text
        assert invalid_feedback.is_displayed(), "Invalid email is not triggering visual feedback"
        print("Feedback over invalid email is present on the login page.")

    except Exception as e:
        print(f"TEST FAILED: {str(e)}")


def test_empty_password(driver):
    try:
        email_field = driver.find_element(By.ID, 'email')
        email_field.send_keys("John Doe")
        
        password_field = driver.find_element(By.ID, 'password')
        password_field.clear()
        
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        validation_msg =  password_field.get_attribute("validationMessage")
        print("Password is emptied and submit button is pressed.")

        # Assert that the buttons exist and contain the desired text
        assert "Please fill out this field" in validation_msg, "Empty password is not triggering validation message"
        print("Vlidation message over empty password is activated.")

    except Exception as e:
        print(f"Test fails because: {str(e)}")
    
    finally:
        teardown(driver)


if __name__ == "__main__":
    drv = test_login_form_exists()
    test_invalid_email(drv)
    test_empty_password(drv)