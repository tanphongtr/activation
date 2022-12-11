import nanoid
import datetime
import random

def nanoid_generate(size=6):
    nw = datetime.datetime.now().strftime('%y%m%d')
    return f"1-{nw}-{nanoid.generate(size=size, alphabet='0123456789')}"

def order_id_generate(size=6):
    return random.randint(1, 9)
    random_number = random.randint(1, 9)
    today = datetime.datetime.now().strftime('%d')

    return f"{random_number}{today}{nanoid.generate(size=size, alphabet='0123456789')}"

    # random from 1 to 9