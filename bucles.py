def printer(limit):
    number = 1
    while number <= limit:
        print(number)
        number = number * 2

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    printer(LIMITE)


if __name__ == '__main__':
    run()