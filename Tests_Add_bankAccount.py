from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email = 'powerpuff2k@gmail.com'
password = 'password1'

driver = webdriver.Chrome(executable_path=r"C:\Users\power\chromedriver_win32\chromedriver.exe")
driver.get("https://www.xero.com/nz/")


email_field = driver.find_element_by_link_text('Login')

driver.maximize_window()


def login(self, email, password):
    self.email_field.sendkeys(email)
    self.password_field.sendkeys(password)
    self.password_field.send_keys(Keys.ENTER)

#
# time.sleep(5)
# emailInput = driver.find_element(By.ID('login'))
# emailInput.send_keys(email)


