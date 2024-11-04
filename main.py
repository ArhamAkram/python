
def kth_symbol(n, k):
    if n == 1:
        return 0
    sequence = "0"

    for i in range(2**(n-2)):
        if i == 0:
            sequence += "1"
        elif sequence[i] == '0':
            sequence += "01"
        elif sequence[i] == "1":
            sequence += "10"
        elif sequence[-1] == '0':
            sequence += "01"
            kth_symbol(n - 1, k)
        elif sequence[-1] == '1':
            sequence += "10"
            kth_symbol(n - 1, k)
    return int(sequence[k-1])

print(kth_symbol(4,1))









