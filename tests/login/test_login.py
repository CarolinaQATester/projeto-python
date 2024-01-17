from pages.loginPage import LoginPages
from tests.baseTest import BaseTest

class TestLogin(BaseTest):
    
       
    def deve_preencher_login_sucesso(self):
        LoginPages.deve_preencher_login_sucesso()
        
        
  