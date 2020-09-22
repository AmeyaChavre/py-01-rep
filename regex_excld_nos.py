import re

sentence = "This is a sentence from future with 18 words written in 2050 after 30 years from today 22nd-Sept-2020"

pattern = r'[^\d]+'
list_of_words=[]
for word in re.finditer(pattern,sentence):
    list_of_words.append(word.group())
print(f"List with excluded numbers : {list_of_words}")
