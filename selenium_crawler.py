from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.common.exceptions as SeleniumException
import time


class FirefoxCrawler():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"D:\VisualStudioCode\SeleniumProjectBitCoin\driver\geckodriver.exe")
        '''
        Os dados estão em um dicionário para, caso precise, adicionar mais dados
        '''
        self.dados ={
            "CoinMarketCap" : {
                "home" : "https://coinmarketcap.com/pt-br/all/views/all/",                
            }
        }

    def entraSite(self, site: str, timeout: int = 10):
        
        t = time.time()
        self.driver.set_page_load_timeout(timeout)

        try:
            self.driver.get(site)

        except TimeoutException:
            self.driver.execute_script("window.stop();")

        print('Time consuming:', time.time() - t)


    def retornaElemento(self, tipo_elemento:str = "", nome_elemento: str = ""):
        '''
        Retorna um elemento dentro da página a partir do tipo de busca que queremos, da tag HTML e o como ele se identifica
        '''


        if tipo_elemento == "id":
            wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, nome_elemento)))
            return self.driver.find_element_by_id(nome_elemento)

        elif tipo_elemento == "class":
            wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, nome_elemento)))
            return self.driver.find_element_by_class_name(nome_elemento)
        
        elif tipo_elemento == "css":
            wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, nome_elemento)))
            return self.driver.find_element_by_css_selector(nome_elemento)
        
        elif tipo_elemento == "xpath":
            wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, nome_elemento)))
            return self.driver.find_element_by_xpath(nome_elemento)

        else:
            return None


    def pegaPrecos(self):

        '''
        Pega a lista das 10 primeiras Moedas e seus preços e retorna suas listas
        '''

        lista_elementos = self.retornaElemento(tipo_elemento="xpath", nome_elemento="/html/body/div/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/table/tbody")

        lista_elementos = lista_elementos.find_elements_by_tag_name("tr")

        list_nomes = []
        list_precos = []

        for elemento in lista_elementos[:10]:
            preco = elemento.find_element_by_css_selector("td:nth-child(5) > div:nth-child(1) > a:nth-child(1)").get_attribute("text")
            nome = elemento.find_element_by_css_selector("td:nth-child(2) > div:nth-child(1) > a:nth-child(3)").get_attribute("text")
            
            
            list_nomes.append(nome.replace(" ", ""))
            list_precos.append(preco)


        return list_nomes, list_precos

    
    def verificaPopup(self):
        alert = webdriver.common.alert.Alert(self.driver)
        alert.dismiss()
        
    def novaAba(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

    def sair(self):
        self.driver.close()


if __name__ == "__main__":

    firefox = FirefoxCrawler()
    #Lojas Americanas
    firefox.entraSite(firefox.dados["CoinMarketCap"]["home"])
    print(firefox.pegaProduto())
    


    firefox.sair()



