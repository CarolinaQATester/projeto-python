from pages.loginPage import LoginPages
from tests.baseTest import BaseTest

class TestLogin(BaseTest):
    
       
    def deve_preencher_login_sucesso(self):
        LoginPages.deve_preencher_login_sucesso()
        texto_esperado = "Products"
        assert(texto_esperado, LoginPages.deve_validar_titulo()) == texto_esperado
        
  