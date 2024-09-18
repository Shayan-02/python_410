lst = []

for i in range(1, 25):
    lst.append(i)

# sum = 0
# for j in lst:
#     sum += j

sums = sum(lst)
avg = sums/len(lst)
print(avg)
max = 0
for k in lst:
    if k > max:
        max = k

# for l in lst:
#     if l < min:
#         min = l
print(min(lst))
print(sum)
print(max)