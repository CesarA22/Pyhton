class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def obter_titulo(self):
        return self._titulo

    def obter_autor(self):
        return self._autor

    def obter_ano_publicacao(self):
        return self._ano_publicacao

    def esta_disponivel(self):
        return self._disponivel

    def definir_disponibilidade(self, status):
        self._disponivel = status


class Usuario:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._livros_emprestados = []

    def obter_nome(self):
        return self._nome

    def obter_email(self):
        return self._email

    def emprestar_livro(self, livro):
        if livro.esta_disponivel():
            self._livros_emprestados.append(livro)
            livro.definir_disponibilidade(False)
            print(f"Livro '{livro.obter_titulo()}' emprestado para {self._nome}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)
            livro.definir_disponibilidade(True)
            print(f"Livro '{livro.obter_titulo()}' devolvido por {self._nome}.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não foi emprestado por {self._nome}.")


class CatalogoLivros:
    def __init__(self):
        self._livros = []

    def adicionar_livro(self, livro):
        if livro.esta_disponivel():
            self._livros.append(livro)
            print(f"Livro '{livro.obter_titulo()}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível.")

    def remover_livro(self, livro):
        if livro in self._livros:
            self._livros.remove(livro)
            print(f"Livro '{livro.obter_titulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obter_titulo()}' não está na biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self._livros:
            if livro.obter_titulo() == titulo:
                return livro
        return None


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def adicionar_usuario(self, usuario):
        if usuario.obter_nome() != "":
            self._usuarios.append(usuario)
            print(f"Usuário '{usuario.obter_nome()}' adicionado à biblioteca.")
        else:
            print("Nome de usuário inválido.")

    def remover_usuario(self, usuario):
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)
            print(f"Usuário '{usuario.obter_nome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obter_nome()}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome):
        for usuario in self._usuarios:
            if usuario.obter_nome() == nome:
                return usuario
        return None


class GestorEmprestimos:
    @staticmethod
    def emprestar_livro(usuario, livro):
        if livro.esta_disponivel():
            usuario.emprestar_livro(livro)
        else:
            print(f"Livro '{livro.obter_titulo()}' não está disponível para empréstimo.")

    @staticmethod
    def devolver_livro(usuario, livro):
        usuario.devolver_livro(livro)


# Exemplo de uso do código:
# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)
# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")
# Criação dos gestores
catalogo = CatalogoLivros()
gestor_usuarios = GestorUsuarios()
gestor_emprestimos = GestorEmprestimos()
# Adicionar livros ao catálogo
catalogo.adicionar_livro(livro1)
catalogo.adicionar_livro(livro2)
# Adicionar usuários ao gestor
gestor_usuarios.adicionar_usuario(usuario1)
gestor_usuarios.adicionar_usuario(usuario2)
# Empréstimo de livro
gestor_emprestimos.emprestar_livro(usuario1, livro1)
# Tentativa de empréstimo de livro indisponível
gestor_emprestimos.emprestar_livro(usuario2, livro1)
# Devolução de livro
gestor_emprestimos.devolver_livro(usuario1, livro1)
# Remoção de livro
catalogo.remover_livro(livro2)
# Remoção de usuário
gestor_usuarios.remover_usuario(usuario2)
# Busca de livro e usuário
livro_encontrado = catalogo.buscar_livro("Python para Iniciantes")
usuario_encontrado = gestor_usuarios.buscar_usuario("Alice")
# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.obter_titulo())
if usuario_encontrado:
    print(usuario_encontrado.obter_nome())
