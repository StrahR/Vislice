import math


def sieve(n: int) -> list:
    bit_field = [True] * (n+1)
    bit_field[0] = False
    bit_field[1] = False

    for i in range(2, math.floor(math.sqrt(n))+1):
        if bit_field[i]:
            for k in range(2*i, n+1, i):
                bit_field[k] = False
    return [i for i in range(n+1) if bit_field[i]]


print("Praštevila manjša od 200:")
print("\n".join(map(str, sieve(200))))
