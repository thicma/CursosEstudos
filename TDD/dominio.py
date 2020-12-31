import sys
from copy import deepcopy

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome
    
    @property
    def carteira(self):
        return self.__carteira
    
    def propoe_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise ValueError('Não pode propor lance maior que o da carteira!')
        lance = Lance(self, valor)
        leilao.propoe_lance(lance)
        self.__carteira -= valor
        


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe_lance(self, lance: Lance):
        # if len(self.__lances) == 0 or self.__lances[-1].usuario != lance.usuario:  
        if not self.__lances or self.__lances[-1].usuario != lance.usuario:  
            if lance.valor > self.maior_lance:
                self.maior_lance =  lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            self.__lances.append(lance)
        elif lance.usuario in self.__lances:
            # if self.__lances[-1].valor < lance.valor:
            raise ValueError('O valor do lance do usuário deve ser maior que o lance anterior.')
            # else:
            #     self.__lances.append(lance)
        else:
            raise ValueError('O mesmo usuário não pode propor dois lances seguidos!')

    
    
    @property
    def lances(self):
        return deepcopy(self.__lances)#devolve uma cópia profunda da lista de lances


        
    
