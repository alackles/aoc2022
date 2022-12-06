with open("input.txt") as f:
    signal = f.read().strip()

def find_start(signal, m=4):
    n = len(signal)
    q = [i for i in signal[0:m]]
    for i in range(m, n):
        q.pop(0)
        if len(set(q)) == m-1 and signal[i] not in q:
            return i+1
        q.append(signal[i])
    
print(find_start(signal))
print(find_start(signal,m=14))