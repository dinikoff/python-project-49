import random
from datetime import datetime

LOW_LIMIT = 1
HIGH_LIMIT = 20


def get_numbers():
    random.seed(datetime.now())
    first = random.randint(LOW_LIMIT, HIGH_LIMIT)
    second = random.randint(LOW_LIMIT, HIGH_LIMIT)
    return first, second
