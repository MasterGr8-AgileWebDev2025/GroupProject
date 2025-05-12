import email
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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

    

def test_empty_password():
    try:
        driver = setup()
        driver.implicitly_wait(waitingTime)
        
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
    drv = test_login_form_exists()
    test_invalid_email(drv)
    # test_empty_password(drv)