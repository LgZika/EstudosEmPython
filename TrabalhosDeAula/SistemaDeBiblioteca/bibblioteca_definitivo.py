class Livro:
    def __init__(self, id, titulo, autor, isbn, disponibilidade=True):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn 
        self.__disponibilidade = disponibilidade 
         
    def __str__(self):
        return f'ID: {self.__id}\nTitulo: {self.__titulo}\nAutor: {self.__autor}\nISBN: {self.__isbn}\nStatus: {self.__disponibilidade}\n'
       
    def adicionar(self, biblioteca):
        biblioteca.livros.append(self)
    
    def emprestar(self):
        pass

    def devolver(self):
        pass
    
    @staticmethod
    def buscar(biblioteca, id=None, titulo=None):
        livros_encontrados = []

        for livro in biblioteca.livros:
            if (id == livro.__id) or (titulo and titulo.lower() in livro.__titulo):
                livros_encontrados.append(livro)

        return livros_encontrados

class Usuario:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__livros_emprestados = []

    def __str__(self):
        return f'ID: {self.__id}\nNome: {self.__nome}\nLivros Emprestados: {self.__livros_emprestados}\n'
    
    def adicionar(self, biblioteca):
        biblioteca.usuarios.append(self)

class Autor:
    pass

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

# Função que administra e trata o input de livros no sistema
def adicionar_livro(biblioteca):
    print("\nAdicionar Livro")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    id = len(biblioteca.livros)

    livro = Livro(id, titulo, autor, isbn) # Objeto livro recebe uma instância da classe Livro inciada com o seu construtor
    livro.adicionar(biblioteca)            # Usa-se o método adicionar da classe para inserir o novo livro na biblioteca

# Função para exibir todos os livros armazenados na biblioteca e seus atributos
def listar_livros(biblioteca):
    for livro in biblioteca.livros:
        print(livro)

# Função para pesquisar por livros no sistema
def buscar_livros(biblioteca):
    print("\nBuscar Livro por:")
    print("(1) ID")
    print("(2) Titulo")
    # print("(0) Cancelar")
    opcao = int(input("Opcao escolhida: "))

    if opcao == 1:
        id = int(input("\nInsira o ID do livro: "))
        livros_encontrados = Livro.buscar(biblioteca, id)
    elif opcao == 2:
        titulo = input("\nInsira o Titulo do livro: ")
        livros_encontrados = Livro.buscar(biblioteca, titulo)
    else:
        print("Opcao invalida. Tente novamente.")

    if livros_encontrados:
        print("Livros encontrados:\n")
        for livro in livros_encontrados:
            # print(livro)
            # status = "Disponivel" if livro.disponibilidade == True else "Indisponivel"
            print(f'ID: {livro.id}\nTitulo: {livro.titulo}\nAutor: {livro.autor}\nISBN: {livro.isbn}\nStatus: {livro.disponibilidade}\n')

# Função para adicionar novos usuarios ao sistema
def adicionar_usuario(biblioteca):
    print("\nAdicionar Usuario")
    nome = input("Nome: ") 
    id = len(biblioteca.usuarios)

    usuario = Usuario(id, nome)     # Objeto usuario recebe uma instância da classe Usuario inciada com o seu construtor
    usuario.adicionar(biblioteca)   # Usa-se o método adicionar da classe para inserir o novo usuario na biblioteca

def listar_usuarios(biblioteca):
    for usuario in biblioteca.usuarios:
        print(usuario)

def main():
    biblioteca = Biblioteca() # Instância da classe Biblioteca
    
    while True:
        print("\n======= Menu =======")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        #print("4. Remover Livro")
        print("5. Emprestar Livro")
        print("6. Devolver Livro")
        print("7. Adicionar Usuario")
        print("8. Listar Usuarios")
        #print("9. Remover Usuario")
        print("0. Sair")
        print("====================")
        opcao = input("Digite o número da opcao: ")

        match opcao:
            case "0": 
                print("Saindo...") 
                break
            case "1": 
                adicionar_livro(biblioteca)
            case "2": 
                listar_livros(biblioteca)
            case "3": 
                buscar_livros(biblioteca)
            case "7":
                adicionar_usuario(biblioteca)
            case "8":
                listar_usuarios(biblioteca)
            case _:
                print("Opcao invalida. Tente novamente.")

    
if __name__ == "__main__":
	main()