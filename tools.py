import random
import string

def generate_randstring(num = 8):
    value = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return(value)
