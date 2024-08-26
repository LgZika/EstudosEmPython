class Livro:
    def __init__(self, id_livro, titulo, autor, isbn, disponibilidade=True):
        self.__id_livro = id_livro
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn 
        self.__disponibilidade = disponibilidade 

    def __str__(self):
        status = "Disponivel" if self.__disponibilidade == True else "Indisponivel"
        return f'ID: {self.__id_livro}\nTitulo: {self.__titulo}\nAutor: {self.__autor}\nISBN: {self.__isbn}\nStatus: {status}\n'
    
    @property
    def get_titulo(self) -> str:
        return self.__titulo

    @get_titulo.setter
    def set_titulo(self, valor_qualquer_ai):
        self.__titulo = valor_qualquer_ai


def main() -> None:
    livro01 = Livro(0, "OlaMundo", "eu", "777")
    # print(livro01)
    print(livro01.get_titulo)
    livro01.set_titulo = "ola"
    print(livro01.get_titulo)
        
if __name__ == "__main__":
	main()