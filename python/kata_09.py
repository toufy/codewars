import re


# Extract the domain name from a URL
# https://www.codewars.com/kata/514a024011ea4fb54200004b
def domain_name(url: str):
    regex = "(:\\/\\/|.*www\\.)([^\\.]*)"
    pattern = re.search(regex, url)
    if pattern:
        return pattern.group(2)
    regex = "(^[a-zA-Z0-9]*)(\\.)"
    pattern = re.search(regex, url)
    if pattern:
        return pattern.group(1)
