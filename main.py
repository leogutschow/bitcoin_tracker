from selenium_crawler import FirefoxCrawler
from databaseconnector import ConexaoSQL
from graphshow import Grafico

def main():
    firefox = FirefoxCrawler()
    firefox.entraSite(firefox.dados["CoinMarketCap"]["home"])
    nomes, precos = firefox.pegaPrecos()

    sql = ConexaoSQL()
    sql.acrescentaValores(moedas=nomes, precos=precos)
    valores = sql.imprimeValores()

    print(valores)

    graph = Grafico()
    graph.showGraph(valores)
    
    firefox.sair()
    sql.fechar()

if __name__ == "__main__":
    main()