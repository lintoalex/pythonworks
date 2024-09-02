
f=open("C:\\Users\\linto\\OneDrive\\Desktop\\PythonJuneWorks\\Fileoperations\\english_story.txt","r")


word_list=[w for line in f for w in line.rstrip("\n").split(" ")]

# print(word_list)


# for line in f:

#     word_list=line.rstrip("\n").split(" ")

#     for w in f:

#       word=word_list.append(w)

# print(word_list)

wc={w:word_list.count(w) for w in word_list}

# print(wc)

def get_value(key):

    return wc.get(key)

srt=sorted(wc,key=get_value,reverse=True)

# print(srt)





 