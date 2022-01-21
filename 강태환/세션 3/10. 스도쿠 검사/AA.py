import sys
#sys.stdin = open('input.txt', 'rt')
a = [list(map(int, input().split())) for _ in range(9)]
b = [1,2,3,4,5,6,7,8,9]
def sdk(x):
    sdk1 = list()
    for i in range(3):
        for j in range(3):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(3):
        for j in range(3,6):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(3):
        for j in range(6,9):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(3,6):
        for j in range(3):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(3,6):
        for j in range(3,6):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(3,6):
        for j in range(6,9):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(6,9):
        for j in range(3):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(6,9):
        for j in range(3,6):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    sdk1 = list()
    for i in range(6,9):
        for j in range(6,9):
            sdk1.append(a[i][j])
            sdk1 = sorted(sdk1)
    if sdk1 != b:
        return False
    return True

if sdk(a):
    print('YES')
else:
    print('NO')