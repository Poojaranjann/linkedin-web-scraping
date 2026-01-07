import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

# 1. Load your login details from the .env file
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# 2. Setup the Chrome Browser
# This opens a real Chrome window that the script controls
driver = webdriver.Chrome() 

def login():
    # Go to the login page
    print("Opening LinkedIn...")
    driver.get("https://www.linkedin.com/login")
    time.sleep(3) # Wait for page to load

    # Enter Email
    driver.find_element("id", "username").send_keys(EMAIL)
    # Enter Password
    driver.find_element("id", "password").send_keys(PASSWORD)
    # Click Login
    driver.find_element("xpath", "//button[@type='submit']").click()
    
    print("Logged in! Keeping window open for 10 seconds...")
    time.sleep(60)

# Run the function
if __name__ == "__main__":
    login()
    
    # This keeps the window open until YOU press Enter in the terminal
    input("Press Enter in this terminal after you have finished the OTP/Login...")
    
    driver.quit()