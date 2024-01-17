from selenium.webdriver.common.by import By

class LoginLocators(object):
    INPUT_USERNAME = (By.XPATH,"//input[@id='user-name']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='password']")
    BTN_LOGIN = (By.XPATH, "//input[@id='login-button']")