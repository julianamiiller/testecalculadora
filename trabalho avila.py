usuario_ativo = "Igor"
senha_valida = "1234"

usuario_digitado = input("Digite o nome de usuário: ")
senha_digitada = input("Digite a senha: ")

if usuario_ativo == usuario_digitado and senha_digitada == senha_valida:
    print("Acesso permitido")
else:
    print("Usuário ou senha incorretos")