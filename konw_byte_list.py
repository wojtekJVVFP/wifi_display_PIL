
a = [50, 345, 286, 60000]
ab = []
abr = [0]

#konwersja z int na bytes
def list_to_bytes(n):
    ret
    for i in n:
        ab.append(i.to_bytes(2,'little'))


print(ab[0])
j=0
for i in ab:
    abr[j] = int.from_bytes(i,'little')
    print(i, abr[j])
    abr.append(0)
    j += 1
