def get_percentage(number, round_digits=None):
    return "{}%".format(round(number * 100, ndigits=round_digits))
