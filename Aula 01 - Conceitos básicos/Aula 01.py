# Exemplo 01 - lista de nomes

nomes = ["Marcelo", "Lucas", "Angela", "Sabrina", "Marcelo", "Lucas", "Marcio"]

# Funcao input: Guarda o que o usuario digitou em uma variavel
nome = input("Digite o nome a ser contado: ")
 
# Utlizando o método count na lista de strings
# Método count: retorna o numero de ocorrencias de um valor em uma lista 
contagem = nomes.count(nome)

# Mostrando o resultado de ocorrencias do valor digitado
print("O número de ocorrencias referentes ao nome " + nome + " na lista é igual há:", contagem)
