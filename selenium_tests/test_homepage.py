from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless=new') # For Chrome 109+

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service) 

try:
    # Replace this URL with the actual page you want to test
    # For demonstration, we'll use a local HTML file with your button
    # In a real test, you would use your actual website URL
    driver.get("http://127.0.0.1:5000/")
    
    print("Driver title: " + driver.title)
    initial_url = driver.current_url
    print("Current url: " + initial_url)
    
    # Find the button element using its class and href attributes
    button_register = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[@href="/register" and contains(@class, "btn")]')
        )
    )
    # Assert that the button exists and is displayed
    assert button_register.text.lower() in "get started", "Register button is not present on the page"
    
    # Print success message
    print("TEST PASSED: Register button exists and contains text 'Get Started' on the page")
    
    # Highlight the button for 3 seconds to make it visible during the test
    driver.execute_script("arguments[0].style.border='3px solid red'", button_register)
    time.sleep(5)
    
except Exception as e:
    print(f"TEST FAILED: {str(e)}")
    
finally:
    # Close the browser
    driver.quit()