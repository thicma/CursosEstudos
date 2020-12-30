from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_deve_retornar_maior_e_menor_quando_adicionado_em_ordem_crescente(self):
        thiago = Usuario('Thiago')
        thicma = Usuario('Thicma')
        juliana = Usuario('Juliana')

        lance_do_Thiago = Lance(thiago, 100)
        lance_do_thicma = Lance(thicma, 150)
        lance_da_Juliana = Lance(juliana, 300)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_da_Juliana)
        leilao.lances.append(lance_do_thicma)
        leilao.lances.append(lance_do_Thiago)

        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100
        maior_valor_esperado = 300
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def test_deve_retornar_maior_e_menor_quando_adicionado_em_ordem_decrescente(self):
        thiago = Usuario('Thiago')
        thicma = Usuario('Thicma')
        juliana = Usuario('Juliana')

        lance_da_Juliana = Lance(juliana, 300)
        lance_do_thicma = Lance(thicma, 150)
        lance_do_Thiago = Lance(thiago, 100)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_da_Juliana)
        leilao.lances.append(lance_do_thicma)
        leilao.lances.append(lance_do_Thiago)

        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100
        maior_valor_esperado = 300
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_leilao_com_um_lance(self):
        thiago = Usuario('Thiago')

        lance_do_Thiago = Lance(thiago, 100)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_Thiago)

        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100
        maior_valor_esperado = 100
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)