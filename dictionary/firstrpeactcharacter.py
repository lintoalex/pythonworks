text="ABCCDDBB"

words_count={}

for c in text:

    if c in words_count:

        print(c,"first recursive character")

        break

    else:

        words_count[c]=1