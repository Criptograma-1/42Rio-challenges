#qt = int(input('Quantos números você deseja somar: '))
n = input('Digite os números: ').split()
result = 0
'''while len(n) != qt:
  print("Você digitou a quantidade errada de números")
  n = input("Digite " + str(qt) + " números: ").split()
else:'''
for x in range(len(n)):
  result = result + int(n[x])
print(result)