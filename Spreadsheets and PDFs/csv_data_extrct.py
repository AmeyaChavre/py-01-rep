import csv

open_file = open("C:\\Users\\User-PC\\Desktop\\example.csv",encoding="utf-8")

csv_data = csv.reader(open_file)

extracted_data = list(csv_data)

print(f"Extracted Data : {extracted_data}\n")
print(f"Number of rows in the spreadsheet : {len(extracted_data)-1}\n")
print("List of Columns:\n")
column_count=0
for column_name in extracted_data[0]:
    column_count+=1
    print(f"\tColumn {column_count} : {column_name}")
print(f"\nNumber of columns in the spreadsheet : {column_count}\n")
mailing_list=[]

for emails in extracted_data[1:]:
    mailing_list.append(emails[3])
print(f"List of all emails in spreadsheet : {mailing_list}")

amazon_accounts = []
for any_email in mailing_list:
    if "amazon.com" in any_email:
        amazon_accounts.append(any_email)
print(f"\nList of Amazon Accounts : {amazon_accounts}")

aws_accounts = open('C:\\Users\\User-PC\\Desktop\\aws_accounts.csv',mode='w',newline='')

csv_results = csv.writer(aws_accounts,delimiter=',')

csv_results.writerow(['dhowatt6@amazon.com', 'kherion7@amazon.com', 'hbraidwoodz@amazon.com'])

aws_accounts.close()

print(f"Amazon accounts have been saved in aws_accounts.csv")

    
    
    






