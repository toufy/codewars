import re


# Converting string to camel case
# https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text: str):
    lst = re.split("-|_", text)
    if lst[0] == lst[0].upper():
        return " ".join(lst).title().replace(" ", "")
    return lst[0] + " ".join(lst[1:]).title().replace(" ", "")
