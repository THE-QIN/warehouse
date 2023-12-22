def kelipatan(x, y):
    if x < 0 or y < 0:
        raise ValueError("X dan Y harus positif atau nol")
    if x == 0 or y == 0:
        raise ValueError("X atau Y tidak boleh nol")
    return x * y 