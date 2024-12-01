from abc import ABC, abstractmethod

# Classe base Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    @abstractmethod
    def exibir_informacoes(self):
        pass

# Subclasse UsuarioComum
class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
        else:
            print("Não é possível emprestar o livro.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

# Subclasse Administrador
class Administrador(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)

    def cadastrar_livro(self, titulo, autor, ano):
        return Livro(titulo, autor, ano)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

# Classe base ItemBiblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    @abstractmethod
    def exibir_detalhes(self):
        pass

# Subclasse Livro
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Status: {status}")

# Funções para relatórios
def exibir_livros_disponiveis(livros):
    for livro in livros:
        if livro.disponivel:
            livro.exibir_detalhes()

def exibir_usuarios_com_livros(usuarios):
    for usuario in usuarios:
        if usuario.livros_emprestados:
            usuario.exibir_informacoes()
            for livro in usuario.livros_emprestados:
                livro.exibir_detalhes()

# Exemplo de uso
if __name__ == "__main__":
    admin = Administrador("Admin", 30, "A001")
    usuario = UsuarioComum("Matheus Marinho", 19, "37023311")

    livro1 = admin.cadastrar_livro("Livro 1", "Autor 1", 2000)
    livro2 = admin.cadastrar_livro("Livro 2", "Autor 2", 2005)

    usuario.emprestar_livro(livro1)
    usuario.emprestar_livro(livro2)

    exibir_livros_disponiveis([livro1, livro2])
    exibir_usuarios_com_livros([usuario])