import unittest

from troco import *

class TesteTroco(unittest.TestCase):
    def setUp(self):
        self.arr_tests = []
        self.var_tests = [63,33,44,116,10]
        self.arr_tests.append([1,5,10,21,25])
        self.arr_tests.append([2,5,10,20,50,100,200])

    def teste_quantidade_moedas(self):
        memoria_contagem = []
        memoria_moedas = []
        valor_esperado = [3,4,4,6,1]

        for i,valor in enumerate(self.var_tests):
            memoria_contagem = [0]*(valor+1)
            memoria_moedas= [0]*(valor+1)
            self.assertEqual(valor_esperado[i],calculaTroco(self.arr_tests[0],self.var_tests[i],memoria_contagem,memoria_moedas),msg=f"A quantidade de moedas para um troco de {self.var_tests[i]} está incorreto!")
    
    def teste_moedas_resultantes(self):
        memoria_contagem = []
        memoria_moedas = []
        listas_esperadas = [[21,21,21], [1,1,10,21], [1,1,21,21], [10,10,21,25,25,25], [10]]

        for i,valor in enumerate(self.var_tests):
            memoria_contagem = [0]*(valor+1)
            memoria_moedas= [0]*(valor+1)
            calculaTroco(self.arr_tests[0],self.var_tests[i],memoria_contagem,memoria_moedas)
            self.assertEqual(listas_esperadas[i],moedasResultantes(memoria_moedas,self.var_tests[i]))
        
    def teste_aplicacao_salario_minimo_2020(self):
        memoria_contagem = [0]*1040
        memoria_moedas= [0]*1040
        self.assertEqual(10,calculaTroco(self.arr_tests[1],1039,memoria_contagem,memoria_moedas),msg=f"A quantidade de notas para um troco de R$1039 está incorreto!")


            
if __name__ == "__main__":
    unittest.main()
