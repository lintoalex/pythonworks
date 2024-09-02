
word="pneumonoultramicroscopicsilicovolcanoconiosis"

consonant="aeiou"

vowel_count=0

consonant_count=0

for ch in word:

    if consonant.count(ch)!=0:
        vowel_count+=1

    else:

        consonant_count+=1



print(f"consonant_count{consonant_count}")

print(f"vowel_count{vowel_count}")