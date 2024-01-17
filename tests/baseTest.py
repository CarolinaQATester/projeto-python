from selenium import webdriver

import time

class BaseTest:
    
     #inicialização
    def setup_class(self):
        self.driver = webdriver.FirefoxOptions()
        self.enable_headless()
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com/')
        time.sleep(2)
        
    def enable_headless(self):
      self.firefox_options.add_argument('--headless')
      
      #Fechar a conexao
    def teardown_class(self):
        self.driver.close()