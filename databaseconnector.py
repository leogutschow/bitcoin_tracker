import pymysql.cursors
from datetime import datetime


class ConexaoSQL:
    def __init__(self):
        self.conexao = self.conecta()
        self.criptos = ["Bitcoin", "Ethereum", "Cardano", "Tether", "BinanceCoin", "XRP", "Solana", "Polkadot", "USDCoin", "Dogecoin"]
        print("Conectado com Sucesso!")

    def conecta(self):
        print("Conectando...")
        return pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            db = 'precos',
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor
        )

    def acrescenta_valores(self, moedas:list, precos:list):
        '''
        Pega os valores e os coloca na Base de Dados
        '''

        

        lista_tuplas = []
        for i in range(10):
            lista_tuplas.append((moedas[i], precos[i]))
 
        dia = datetime.now()
        dia = dia.strftime("%d/%m")
        with self.conexao.cursor() as cursor:
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS moedas ('
                    'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'nome VARCHAR(30) NOT NULL UNIQUE'
                ')'
                )
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS precos ('
                    'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    'dia VARCHAR(30) NOT NULL,'
                    'preco VARCHAR(30) NOT NULL,'
                    'moeda INT NOT NULL,'
                    'FOREIGN KEY (moeda) REFERENCES moedas(id)'
                ')'
                )
            
            for cripto in self.criptos:
                insert_ignore = 'INSERT IGNORE INTO moedas (nome) VALUES (%s)'

                cursor.execute(insert_ignore, (cripto))
                    
            print("Colocando dados na tabela")
            sql = 'INSERT INTO precos (dia, preco, moeda) SELECT  %s, %s, id  FROM moedas WHERE moedas.nome = %s'
            for tupla in lista_tuplas:
                
                cursor.execute(sql, (dia, tupla[1], tupla[0]))
              

        self.conexao.commit()

    def imprime_valores(self):

        '''
        Essa função, por enquanto, imprime todos os valores
        da tabela da database. Seria ideal passar o parametro
        que quero procurar
        '''

        with self.conexao.cursor() as cursor:
            sql = 'SELECT dia, preco, moedas.nome FROM precos, moedas WHERE precos.moeda = moedas.id'
            cursor.execute(sql)
            resultado = cursor.fetchall()

        return resultado

    def fechar(self):
        self.conexao.close()


