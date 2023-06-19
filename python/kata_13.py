# Build Tower Advanced
# https://www.codewars.com/kata/57675f3dedc6f728ee000256
def tower_builder(n_floors: int, block_size: tuple[int, int]):
    floors: list[str] = []
    w, h = block_size
    increment = w * 2
    base = (n_floors * increment) - w
    for level in range(n_floors):
        blocks = (2 * (w * level)) + w
        spaces = (base - blocks) // 2
        floor = f"{' '*spaces}{'*'*blocks}{' '*spaces}"
        for _ in range(h):
            floors.append(floor)
    return floors
