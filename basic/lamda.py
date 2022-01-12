def two(x):
    return x * 2


# the one with the single par
Two = lambda x: x * 2

# the one with the many par
sub = lambda x, y: x * y


tables = [lambda y, x=x: x * y for x in range(1, 11)]
for table in tables:
    print(table(1))
