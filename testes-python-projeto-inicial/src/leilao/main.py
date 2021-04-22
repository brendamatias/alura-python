from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


brenda = Usuario('Brenda')
joao = Usuario('João')

lance_brenda = Lance(brenda, 100.0)
lance_joao = Lance(joao, 50.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_brenda)
leilao.lances.append(lance_joao)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')