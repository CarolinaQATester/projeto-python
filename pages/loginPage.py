
from locators.loginLocators import LoginLocators
from pages.basePage import BasePage



class LoginPages(BasePage):
    
    def deve_preencher_login_sucesso(self):
        input_username = self.driver.find_element(LoginLocators.INPUT_USERNAME)
        input_username.send_keys('standard_user')
        
        input_password =self.driver.find_element(LoginLocators.INPUT_PASSWORD)
        input_password.send_keys('secret_sauce')
        
        btn_login = self.driver.find_element(LoginLocators.BTN_LOGIN)
        btn_login.click()