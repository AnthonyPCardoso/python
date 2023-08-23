def sistema(colocacao = []):
    if max(colocacao) == colocacao[0] and min(colocacao) == colocacao[1]:
        print(f'''
            Primeiro colocado é {max(colocacao)}
            Segundo colocado é {colocacao[2]}
            Terceiro colocado é {min(colocacao)}
    ''') 
    elif max(colocacao) == colocacao[2] and min(colocacao) == colocacao[0]:
        print(f'''
            Primeiro colocado é {max(colocacao)}
            Segundo colocado é {colocacao[1]}
            Terceiro colocado é {min(colocacao)}
    ''') 

    else:
        print(f'''
            Primeiro colocado é {max(colocacao)}
            Segundo colocado é {colocacao[0]}
            Terceiro colocado é {min(colocacao)}
    ''') 

posicionamento = []
for i in range(3):
    player = int(input("Qual a pontuação? "))
    posicionamento.append(player)

sistema(posicionamento)