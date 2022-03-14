import PIL
from PIL import Image
import os
os.chdir(r"C:\Users\kevin\OneDrive\Pictures\Matthew")

isi = os.listdir(r"C:\Users\kevin\OneDrive\Pictures\Matthew")


for i in isi : 
    if i.startswith("foto"):
        foto = Image.open(i)
        foto.rotate(-90).save(r"C:\Users\kevin\OneDrive\Pictures\Matthew\hasil\ " + i , "JPEG")
        print(i)
    
print("Hello World")

#pubesar= foto.rotate(0).resize((1920,1080))
#os.chdir(r"C:\Users\kevin\OneDrive\Pictures\Matthew\trial123")
#pubesar.save("C:\Users\kevin\OneDrive\Pictures\Matthew\trial123", )