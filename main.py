from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import json
import chromedriver_autoinstall

""" user specific information - modify OK """
# chromedriver path
PATH = "./chromedriver"
# Your friend's Snapchat username
friendsUsername = "test"
# Numbers only, no letters or symbols
streakLength = "5"

# ---------------------------------------------------------------
credentials = {"username":"","emailAddress":"","mobileNumber":""}
# required info
information = ("Our snapstreaks randomly disappeared today, even though we"
               " snapped each other multiple times yesterday and today, and the hourglass icon",
               " didn't show up either.")

# ---------------------------------------------------------------

""" website specific IDs - do not modify"""

URL = "https://support.snapchat.com/en-GB/i-need-help"
SUCCESS_URL = "https://support.snapchat.com/en-GB/success"
HELP_OPTION_ID = "5695496404336640"
USERNAME_INPUT_ID = "field-24281229"
EMAIL_INPUT_ID = "field-24335325"
PHONE_NUMBER_INPUT_ID = "field-24369716"
DEVICE_INPUT_ID = "field-24369726"
FRIEND_USERNAME_INPUT_ID = "field-24369736"
ISSUE_DATE_INPUT_ID = "field-24326423"
STREAK_LENGTH_INPUT_ID = "field-24641746"
DROPDOWN_HOURGLASS_TAG = 'i'
DROPDOWN_DATA_VALUE_CLASS = "//div[@data-value='hourglass-no']"
INFORMATION_INPUT_ID = "field-22808619"
SUBMIT_BUTTON_ID = "submit-button"
LAST = -1


# ---------------------------------------------------------------

def main():
   global friendsUsername
   global streakLength

   
   credentials["username"] = "kdsender383"
   credentials["emailAddress"] = "itssenderkd@gmail.com"
   credentials["mobileNumber"] = "+91 9848382920"


   chromedriver_autoinstall.install()
   if chromedriver_autoinstall.get_platform() == "mac":
      os.chmod('./chromedriver', 0o755)

   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_argument('--headless')  # Run in headless mode
   chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
   chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

   driver.get(URL)

   help_option = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, HELP_OPTION_ID)))
   help_option.send_keys(Keys.ENTER)

   # username
   username_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, USERNAME_INPUT_ID)))
   username_input.send_keys(credentials["username"])

   # email address
   email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, EMAIL_INPUT_ID)))
   email_input.send_keys(credentials["emailAddress"])

   # mobile number
   mobile_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, PHONE_NUMBER_INPUT_ID)))
   mobile_input.send_keys(credentials["mobileNumber"])

   # friend's username
   friend_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, FRIEND_USERNAME_INPUT_ID)))
   friend_input.send_keys(friendsUsername)

  
   # submit button
   submit_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, SUBMIT_BUTTON_ID))).click()

   WebDriverWait(driver, 1000).until(lambda driver: driver.current_url == SUCCESS_URL)
   driver.quit()

main()
