 # Задача Иосифа Флавия

n = int(input())
k = int(input())
l = list(range(1, n + 1))

def kill(li, var):
    li.append(var)
    return li

def cycle(l, k, count=0):
    l1 = []
    while len(l1) < len(l):
        for i in range(0, len(l)):
            if l[i] == '*':
                count += 0
            else:
                count += 1
            if count == k:
                kill(l1, l[i])
                l[i] = '*'
                count = 0
    else:
        print(l1[-1])

cycle(l, k)