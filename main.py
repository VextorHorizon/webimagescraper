import os
import requests
from bs4 import BeautifulSoup 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str)
args = parser.parse_args()

#ขอเนื้อเว็บ
user_input = args.url #url ของเว็บ 
url = requests.get(user_input).content #ขอ content(เปรียบเทียบเป็นกล่องพัสดุ content คือเอาแค่ของในพัสดุ ตัดชื่อผู้ส่งผู้รับที่อยู่บ้านเบอร์โทร)
html_content = BeautifulSoup(url, "html.parser") #กำหนดกฎที่เราจะอ่านไอเจ้านี่ให้เป็นกฎของ html

#หา tags img ในตัวของ content ที่ได้มา
imgs_in_targetweb = html_content.find_all('img') #ได้ list ขอ ที่แปะแท็ค img ทั้งหมดในกล่อง html_content

# imgs_purify = []
# for image in imgs_in_targetweb:
#     image_url = image['src'] #แยกทุกอย่างในแท็ก <img> ออก ให้เหลือแต่ไส้ในที่เราต้องการ ซึ่งคือ src มันมี image url อยู่
#     if 'png' or 'jpg' or 'webp' in image_url: #เอา png jpg webp เท่านั้น ยัดลง imgs_purify
#         imgs_purify.append(image_url)
#     for img_num, image_in_purify in enumerate(imgs_purify, start=1):
#         if 'png' in image_in_purify:
#             img_data = requests.get(image_in_purify).content
#             with open(f'image_{img_num}.png', 'wb') as imgbinary:
#                 imgbinary.write(image_in_purify)
#         elif 'jpg' in image_in_purify:
#             img_data = requests.get(image_in_purify).content
#             with open(f'image_{img_num}.jpg', 'wb') as imgbinary:
#                 imgbinary.write(image_in_purify)
#         elif 'webp' in image_in_purify:
#             img_data = requests.get(image_in_purify).content
#             with open(f'image_{img_num}.webp', 'wb') as imgbinary:
#                 imgbinary.write(image_in_purify)

                



# ระบุว่าเว็บที่เราต้องการให้ไปดึงรูปภาพคือเว็บอะไร /// input ของ user
# ค้นหารูปภาพที่เราต้องการจากเว็บที่เราใส่ไป /// หน้าที่ bs4
# download รูปภาพ /// img_data = requests.get(img_url).content
# ระบุว่า path ที่จะให้ download รูปไปเก็บ ไปเก็บที่ไหน /// os ชี้ path