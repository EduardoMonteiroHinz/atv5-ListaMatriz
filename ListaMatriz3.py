import random

linha = int(input("Número de linhas: "))
coluna = int(input("Número de colunas: "))

def matrizes(linha,coluna):
    matriz=[]
    for i in range(linha):
        linhas=[]
        for j in range(coluna):
            elementos=random.randint(1, 20)
            linhas.append(elementos)
        matriz.append(linhas)
    return matriz

m=matrizes(linha,coluna)

def MatrizesPrint(matriz):
    for linha in matriz:
        print(linha)

MatrizesPrint(m)

def MatrizPar(linha,coluna,matriz):
    p = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] % 2 == 0:
                p += matriz[i][j]
    return print(f"A soma dos numeros pares dentro da matriz é: {p}")

MatrizPar(linha,coluna,m)

def SomaColuna(matriz, coluna):
    if coluna < 0 or coluna >= len(matriz[0]):
        return f"A coluna {coluna} não existe na matriz."
    
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][coluna]
    
    return f"A soma dos elementos da coluna {coluna} é: {soma}"

coluna = int(input("coluna a ser somada: "))
print(SomaColuna(m, coluna))

def MaiorValorLinha(matriz, linha):

    if linha < 0 or linha >= len(matriz):
        return f"A linha {linha} não existe na matriz."
    
    MaiorValor = matriz[linha][0]
    for valor in matriz[linha]:
            if valor > MaiorValor:
                MaiorValor = valor
    return f"O maior valor da linha {linha} é: {MaiorValor}"

linha = int(input("Escolha uma linha para encontrar o maior valor: "))
print(MaiorValorLinha(m, linha))

def GerarMatrizEspecifica():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            if i < j:
                valor = 2 * i + 7 * j + 2
            elif i == j:
                valor = 3 * i ** 2 + 1
            else:
                valor = 4 * i ** 3 + 5 * j ** 2 + 1
            linha.append(valor)
        matriz.append(linha)
    return matriz

print("Matriz:")
matrizEspecifica = GerarMatrizEspecifica()
MatrizesPrint(matrizEspecifica)

def cadastrar_pessoas():
    pessoas = []
    
    while True:
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = int(input("Idade: "))
        renda_mensal = float(input("Renda Mensal: "))
        
        pessoa = [nome, cpf, idade, renda_mensal]
        pessoas.append(pessoa)
        
        continuar = input("Deseja cadastrar mais uma pessoa? (s/n): ")
        if continuar == "s":
            continue
        elif continuar == "n":
            break
    return pessoas

def ImprimirPessoas(pessoas):
    for usuario in pessoas:
        print(f"Nome: {usuario[0]}, CPF: {usuario[1]}, Idade: {usuario[2]}, Renda mensal: {usuario[3]}")
    
def calcular_medias(pessoas):
    total_idade = 0
    total_renda = 0.0
    
    for usuario in pessoas:
        total_idade += usuario[2]
        total_renda += usuario[3]
    
    mediaIdade = total_idade / len(pessoas)
    media_renda = total_renda / len(pessoas)
    
    return media_idade, media_renda

pessoas = cadastrar_pessoas()
print("\nPessoas cadastradas:")
ImprimirPessoas(pessoas)

media_idade, media_renda = calcular_medias(pessoas)
print(f"\nMédia de Idade: {media_idade:.2f}")
print(f"Média de Renda Mensal: {media_renda:.2f}")