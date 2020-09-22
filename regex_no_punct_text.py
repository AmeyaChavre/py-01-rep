import re

text = "This is a string!! , with a lot of punctuation(s). How can we remove it ?"
text_no_punct = ''
for words in re.finditer(r'[^!,?.()]+',text):
    text_no_punct+=(words.group())
list_no_punct = text_no_punct.split()
print(f"List with no punctuations : {list_no_punct}")
