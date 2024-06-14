import random
import string


def generate_code():
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(8))
    return codigo
