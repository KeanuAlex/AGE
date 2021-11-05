s = "аворт"
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                st = a + b + c + d
                count += 1
                if st == "вата":
                    print(count, st)
