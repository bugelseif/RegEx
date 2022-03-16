import re

expressao = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$')


def main():
    senha = input("Digite a senha\n")
    print(validar(senha))


def validar(senha):
    validador = expressao.match(senha)
    if validador:
        return 'válido'
    return 'inválido'


if __name__ == '__main__':
    main()
