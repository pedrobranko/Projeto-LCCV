def keyrsa():
        from math import gcd #Função que calcula o MMC
        import random #Função que gera um número aleatório

      
        p = 17 #Definicao dos dois numeros primos (p e q) que darao base aos calculos
        q = 41
        n = p*q
        toti = (p - 1)*(q - 1) #Função totiente que usaremos para encontrar a chave

        keyp = [] #Lista com as possíveis chaves publicas
        auxe = []
        for i in range(toti+1): 
                if gcd(toti,i) == 1: 
                        keyp.append(i)
        a = keyp[random.randrange(len(keyp))]
        d=0
        while (d*a)%toti !=1 :
                d=d+1
        return (n,a,d)

(a,b,c) = keyrsa()
print (a,b,c)

    
        
