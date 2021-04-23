from statistic import FileStatistic


def main():
    stat = FileStatistic("Alice_in_wonderland.txt")
    print("Top 10 words:")
    for el in stat.get_most_common():
        print(f"{el[0]} : {el[1]}")
    print(f"Num of sentences in text: {stat.get_num_of_sentences()}")


if __name__ == '__main__':
    main()
