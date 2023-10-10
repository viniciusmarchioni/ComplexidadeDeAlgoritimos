#count sort
vetor = [2,5,0,1,2,3,10]
vetor_aux = []
valor = len(vetor)
maior = max(vetor)
menor = min(vetor)

for i in range(maior+1):
    vetor_aux.append(0)

for i in vetor:
    vetor_aux[i]+=1

vetor=vetor_aux
vetor_aux=[]
for i in range(len(vetor)):
    for j in range(vetor[i]):
        vetor_aux.append(i)


print(vetor_aux)
