# Directions Reduction
# https://www.codewars.com/kata/550f22f4d758534c1100025a


def dirReduc(arr: list[str]):
    conflicts = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    redDirs: list[str] = []
    for dir in arr:
        if not redDirs:
            redDirs.append(dir)
        elif redDirs[-1] == conflicts.get(dir):
            redDirs.pop()
        else:
            redDirs.append(dir)
    return redDirs
