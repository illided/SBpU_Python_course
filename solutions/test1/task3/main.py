from statistic import FileStatistic


def main():
    stat = FileStatistic("Alice_in_wonderland.txt")
    open("stat.txt", 'w').close()
    with open("stat.txt", 'a') as stat_output:
        stat_output.write("Top 10 words:\n")
        for el in stat.get_most_common():
            stat_output.write(f"{el[0]} : {el[1]}\n")
        stat_output.write(f"Num of sentences in text: {stat.get_num_of_sentences()}\n")



if __name__ == '__main__':
    main()
