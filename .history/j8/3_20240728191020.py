a = "hello worlld"
lst = []
sums = ""
for i in a:
    if i == " ":
        continue
    sums += i
    lst.append(sums)
        
print(lst)