# Classe Livro
class Livro():
    def __init__(self, titulo, autor, isbn, disponibilidade):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponibilidade = disponibilidade

    def __str__(self):
        return "Nome: " + str(self._titulo) + "\nAutor: " + str(self._autor) + "\nISBN: " + str(self._isbn) + "\nDisponibilidade: " + str(self._disponibilidade) 

    def get_livro(self):
        pass

    def set_livro(self):
        pass
    
    def adicionar(self):
        pass

    def buscar(self):
        pass

    def emprestar(self):
        pass

    def devolver(self):
        pass

# Classe Autor
class Autor():
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    def get_autor(self):
        pass

    def set_autor(self):
        pass   

# Classe Usuario
class Usuario():
    def __init__(self, id, nome, livros_emprestados):
        self._id = id
        self._nome = nome
        self._livros_emprestados = livros_emprestados

    def get_usuario(self):
        pass

    def set_usuario(self):
        pass  

# Função Principal
def main():
    livros = ()
    usuarios = []

    while True:
        print("\nMenu de Operações:")
        print("1. Adicionar Livro")
        print("2. Emprestar Livro")
        print("3. Devolver Livro")
        print("4. Remover Livro")
        print("5. Adicionar Usuario")
        print("6. Remover Usuario")
        print("0. Sair")
        choice = int(input("Escolha uma Opcao: "))

        match choice:
            case 0:
                print("Saindo")
                break
            case 1:
                # print("Op 1")
                livros = Livro("Melhor Livro", "Eu", 32323, "Disponivel")
                # print(livros)
                livros = Livro("Melhor Livro2", "Eu", 32323, "Disponivel")
                print(livros)

            case 2:
                print("Op 2")
            case 3:
                print("Op 3")
            case 4:
                print("Op 4")
            case 5:
                print("Op 5")
            case 6:
                print("Op 6")
            case _:
                print("Op Invalida")

if __name__ == "__main__":
	main()