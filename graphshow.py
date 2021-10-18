# importing the required module
import matplotlib.pyplot as plt
from databaseconnector import ConexaoSQL

class Grafico:
    def __init__(self):
        self.dias = []
        self.bitcoin = []
        self.etherium = []
        self.cardano = []
        self.tether = []
        self.binance_coin = []
        self.xrp = []
        self.solana = []
        self.polkadot = []
        self.usd_coin = []
        self.doge_coin = []
     

    def separaValores(self, lista:list):
        '''
        Recebe uma lista de dicionários vindos do SQL e os separa para os dados do gráfico
        '''
        for dicionario in lista:
            if dicionario["dia"] not in self.dias:
                self.dias.append(dicionario["dia"])

            if dicionario["nome"] == "Bitcoin":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.bitcoin.append(int(base_valor))

            if dicionario["nome"] == "Ethereum":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.etherium.append(int(base_valor))

            if dicionario["nome"] == "Cardano":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.cardano.append(int(base_valor))

            if dicionario["nome"] == "Tether":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.tether.append(int(base_valor))

            if dicionario["nome"] == "BinanceCoin":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.binance_coin.append(int(base_valor))

            if dicionario["nome"] == "XRP":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.xrp.append(int(base_valor))

            if dicionario["nome"] == "Solana":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.solana.append(int(base_valor))

            if dicionario["nome"] == "Polkadot":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.polkadot.append(int(base_valor))

            if dicionario["nome"] == "USDCoin":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.usd_coin.append(int(base_valor))

            if dicionario["nome"] == "Dogecoin":
                base_valor = dicionario["preco"][2:-3].replace(',', '')
                self.doge_coin.append(int(base_valor))


        return self.dias, self.bitcoin, self.etherium, self.cardano, self.tether, self.binance_coin, self.xrp, self.solana, self.polkadot, self.usd_coin, self.doge_coin


    def showGraph(self, valores:list):
        dias, bitcoin, etherium, cardano, tether, binance_coin, xrp, solana, polkadot, usd_coin, doge_coin = self.separaValores(valores)
        plt.plot(dias, bitcoin) #, bitcoin
        # plt.plot(dias,etherium)
        # plt.plot(dias,cardano)
        # plt.plot(dias,tether)
        # plt.plot(dias,binance_coin)
        # plt.plot(dias,xrp)
        # plt.plot(dias,solana)
        # plt.plot(dias,polkadot)
        # plt.plot(dias,usd_coin)
        # plt.plot(dias,doge_coin)

        plt.xlabel('Dias')
        plt.ylabel('Preços')
        plt.title('Preços Criptomoedas por Dia')
    
    # function to show the plot
        plt.show()

if __name__ == "__main__":
    graph = Grafico()
    sql = ConexaoSQL()
    sql = sql.imprimeValores()
    graph.showGraph(sql)