class BasePage(object):
    """Classe base para inicializar a página base que será chamada de todos Páginas"""

    def __init__(self, driver):
        self.driver = driver
