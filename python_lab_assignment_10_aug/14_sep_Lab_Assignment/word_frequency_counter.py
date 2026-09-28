# write a program that reads a sentences from the user and print the frequency of each word.
# eg, input: "Hello world hello"
# output: hello: 2, world: 1

sentence = input("Enter a sentence: ")
words = sentence.split()
word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
     