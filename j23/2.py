def read_file_lazy(file_name):
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            yield line.strip()


for line in read_file_lazy("sample.txt"):
    print(line)

