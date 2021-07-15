def bipolar(agents):
    a = list(range(agents))
    b = []
    b.append(a)
    b.append(a[::-1])
    return b


if "__main__" == __name__:
    print(bipolar(10))