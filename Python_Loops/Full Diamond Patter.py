rows = int(input("Enter Diamond patterns Rows = "))
print("Diamond Star pattern ")
for i in range(1, rows +1):
    for j in range(1, rows - i +1):
        print(end=' ')
    for k in range(0, 2 * i -1):
        print('*', end='')
    print()
for i in range(1, rows):
    for j in range(1, i +1):
        print(end=' ')
    for l in range(0, (2 * (rows - i))):
        print('*', end='')
    print()


