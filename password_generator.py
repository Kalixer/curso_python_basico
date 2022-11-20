import random

def generate_password():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    SYMBOLS = ['?', '/', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '<', '>', ';', ':', '"', '[', ' ]', '{', '}', '|', ',', '.']
    NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

    caracteres = MAYUS + MINUS + SYMBOLS + NUMBERS
    passwd = []

    for i in range(15):
        passwd.append(random.choice(caracteres))

    passwd = "".join(passwd)
    return passwd


def run():
    password = generate_password()
    print("This is your new password: " + password)


if __name__ == '__main__':
    run()