
text="hello hai hello hai hello"

word=text.split(" ")

words_count={}

for w in word:

    if w in words_count:

        words_count[w]+=1

    else:

        words_count[w]=1

print(words_count)