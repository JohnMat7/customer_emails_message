from datetime import *


def time_():
    time_today = datetime.today()
    time = time_today.strftime("%H:%M:%S")
    return time


def date_():
    date_today = datetime.today()
    date = date_today.strftime("%d %B %Y  ")
    return date
