def is_palidrome(word):
    
    sliced_str=word[::-1]

    return word==sliced_str

print(is_palidrome("madam"))
