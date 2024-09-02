
words=["hello","hai","hello","hai","hai","hi"]

# h1=words.count("hello")
# h2=words.count("hi")
# h3=words.count("hai")

# print("hello",h1,"hi",h2,"hai",h3)

word_count={}

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:

     word_count[w]=1

print(word_count)   





     