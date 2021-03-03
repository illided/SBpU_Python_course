import os


def wc(first: str, *args: str):
    def wc_for_one(filepath: str) -> dict:
        size = os.path.getsize(filepath)
        with open(filepath) as f:
            words, lines = 0, 0
            for line in f:
                lines += 1
                words += len(line.split())
        return {"newlines": lines, "words": words, "bytes": size}

    def print_stats(dictionary: dict, f_name: str):
        print("\t".join([str(x) for x in dictionary.values()]), "\t", f_name)

    total = {"newlines": 0, "words": 0, "bytes": 0}
    files_not_found = []
    for filename in [first, *args]:
        try:
            file_wc = wc_for_one(filename)
        except FileNotFoundError:
            files_not_found.append(filename)
            continue
        print_stats(file_wc, filename)
        total = {k: total.get(k, 0) + file_wc.get(k, 0) for k in total}
    print_stats(total, "total")
    if files_not_found:
        print("Files not found: ", ", ".join(files_not_found))


def nl(first: str, *filenames: str):
    count = 1
    for filename in [first, *filenames]:
        try:
            with open(filename) as file:
                for line in file:
                    if line == "\n":
                        print()
                    else:
                        print(str(count) + "\t" + line, end="")
                        count += 1
                print()
        except FileNotFoundError:
            print("nl: ", filename, ": No such file or directory")


def head(filename: str, n: int = 10):
    try:
        with open(filename) as file:
            for line in file:
                if n > 0:
                    n -= 1
                    print(line, end="")
                else:
                    break
    except FileNotFoundError:
        print("No such file: " + filename)


def tail(filename: str, n: int = 10):
    try:
        with open(filename) as file:
            text = file.readlines()
            cut = text[len(text) - n:]
            for line in cut:
                print(line, end="")
    except FileNotFoundError:
        print("No such file: " + filename)
