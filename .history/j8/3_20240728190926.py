a = "hello worlld"
lst = []
sums = ""
for i in a:
    sums += i
    if i == " ":
        continue
        lst.append(sums)
        
print(lst)