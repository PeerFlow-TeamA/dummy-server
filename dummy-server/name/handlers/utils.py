import random

date_random_min = {
    'year': 2022,
    'month': 1,
    'day': 1,
    'hour': 0,
    'minute': 0,
    'second': 0,
}
date_random_max = {
    'year': 2023,
    'month': 12,
    'day': 28,
    'hour': 23,
    'minute': 59,
    'second': 59,
}

def random_datetime():
    year = random.randint(date_random_min['year'], date_random_max['year'])
    month = random.randint(date_random_min['month'], date_random_max['month'])
    day = random.randint(date_random_min['day'], date_random_max['day'])
    hour = random.randint(date_random_min['hour'], date_random_max['hour'])
    minute = random.randint(date_random_min['minute'], date_random_max['minute'])
    second = random.randint(date_random_min['second'], date_random_max['second'])
    return f'{year}-{month}-{day} {hour}:{minute}:{second}'

export = {
    "random_datetime": random_datetime
}