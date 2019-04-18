from RSA import (keyrsa,lista_primos,encrypt,decrypt) #Funções de criptografia e descriptografia

log = open('log.txt','r')
content = log.readlines()
try:
    chaves = content[0].split(',')
    chaves = [int(chaves[i]) for i in range(len(chaves))]    
except:
    print('Nenhuma chave válida foi encontrada, deseja incerir uma nova? [s/n]: ')
    switch = input()
    while switch.upper() != 'S' and 'N':
        print('Resposta inválida')
        switch = input()        
    while True:
        if switch.upper() == 'S':
            chave = input('Entre com chaves válidas no seguinte formato "N, Chave Pública, Chave Privada": ')
            try:
                chave = chave.split(',')
                chave = (int(chave[0]),int(chave[1]),int(chave[2]))            
                while decrypt(encrypt('a',chave),chave) != 'a':
                    print('Chave inválida')
                    chave = input('Entre com chaves válidas no seguinte formato "N, Chave Pública, Chave Privada": ')
                
            except:
                print('Formato de chave inválido asdasd')

        log = open('log.txt','w')
        log.writelines(str(chave[0])+','+str(chave[1])+','+str(chave[0]))
        log.close()
        break
    


    
    
