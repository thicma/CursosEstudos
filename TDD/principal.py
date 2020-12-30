from dominio import Usuario, Lance, Leilao, Avaliador

thiago = Usuario('Thiago')
thicma = Usuario('Thicma')
juliana = Usuario('Juliana')

lance_do_Thiago = Lance(thiago, 100)
lance_do_thicma = Lance(thicma, 150)
lance_da_Juliana = Lance(juliana, 300)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_Thiago)
leilao.lances.append(lance_do_thicma)
leilao.lances.append(lance_da_Juliana)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O Menor lance foi de {avaliador.menor_lance}\nO Maior lance foi de {avaliador.maior_lance}')