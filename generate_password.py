import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
chars = digits + lowercase_letters + uppercase_letters + punctuation

cntPw = input('Укажите количество паролей для генерации: ')
lenPw = input('Укажите длину одного пароля: ')

def generate_password(length, chars):
    """Генератор паролей."""

    password = ''
    for i in range(0, int(lenPw), 4):
        password += random.choice(chars[0:9])
        password += random.choice(chars[10:36])
        password += random.choice(chars[37:63])
        password += random.choice(chars[64:77])
    random.shuffle(list(password))
    return password[0: int(lenPw)]


if __name__=="__main__":
    for m in range(int(cntPw)):
        print(generate_password(lenPw, chars))