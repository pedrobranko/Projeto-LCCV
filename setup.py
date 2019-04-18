from gerador_key import (keyrsa,lista_primos) #Funções de criptografia e descriptografia

string_enter = 'mafagafo'
string_list = [ord(a) for a in string_enter]
chaves = keyrsa(lista_primos(200))
string_crypt = [string_list[a]**chaves[1]%chaves[0] for a in range(len(string_list))]
string_decrypt = [string_crypt[a]**chaves[2]%chaves[0] for a in range(len(string_list))]
string_decrypt = [chr(a) for a in string_decrypt]
print(chaves)



