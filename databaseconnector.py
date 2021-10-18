import pymysql.cursors
from datetime import datetime


class ConexaoSQL:
    def __init__(self):
        self.conexao = self.conecta()
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

    def acrescentaValores(self, moedas:list, precos:list):
        '''
        Pega os valores e os coloca na Base de Dados
        '''

        lista_tuplas = []
        for i in range(10):
            lista_tuplas.append((moedas[i], precos[i]))
 
        dia = datetime.now()
        dia = dia.strftime("%d/%m")
        with self.conexao.cursor() as cursor:
            print("Colocando dados na tabela")
            sql = 'INSERT INTO precos (dia, preco, moeda) SELECT  %s, %s, id  FROM moedas WHERE moedas.nome = %s'
            for tupla in lista_tuplas:
                
                cursor.execute(sql, (dia, tupla[1], tupla[0]))
              

        self.conexao.commit()

    def imprimeValores(self):

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


