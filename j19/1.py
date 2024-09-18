import numpy as np

# ایجاد آرایه‌ای یک‌بعدی
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# ایجاد آرایه‌ای دوبعدی (ماتریس)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

# ایجاد آرایه‌ای با اعداد ۰ تا ۸
arr = np.arange(9)
print("Original array:", arr)

# تغییر شکل آرایه به ۳x۳
arr_reshaped = arr.reshape(3, 3)
print("Reshaped array (3x3):\n", arr_reshaped)

# ایجاد ۵ عدد بین ۰ و ۱
arr = np.linspace(0, 1, 5)
print(arr)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# جمع دو آرایه
print("Sum:", a + b)

# ضرب عنصر به عنصر دو آرایه
print("Multiplication:", a * b)

# مجذور هر عنصر
print("Squared:", a**2)

arr = np.array([1, 2, 3, 4, 5])

# جمع عناصر
print("Sum:", np.sum(arr))

# میانگین عناصر
print("Mean:", np.mean(arr))

arr = np.array([1, 2, 3, 4, 5])

# دسترسی به عنصر سوم
print("Third element:", arr[2])

# دسترسی به عناصر از اندیس ۱ تا ۳
print("Slice from 1 to 3:", arr[1:4])

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# دسترسی به عنصر وسط (ردیف دوم، ستون دوم)
print("Element at (2, 2):", arr_2d[1, 1])

# دسترسی به تمام ردیف دوم
print("Second row:", arr_2d[1, :])

arr = np.array([1, 2, 3, 4, 5])

# انحراف معیار
print("Standard Deviation:", np.std(arr))

# واریانس
print("Variance:", np.var(arr))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# ضرب دو ماتریس
C = np.dot(A, B)
print("Matrix Multiplication:\n", C)

# تولید ۵ عدد تصادفی بین ۰ و ۱
random_numbers = np.random.rand(5)
print(random_numbers)

# تولید آرایه‌ای از اعداد تصادفی صحیح بین ۰ و ۱۰
random_integers = np.random.randint(0, 10, size=(3, 3))
print(random_integers)
