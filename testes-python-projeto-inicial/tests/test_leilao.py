# -*- coding: utf-8 -*-
from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.execoes import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self):
        self.brenda = Usuario('Brenda', 500.0)
        self.lance_brenda = Lance(self.brenda, 100.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_menor_lance_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        joao = Usuario('João', 500.0)
        lance_joao = Lance(joao, 150.0)

        self.leilao.propoe(self.lance_brenda)
        self.leilao.propoe(lance_joao)

        self.assertEqual(100, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_lance_em_ordem_descrecente(self):
        with self.assertRaises(LanceInvalido):
            joao = Usuario('João', 500.0)
            lance_joao = Lance(joao, 150.0)

            self.leilao.propoe(lance_joao)
            self.leilao.propoe(self.lance_brenda)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_brenda)

        self.assertEqual(100, self.leilao.menor_lance)
        self.assertEqual(100, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_menor_lance_quando_leilao_tiver_tres_lance(self):
        vini = Usuario('Vini', 500.0)
        joao = Usuario('João', 500.0)
        lance_joao = Lance(joao, 150.0)
        lance_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_brenda)
        self.leilao.propoe(lance_joao)
        self.leilao.propoe(lance_vini)

        self.assertEqual(100, self.leilao.menor_lance)
        self.assertEqual(200, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_brenda)
        quantidade_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lances)

    def test_deve_permitir_propor_lance_caso_ultimo_usuario_seja_diferente(self):
        joao = Usuario('João', 500.0)
        lance_joao = Lance(joao, 200.0)

        self.leilao.propoe(self.lance_brenda)
        self.leilao.propoe(lance_joao)

        quantidade_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances)

    def test_nao_deve_permitir_propor_lance_caso_ultimo_usuario_seja_o_mesmo(self):
        lance_brenda500 = Lance(self.brenda, 500.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_brenda)
            self.leilao.propoe(lance_brenda500)
