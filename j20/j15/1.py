# dataset:
# 1) structural ---> excel, csv, txt, ...
# 2) unsctrucural ---> image, voice, text (email), ...

import pandas as pd
import numpy as np

# student table
student_info = {
    "name": ['amin', 'ali', 'reza', 'amir', "mohsen", "hossein"],
    "age": [20, 23, np.nan, 22, np.nan, 19],
    "degree": ['BS', 'BS', 'MS', 'MS', "PHD", "BS"],
    "ins": [True, False, True, False, False, False],
    "gpa": [3.5, 3.7, 3.6, 3.8, 3.9, 4]
}

for key, value in student_info.items():
    print(f"key: {key}\tvalue: {value}")

student_df = pd.DataFrame(student_info)
print(student_df)