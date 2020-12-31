from dominio import Usuario, Leilao, Lance
import pytest

@pytest.fixture
def vini():
    return Usuario('Vini', 100)

@pytest.fixture
def leilao():
    return Leilao('Celular')

#usuário só pode dar lance até o valor máximo de sua carteira
def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propor_uma_lance(vini,leilao):
    vini.propoe_lance(leilao, 50)
    assert vini.carteira == 50

def test_deve_aceitar_lance_ate_o_limite_da_carteira(vini,leilao):
    vini.propoe_lance(leilao, 1)
    assert vini.carteira == 99

def test_deve_aceitar_lance_ate_o_valor_igual_ao_da_carteira(vini,leilao):
    vini.propoe_lance(leilao, 100)
    assert vini.carteira == 0

def test_nao_deve_aceitar_lance_maior_que_o_da_carteira(vini,leilao):
    with pytest.raises(ValueError):
        vini.propoe_lance(leilao, 200)
