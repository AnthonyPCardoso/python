class Registroestudante:
    def __init__(self):
        self.registrar = {}

    def adicionar_estudante(self, nome, estudante_id):
        if estudante_id not in self.registrar:
            self.registrar[estudante_id] = nome
            print(f"Aluno {nome} com o  ID {estudante_id} adicionado.")
        else:
            print(f"Aluno com o ID {estudante_id} Já existe.")

    def remove_estudante(self, estudante_id):
        if estudante_id in self.registrar:
            nome = self.registrar.pop(estudante_id)
            print(f"Estudante {nome} com o ID {estudante_id} removido.")
        else:
            print(f"Estudante com o ID {estudante_id} não existe.")

    def ver_estudante(self):
        print("Registro dos estudantes:")
        for estudante_id, nome in self.registrar.items():
            print(f"ID: {estudante_id}, Nome: {nome}")

def main():
    registrar = Registroestudante()

    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Ver alunos")
        print("4. Sair")
        choice = input("Digite o número de sua escolha: ")

        if choice == "1":
            nome = input("Nome do aluno: ")
            estudante_id = input("ID do aluno: ")
            registrar.adicionar_estudante(nome, estudante_id)
        elif choice == "2":
            estudante_id = input("ID do aluno para remover: ")
            registrar.remove_estudante(estudante_id)
        elif choice == "3":
            registrar.ver_estudante()
        elif choice == "4":
            print("Fim o programa.")
            break
        else:
            print("Escolha inválida. Por favor escolha uma opção existente.")


main()