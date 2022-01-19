import sys
#sys.stdin = open('input.txt', 'rt')
n,m = map(int, input().split())
a = list(map(int, input().split()))
st = 0
fin = 1
cnt = 0
hap = a[st]
while True:
    if hap < m:
        if fin<n:
            hap+=a[fin]
            fin+=1
        else:
            break
    elif hap == m:
        cnt += 1
        st += 1
        fin = st+1
        hap = a[st]
    else:
        st +=1
        fin = st+1
        hap = a[st]
print(cnt)