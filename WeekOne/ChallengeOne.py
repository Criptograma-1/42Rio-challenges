class user:
    def __init__(self, name, age, discord):
        self.__name = name
        self.__age = age
        self.__discord = discord

        texto = self.__name + ' ' + str(self.__age) + ' ' + self.__discord
        try:
            arquivo = open('usuarios.txt', 'r')
        except FileNotFoundError:
            arquivo = open('usuarios.txt', 'w')
            arquivo.writelines(texto)
        conteudo = arquivo.readlines()
        conteudo.append("\n" + texto)
        arquivo = open('usuarios.txt', 'w')  
        arquivo.writelines(conteudo)
        arquivo.close()

    def my_print(self):
        print('Seu nome é', self.__name, ', você tem', self.__age,'anos de idade, and seu usuário do discord é ', self.__discord)
    
    def print_users(self):
        arquivo = open("usuarios.txt","r")
        linha = arquivo.readline()
        while linha:
            valores = linha.split()
            print('nome:', valores[0], ' idade:', valores[1], ' discord:', valores[2] )
            linha = arquivo.readline()
        arquivo.close()

name = input('Por favor digite o seu nome: ')
age = input('Por favor digite o sua idade: ')
discord = input('Por favor digite o seu usuário no discord: ')
my_user = user(name, age, discord)
my_user.my_print()
decision = input('Quer exibir todos os usuários cadastrados (s/n):')
if decision == 's':
    my_user.print_users()