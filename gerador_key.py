def lista_primos(n): #Função que retorna uma lista com os numeros primos de 2 a N
    numeros = []
    primos = []    
    for i in range(0,n): #Cria uma lista com todos os numeros de 2 a N
        numeros.append(i)
    for i in range(2,len(numeros)):
            
#Este trecho divide o número atual pelos anteriores
#e para se encontrar um múltiplo-------------------
            
        count = 2
        while count != i: 
            if i%count == 0:
                break
            else:
                count += 1
                
#Fim do trecho ------------------------------------

        if count == i: #Se após o while anterior não encontrar um múltiplo, o número é ímpar
            primos.append(i)
    return primos 

def keyrsa(primos): #Função que vai gerar as chaves publicas e privadas

        from math import gcd #Função que calcula o MDC
        import random #Função que gera um número aleatório      

        p = 10
        q = 10
        
        while gcd(p,q) != 1: #Escolhe dois números primos na lista da função lista_primos
                p = primos[random.randrange(len(primos))]
                q = primos[random.randrange(len(primos))]
                
        n = p*q
        toti = (p - 1)*(q - 1) #Função totiente que usaremos para encontrar a chave
        keyp = [] #Lista com as possíveis chaves publicas        
        for i in range(toti+1): 
                if gcd(toti,i) == 1: 
                        keyp.append(i)
        a = keyp[random.randrange(len(keyp))]
        d = 0
        while (d*a)%toti !=1 : #Encontra o valor da chave privada
                d=d+1
        return (n,a,d)

primos = lista_primos(100)
(a,b,c) = keyrsa(primos)
print (a,b,c)

    
        
