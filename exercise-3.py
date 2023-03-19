def gcd(*args):
    if len(args) < 2:
        return "Error"

    def gcd_for_two(x, y):
        while y:
            x, y = y, x % y
        return x

    b = args[0]
    for i in args[1:]:
        b = gcd_for_two(b, i)
    return b


print(gcd(4, 8, 16))
