from math import sqrt

x, y, z = map(float,input("Введите основания и высоту трапеции: ").split())

print("Периметр трапеции равеш= ", round (x + y + 2 * sqrt(sqrt(z) + sqrt(x - y) / 4),2))
