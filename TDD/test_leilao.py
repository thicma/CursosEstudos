from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
#setUp invoca semrpe que tiver um teste, este cenário.
    def setUp(self):
        self.thiago = Usuario('Thiago')
        self.thicma = Usuario('Thicma')
        self.juliana = Usuario('Juliana')

        self.lance_do_Thiago = Lance(self.thiago, 100)
        self.lance_do_thicma = Lance(self.thicma, 150)
        self.lance_da_Juliana = Lance(self.juliana, 300)

        self.leilao = Leilao('Celular')

    def test_deve_retornar_maior_e_menor_quando_adicionado_em_ordem_crescente(self):
        self.leilao.propoe_lance(self.lance_da_Juliana)
        self.leilao.propoe_lance(self.lance_do_thicma)
        self.leilao.propoe_lance(self.lance_do_Thiago)
        menor_valor_esperado = 100
        maior_valor_esperado = 300
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_deve_retornar_maior_e_menor_quando_adicionado_em_ordem_decrescente(self):
        self.leilao.propoe_lance(self.lance_da_Juliana)
        self.leilao.propoe_lance(self.lance_do_thicma)
        self.leilao.propoe_lance(self.lance_do_Thiago)

        menor_valor_esperado = 100
        maior_valor_esperado = 300
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_leilao_com_um_lance(self):
        self.leilao.propoe_lance(self.lance_do_Thiago)
        menor_valor_esperado = 100
        maior_valor_esperado = 100
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    #se o leilao não tiver lances, deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe_lance(self.lance_do_Thiago)
        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebidos)

    #se o ultimo usuario for diferente, deve permitir propo o lance
    def test_deve_pemitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe_lance(self.lance_do_Thiago)
        self.leilao.propoe_lance(self.lance_da_Juliana)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        
        self.assertEqual(2, quantidade_de_lances_recebidos)

    #se o ultimo usuario for o mesmo, não deve permitir propor lance
    def test_nao_deve_pemitir_propor_um_lance_caso_o_ultimo_usuario_seja_o_mesmo(self):
        novo_lance_Thiago = Lance(self.thiago, 50)
        with self.assertRaises(ValueError):
            self.leilao.propoe_lance(self.lance_do_Thiago)
            self.leilao.propoe_lance(novo_lance_Thiago)
    
    def test_deve_permitir_propor_novo_lance_apenas_maior_que_o_anterior(self):
        novo_lance_Thiago = Lance(self.thiago, 150)
        with self.assertRaises(ValueError):
            self.leilao.propoe_lance(self.lance_do_Thiago)
            self.leilao.propoe_lance(self.lance_da_Juliana)
            self.leilao.propoe_lance(novo_lance_Thiago)

    def test_não_deve_permitir_propor_novo_lance_apenas_maior_que_o_anterior(self):
        novo_lance_Thiago = Lance(self.thiago, 50)
        with self.assertRaises(ValueError):
            self.leilao.propoe_lance(self.lance_do_Thiago)
            self.leilao.propoe_lance(self.lance_da_Juliana)
            self.leilao.propoe_lance(novo_lance_Thiago)
        

            
            

        