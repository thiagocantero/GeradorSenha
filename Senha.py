#Gerador de Senhas em Python
#Versão: 0.1
#Autor: Thiago Cantero Mari Monteiro
#thiagocantero.com.br/sobre


#Importa biblioteca Random (esta com o objetivo de fazer a função aleatória dos anagramas)
import random

#Inicializa as variáveis para compor a senha
minuscula = "abcdefghijklmnopqrstuvwxyz"
maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "<>#[]{}()*;/,_-!"

#concatena as variáveis para formar a senha
tudo = minuscula+maiuscula+numeros+simbolos
#define o tamanho da senha
tamanho = 12
#transforma em anagrama, utilizando todas as variáveis, especificada pelo tamanho, e cria de maneira aleatória
senha = "".join(random.sample (tudo, tamanho))
#imprime na tela a sua senha
print (senha)