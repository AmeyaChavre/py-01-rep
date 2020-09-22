import re

text = "This is a very long paragraph , with phone numbers. Whitehouse : 555-555-5555 . DisneyLand : 888-878-9090 . Police Department : 911-119-911. McDonalds : 667-687-6767. Fire Department : 999-911-9111. US Coast Guard : 123-232-7867."
count=0
for phone_no in re.finditer(r'\d{3}-\d{3}-\d{4}',text):
    count+=1
    print(f"\tPhone Number {count}: {phone_no.group()}\n")
print(f"\tThere are {count} phone numbers in the text.")
