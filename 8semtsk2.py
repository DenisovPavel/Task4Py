def long_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().split()
        count_words = 0

        for i in range(len(text)):
            if len(text[i]) > count_words:
                count_words = len(text[i])
        for j in text:
            if len(j) == count_words:
                print(j, end=" ")

long_words("Pushkin.txt")