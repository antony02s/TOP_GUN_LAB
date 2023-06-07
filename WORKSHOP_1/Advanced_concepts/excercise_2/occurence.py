# Create a Python program that reads a text file and counts the occurrences of each
# word using a dictionary. The program should print the words and their counts.

def count_word_occurence():
    word_count = {}

    with open(r"C:\\Users\ACER\Desktop\\Repo_TOP_GUN\\TOP_GUN_LAB\WORKSHOP_1\\Advanced_concepts\\excercise_2\\text.txt",'r') as file:
        for line in file:
            words = line.strip().split()

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count

def word_counts(word_count):
    for word, count in word_count.items():
        print(f'{word}: {count}')