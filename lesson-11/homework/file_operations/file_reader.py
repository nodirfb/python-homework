def read_file(file_path):
    with open(file_path, 'r') as f:
        for i in f:
            print(i)