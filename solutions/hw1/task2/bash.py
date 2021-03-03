import os


def wc(first: str, *args: str):
    def wc_for_one(filepath: str):
        size = os.path.getsize(filepath)
        f = open(filepath)
        words = 0
        lines = 0
        for line in f:
            lines += 1
            words += len(line.split())
        f.close()
        return {"newlines": lines, "words": words, "bytes": size}

    acc = {"newlines": 0, "words": 0, "bytes": 0}
    files_not_found = []
    for filename in [first, *args]:
        try:
            file_wc = wc_for_one(filename)
        except FileNotFoundError:
            files_not_found.append(filename)
            continue
        print(str(file_wc) + "\t" + filename)
        acc = {k: acc.get(k, 0) + file_wc.get(k, 0) for k in acc}
    print(str(acc), "\ttotal")
    if files_not_found:
        print("Files not found: ", end="")
        for file in files_not_found:
            print(file, end=", ")


def nl(filepath: str):
    try:
        file = open(filepath)
    except FileNotFoundError:
        print("No such file: ", filepath)
        return
    count = 1
    for line in file:
        if line == "\n":
            print()
        else:
            print(str(count) + " " + line, end="")
            count += 1
    file.close()


def head(filename: str, n=10):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("No such file: " + filename)
        return
    text = f.readlines()
    cut = text[: len(text) - n if len(text) >= n else len(text)]
    for line in cut:
        print(line, end="")


def tail(filename: str, n=10):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("No such file: " + filename)
        return
    text = f.readlines()
    cut = text[len(text) - n if len(text) >= n else 0 :]
    for line in cut:
        print(line, end="")
