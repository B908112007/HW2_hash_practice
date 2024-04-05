def count_words(filename):
    word_count = {}
    total_unique_words = 0

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                    total_unique_words += 1

    return total_unique_words, word_count

def main():
    filename = 'hw2_data.txt'
    total_unique_words, word_count = count_words(filename)

    print("總共出現單字數:", total_unique_words)
    print("每個單字出現的次數:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
  
