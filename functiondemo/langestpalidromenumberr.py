
text="RACECAR"

longest_palidrome=""

for i in range(0,len(text)):

    left=i

    right=i

    while(left>=0 and right<len(text) and text[left]==text[right]):

        current_palidrome_text=text[left:right+1]

        if len(current_palidrome_text) >len(longest_palidrome):

            longest_palidrome=current_palidrome_text

        left=left-1

        right=right+1

print(longest_palidrome)            