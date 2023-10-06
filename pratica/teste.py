# def somar(a, b):

#     return a + b



# resultado = somar(3, 4) + somar(5, 2)
# print(resultado)

# palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'papagaio']


# resultado = list(filter(lambda x: len(x) > 5, palavras))

# numeros = [1, 2, 3, 4, 5]

# resultado = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numeros))


# palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre','papagaio']

# resultado = list(filter(lambda x: len(x) > 5, palavras))
# print(resultado)

def minha_funcao(*args, **kwargs):

    for arg in args:

        print(arg)

    for key, value in kwargs.items():

        print(key, value)



minha_funcao (1,2,3,nome="Alice", idade=25)