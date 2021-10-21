# Exemplo 01 - lista de nomes

# Declarando lista de strings
lista_de_nomes = ["Marcelo", "Lucas", "Angela", "Sabrina", "Marcelo", "Lucas", "Marcio"]

# Funcao input: Guarda o que o usuario digitou em uma variavel
nome_input = input("Digite o nome a ser contado: ")
 
# Utlizando o método count na lista de strings
# Método count: retorna o numero de ocorrencias de um valor em uma lista 
contagem_nomes = lista_de_nomes.count(nome_input)

# Mostrando o resultado de ocorrencias do valor digitado
print("O número de ocorrencias referentes ao nome " + nome_input + " na lista é igual há:", contagem_nomes)
