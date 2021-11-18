with open("file/24_27421.txt") as f:
    s = f.readline()
count = 0
Maxcount = 0
for char in range(1, len(s)):
    if s[char] != s[char - 1]:
        count += 1
        Maxcount = max(Maxcount, count)
    else:
        count = 0
print(Maxcount)
