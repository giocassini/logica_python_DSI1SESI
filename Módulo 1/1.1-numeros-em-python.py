# AULA COMPLETA: NUMEROS EM PYTHON

"""
Vamos aprender:
1 - Tipos numéricos
2 - Conversões de tipos
3 - Hierarquia numérica
4 - Operações matemáticas
5 - Coerção de tipos 
6 - verificação fe tipos 
7 - Entrada de dados 
"""
#===========================
# PASSO 1 - Tipos numéricos 
#===========================
# int -> números inteiros 
# float -> números com casas decimais
# complex -> números complexos (usado em matemática/engenharia)

print("===== TIPOS DE NÚMERICOS =====") 

# exemplo 01 - numero inteiro

#criamos uma variavel chamada numero_inteiro
numero_inteiro = 10

#mostrando o valor
print ("Valor:", numero_inteiro)

#Type() mostra qual é o tipo da variável
print("Tipo", type(numero_inteiro))

print ("--------------------------------")

# exemplo 02 - numero decimal 

# float é um numero com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("tipo:", type(numero_decimal))

print("------------------------------")

# exemplo 03 - numeros complexos
# um numero complexo possui duas partes:
#parte real (numero normal)
#parte imaginaria (multiplicada por j)

#estrutura geral: 
# numero = a + bj

# a = parte real
# b = parte imaginaria
# j = unidade imaginaria

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo", type(numero_complexo))
