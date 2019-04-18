from RSA import (keyrsa,lista_primos,encrypt,decrypt) #Funções de criptografia e descriptografia

log = open('log.txt','r') #Faz a leitura do arquivo
content = log.readlines() 
try: #Verifica se o arquivo possui uma chave válida
    chaves = content[0].split(',')
    chaves = [int(chaves[i]) for i in range(len(chaves))]    
except: #Caso não possua, cria uma chave
    print('Nenhuma chave válida foi encontrada, deseja incerir uma nova? [s/n]: ')
    switch = input()
    while (switch.upper() != 'S') and (switch.upper() != 'N'): #Verifica se a resposta é válida
        print('Resposta inválida')
        switch = input()        
    while True: #Faz a enttrada da chave e testa se é válida
        if switch.upper() == 'S':
            chave = input('Entre com chaves válidas no seguinte formato "N, Chave Pública, Chave Privada": ')
            try:
                chave = chave.split(',')
                chave = (int(chave[0]),int(chave[1]),int(chave[2]))            
                while decrypt(encrypt('a',chave),chave) != 'a': #Testa validade da chave
                    print('Chave inválida')
                    chave = input('Entre com chaves válidas no seguinte formato "N, Chave Pública, Chave Privada": ')                
            except:
                print('Formato de chave inválido')
        elif switch.upper() == 'N': #Caso não seja inserida uma chave, o programa cria uma
            chave = keyrsa(lista_primos(200))
            print('A chave',chave,'foi gerada com sucesso!')
        log = open('log.txt','r')
        conteudo = log.readlines()
        log = open('log.txt','w')
        conteudo.insert(0,str(chave[0])+','+str(chave[1])+','+str(chave[0])+'\n') 
        log.writelines(conteudo)
        log.close()
        break
    


    
    
