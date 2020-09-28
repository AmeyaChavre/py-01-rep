from PIL import Image

# Starts the slide show for images kept in folder MacOS Images
for image_no in range(1,12):
    display_image = Image.open(f"C:\\Users\\acer\\Desktop\\MacOS Images\\file_{image_no}.jpg")
    display_image.show()
