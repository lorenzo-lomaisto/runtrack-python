alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

n = 1
while n * (n + 1) // 2 <= len(alphabet):
    start = (n - 1) * n // 2
    end = start + n
    print(alphabet[start:end].center(50))
    n += 1

