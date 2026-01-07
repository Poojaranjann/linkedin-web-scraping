import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Load environment variables
load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

if not EMAIL or not PASSWORD:
    raise ValueError("Missing LINKEDIN_EMAIL or LINKEDIN_PASSWORD in .env file")


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    return driver


def login(driver):
    wait = WebDriverWait(driver, 20)

    print("Opening LinkedIn login page...")
    driver.get("https://www.linkedin.com/login")

    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    email_input.send_keys(EMAIL)

    password_input = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(PASSWORD)

    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    # Confirm login success
    wait.until(
        EC.presence_of_element_located((By.ID, "global-nav"))
    )

    print("Login successful!")


def main():
    driver = create_driver()
    login(driver)

    input("Login complete. Press Enter to close browser...")
    driver.quit()


if __name__ == "__main__":
    main()
