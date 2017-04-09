def generic_read_question(file_path, index):
    f = open(file_path, 'r')
    for idx, line in enumerate(f):
        x = line.strip()
        if index == idx+1:
            f.close()
            return eval(x)
