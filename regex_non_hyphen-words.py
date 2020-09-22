import re

text = "In this text-oriented string how can you remove non-hyphen words?"

pattern = r'[\w]+-[\w]+'

print(re.findall(pattern,text))
