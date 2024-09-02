
source_word="CHICKEN"

target_word="HHEN"

word_count={}

for c in source_word:

        if c in word_count:

            word_count[c]+=1

        else:
    
            word_count[c]=1

is_kangaroo_word=True

for c in target_word:
                 
    if c in word_count and word_count.get(c)>0:
                      
        word_count[c]-=1

    else:
         
         is_kangaroo_word=False

print(is_kangaroo_word)
