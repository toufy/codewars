def rgb(r: int, g: int, b: int):
    h16 = "%02x%02x%02x" % (
        max(0, min(r, 255)),
        max(0, min(g, 255)),
        max(0, min(b, 255)),
    )
    return h16.upper()
