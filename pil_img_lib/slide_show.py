from PIL import Image

# Starts the slide show for images kept in folder MacOS Images

file_name=[]
file_size=[]
file_format_desc=[]
for image_no in range(1,12):
    display_image = Image.open(f"C:\\Users\\acer\\Desktop\\MacOS Images\\file_{image_no}.jpg")
    display_image.show()
    file_name.append(display_image.filename)
    file_size.append(display_image.size)
    file_format_desc.append(display_image.format_description)
print(f"File name list : {file_name} \n\n")
print(f"File size list : {file_size} \n\n")
print(f"File Format Description : {file_format_desc}")
    
	
