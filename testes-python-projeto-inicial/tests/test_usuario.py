from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.execoes import LanceInvalido


@pytest.fixture
def brenda():
    return Usuario('Brenda', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propor_lance(brenda, leilao):
    brenda.propoe_lance(leilao, 50.0)

    assert brenda.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(brenda, leilao):
    brenda.propoe_lance(leilao, 1.0)

    assert brenda.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_o_valor_da_carteira(brenda, leilao):
    brenda.propoe_lance(leilao, 100.0)

    assert brenda.carteira == 0.0

def test_nao_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_valor_da_carteira(brenda, leilao):
    with pytest.raises(LanceInvalido):
        brenda.propoe_lance(leilao, 150.0)
