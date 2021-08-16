qt = int(input('Quantas conjuntos você deseja inserir: '))
result = []

for x in range(qt):
  n = list(map(int, (input('Digite 3 números números: ').split())))
  n.sort()
  result.append(n[0])
print(result)