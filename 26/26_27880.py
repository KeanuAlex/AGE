with open("file/26_ 27880.txt") as f:
    data = f.readlines()
S, _ = map(int, data[0].split())
del data[0]
data = sorted(list(map(int, data)))
total = 0
for i, val in enumerate(data):
    if total +val > S:break
    total += val
print(i)
delta = S - total
condidates = [x for x in data if x-data[i-1]<=delta]
print(max(condidates))