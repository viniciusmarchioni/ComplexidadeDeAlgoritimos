vetor = [2,5,0,1,2,3,10]
vetor_aux = []
valor = len(vetor)
maior = max(vetor)
menor = min(vetor)

for i in range(maior+1):
    vetor_aux.append(0)

for i in vetor:
    vetor_aux[i]+=1

pos = 0

for i in range(len(vetor_aux)):
    for j in range(vetor_aux[i]):
        vetor[pos] = i
        pos += 1


print(vetor)