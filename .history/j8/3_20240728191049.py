a = "hello worlld"
lst = []
sums = ""
for i in a:
    sums += i
    if i == " ":
        lst.append(sums)
        continue
        
print(lst)