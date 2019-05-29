word=input('Enter word:')
count=1
word_count=0
for letter in word:
    if letter[0]==letter[count]:
        print letter[0]