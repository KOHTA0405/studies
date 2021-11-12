a = 1
b = 1

# assert <評価したい式>, "TRUEじゃない時のメッセージ"
assert a + b == 2, "a + b is equal to 2"

def power(base, exp):
    return base * exp


assert power(3, 2) == 9, "3 ** 2 should be 9"