import requests

img_url = "https://media.ctmusicshop.com/wp-content/uploads/2021/10/26095540/Schecter-Reaper-7-Multi-Scale--500x500.webp"
img_data = requests.get(img_url).content
with open('image_1.png', 'wb') as handler: #open คือการขอ os เข้าไปทำอะไรซักอย่างใน Harddisk ซึ่ง เราขอ wb หรือเรียกว่า write binary 
    handler.write(img_data) #เขียน img_data(เป็น binary) ลง handler(คือ image_1.jpg ในโหมด wb)
# print(img_data)