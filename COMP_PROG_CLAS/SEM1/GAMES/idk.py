first = "abcde"
second = "zyxwv"

res = ""
for i in range(len(first)):
    res = res + first[i] + second[i]
print(res)