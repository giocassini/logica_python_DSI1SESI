# AULA COMPLETA - STRINGS EM PYTHON

# - Criação de strings
# - Strings multilinha
# - Índices e slices
# - Operações com strings 
# - Imutabilidade 
# - Métodos úteis
# - Formação de texto
# - Unicode e bytes

#--------------------------
# 1) CRIAÇÃO DE STRINGS
#--------------------------
# Stringd são textos em python.
# Podem ser criadas usando aspas simples ou duplas 

texto1 = "Python"
texto2 = 'Curso de Python'
texto3 = "Copa 'padrão fifa' "
texto4 = 'Copa "padrão fifa"' 

print(texto1, texto2, texto3, texto4)

# Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

#-------------------------------------
# 2) STRINGS MULTILINHA
#-------------------------------------
# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.

menu = """\ 
Uso: programa [OPÇÕES]
-h Exibe ajuda
-u Url do dataset
"""
print(menu)

# Esse formato é muito importante
# - Menus
# - Documentação
# - textos longos

#---------------------------
# 3) concatenação automática
#---------------------------
# Quando duas strings aparece lado a lado, o Python junta automáticamente

texto = ("Copa" "2026" " Neymar é showm mesmo?" "Talvez")
print(texto)

#----------------------------
# 4) STRINGS COMO SEQUÊNCIAS
#----------------------------
# Uma string funciona como uma sequência de caracteres, cada caractere possui um Índice

st = "maracana"
print("Primeira letra", st[0])
# só exibir a letra: m

print ("ultima letra:", st[-1])
# colocar a numeração da ultima letra

print ("Trecho1:4:", st[1:4])

print (" Do ínicio até 3:", st[:3])

print ("Do 2 até o fim", st[2:])

print ("Tamanho", len(st))


