
def calcular_media(notas):
    soma = sum(notas)
    return soma / len(notas)


def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    notas = []
    while True:
        nota_str = input("Digite uma nota (ou 'q' para sair): ")
        if nota_str.lower() == 'q':
            break
        try:
            nota = float(nota_str)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Por favor, digite uma nota válida.")

    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    
    print(f"Média do aluno: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()
