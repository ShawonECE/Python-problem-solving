from numpy import random
x = random.randint(9, size=(4))
y = list(x)
z = []
count = 0

for i in range(10):
    seq = input('Enter 4 digit sequence: ')
    num_seq = list(map(int, seq.split()))
    for j in range(4):
        if num_seq[j] != y[j]:
            if num_seq[j] not in y:
                z.append('Wrong digit')
            else:
                z.append('Wrong position')
        else:
            z.append('Right')
            #count = count + 1
    if num_seq == y:
        count = count + 1
    print(z)
    z = []

print('Chance over. You have corrected', count, 'times.')
print('Original sequence is: ', y)
