numeros  =    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#nomes   =    ['Leonardo','Pedro','jujuba','fake nathy']
#ano     =    ['2002','2024']



#print(f'Numeros :{numeros}')
#print(f'Nomes :{nomes}')
#print(f'Anos :{ano}')

#for numeros in numeros :
    #print(f'Numero : {numeros}')
#for nomes in nomes:
    #print(f'Nomes : {nomes}')    
#for ano in ano:
    #print(f'Ano : {ano}')

# n2 = 0 
#for numero in numeros :
    #if  numero %2 !=0:
        #n2 += numero  
        #print(f'{n2}')


#for i in range(len(numeros)):
    #for j in range(0,len(numeros)-i-1):
        #if numeros[j] < numeros[j + 1]:
            #numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
#print(numeros)


number = int(input('Digite um numero: '))
resultado = 0

print(f'Tabuada do {number}')
for numero in numeros:
    resultado = numero * number
    print(resultado)