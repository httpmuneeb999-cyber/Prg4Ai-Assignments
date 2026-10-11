sentence = input("enter a sentence : ")
words = sentence.split()

def find_longest(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def find_shortest(words):
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

def count_vowels(sentence):
    vowels = 0
    for letter in sentence.lower():
        if letter in "aeiou":
            vowels += 1
    return vowels

total_words = len(words)
total_characters = len(sentence)
longest_word = find_longest(words)
shortest_word = find_shortest(words)
total_vowels = count_vowels(sentence)
unique_words = set(words)
sorted_words = sorted(unique_words)

print("Total words:", total_words)
print("Total characters:", total_characters)
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
print("Total vowels:", total_vowels)
print("Unique words:", unique_words)
print("Alphabetical order:", sorted_words)


file = open("word_analysis.txt", "w")
file.write(
    "word Analysis:\n" +
    "Total words: " + str(total_words) + "\n" +
    "Total characters: " + str(total_characters) + "\n" +
    "Longest word: " + longest_word + "\n" +
    "Shortest word: " + shortest_word + "\n" +
    "Total vowels: " + str(total_vowels) + "\n" +
    "Unique words: " + str(unique_words) + "\n" +
    "alphabetical order: " + str(sorted_words) + "\n"
)
file.close()
