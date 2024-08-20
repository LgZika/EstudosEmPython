# Classe Livro
class Livro():
    def __init__(self, id, titulo, autor, isbn, disponibilidade):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponibilidade = disponibilidade

    def __str__(self):
        return f'ID: {self._id}\nTitulo: {self._titulo}\nAutor: {self._autor}\nISBN: {self._isbn}\nDisponibilidade: {self._disponibilidade}\n'
       
    def set_disponibilidade(self, disponivel):
        self._disponibilidade = disponivel

    def get_livro(self):
        return self._id, self._titulo, self._isbn, self._disponibilidade

    def set_livro(self):
        pass

# Classe Autor
class Autor:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    def __str__(self):
        return f'Nome: {self._nome}\nNacionalidade: {self._nacionalidade}'

    def get_autor(self):
        return self._nome, self._nacionalidade

    def set_autor(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

# Classe Usuario
class Usuario():
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
        self._livros_emprestados = []

    def __str__(self):
        return f'\nID: {self._id}\nNome: {self._nome}\nLivros Emprestados: {self._livros_emprestados}'
    
    def set_emprestimos(self, id_livro):
        self._livros_emprestados.append(id_livro)

# Função para adicionar novo livro à biblioteca
def adicionar_livro(livros):
    print("\nAdicionar Livro")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    id = len(livros)
    livros.append(Livro(id, titulo, autor, isbn, True))            

# Função para listar os livros contidos na biblioteca e filtra-los
def listar_livros(livros):
    while True:
        print("\nListar Livros:")
        print("(1) Todos")
        print("(2) Disoniveis")
        print("(3) Emprestados")
        print("(0) Cancelar")
        escolha = int(input("Opcao escolhida: "))  

        if escolha == 1:
            for livro in livros:
                print(livro)
            break
        elif escolha == 2:
            for livro in livros:
                if livro._disponibilidade == True:
                    print(livro)
            break
        elif escolha == 3:
            for livro in livros:
                if livro._disponibilidade == False:
                    print(livro)
            break
        elif escolha == 0:
            break
        else:
            print("Opcao invalida")

#Função para buscar por algum livro, baseado em seu ID ou titulo
def buscar_livro(livros):
    while True:
        print("\nBuscar Livro por:")
        print("(1) ID")
        print("(2) Titulo")
        print("(0) Cancelar")
        escolha = int(input("Opcao escolhida: ")) 

        if escolha == 1:
            id = int(input("\nInsira o ID do livro: "))
            if id >= 0 and id <= len(livros):
                print(f'\nID: {livros[id]._id}\nTitulo: {livros[id]._titulo}\nAutor: {livros[id]._autor}\nISBN: {livros[id]._isbn}\nDisponibilidade: {livros[id]._disponibilidade}\n')
            else:
                print("\nID Nao Encontrado\n")
            break
        elif escolha == 2:
            titulo = input("Insira o Titulo do livro: ")
            for livro in livros:
                if livro._titulo == titulo:
                    print(f'ID: {livros[livro]._id}\nTitulo: {livros[livro]._titulo}\nAutor: {livros[livro]._autor}\nISBN: {livros[livro]._isbn}\nDisponibilidade: {livros[livro]._disponibilidade}\n')
                    break                
            print("\nTitulo Nao Encontrado\n")
        elif escolha == 0:
            break
        else:
            print("Opcao invalida")

# Função para remover algum livro já adicionado
def remover_livro(livros):
    print("\nRemover Livro")
    id = int(input("Insira o ID do livro: "))
    if id >= 0 and id <= len(livros):
        livros.pop(id)
        print("\nRemovido com Sucesso")
    else:
        print("\nID Inválido\n")

# Função para emprestar livros presentes na biblioteca para um usuario
def emprestar_livro(livros, usuarios):
    print("Emprestar Livro:")
    id_livro = int(input("ID do livro a ser emprestado: "))
    id_usuario = int(input("ID do usuario solicitante: "))

    if id_livro >= 0 and id_livro <= len(livros):
        if id_usuario >= 0 and id_usuario <= len(usuarios):
            while True:
                print(f'Emprestar o Livro {livros[id_livro]._titulo} para {usuarios[id_usuario]._nome}?')
                print("(1) Sim")
                print("(2) Nao")
                escolha = int(input("Opcao escolhida: "))
                if escolha == 1:
                    livros[id_livro].set_disponibilidade(False)
                    usuarios[id_usuario].set_emprestimos(id_livro)
                    print("\nLivro Emprestado com Sucesso")
                    break
                elif escolha == 2:
                    print("Operacao Cancelada")
                    break
                else:
                    print("Opcao Invalida")
        else:
            print("Usuario Nao Encontrado")
    else:
        print("Livro Nao Encontrado")

def devolver_livro(livros, usuarios):
    id_usuario = int(input("ID do usuario a efetuar devolucao: "))
    print("\nLivros Emprestados para este Usuario: ")
    for x in usuarios[id_usuario]._livros_emprestados:
        for livro in livros:
            if usuarios[id_usuario]._livros_emprestados[x] == livro._id:
                print(f'ID: {livros[livro]._id}\nTitulo: {livros[livro]._titulo}\nAutor: {livros[livro]._autor}\nISBN: {livros[livro]._isbn}\nDisponibilidade: {livros[livro]._disponibilidade}\n')

def adicionar_usuario(usuarios):
    print("\nAdicionar Usuario")
    nome = input("Nome: ") 
    id = len(usuarios)
    usuarios.append(Usuario(id, nome))

def remover_usuario(usuarios):
    print("\nRemover Usuario")
    id = int(input("Insira o ID do Usuario: "))
    if id >= 0 and id <= len(usuarios):
        usuarios.pop(id)
        print("\nRemovido com Sucesso")
    else:
        print("\nID Inválido\n")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

# Função Principal
def main():
    # Listas para armazenar os dados
    livros = []
    usuarios = []
    autores = []

    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Remover Livro")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Adicionar Usuario")
        print("8. Remover Usuario")
        print("9. Listar Usuarios")
        print("0. Sair")
        choice = input("Escolha uma Opcao: ")

        match choice:
            case '0':
                print("\nFinalizando Programa\n")
                break
            case '1':
                adicionar_livro(livros)
            case '2':
                listar_livros(livros)
            case '3':
                buscar_livro(livros)
            case '4':
                remover_livro(livros)
            case '5':
                emprestar_livro(livros, usuarios)
            case '6':
                devolver_livro(livros, usuarios)
            case '7':
                adicionar_usuario(usuarios)
            case '8':
                remover_usuario(usuarios)
            case '9':
                listar_usuarios(usuarios)
            case _:
                print("Op Invalida")

if __name__ == "__main__":
	main()