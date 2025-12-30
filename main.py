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

png = []
jpg = []
webp = []

for img in imgs_in_targetweb: #loop วนดูใน list imgs_in_targetweb ก้คือ img ไล่ไปทีละตัวๆใน imgs_in_targetweb เลย
    img_url = img['src'] #แยกทุกอย่างในแท็ก <img> ออก ให้เหลือแต่ไส้ในที่เราต้องการ ซึ่งคือ src มันมี image url อยู่
    if 'png' in img_url: png.append(img_url) #แยก png เข้า list กล่องชื่อ png
    elif 'jpg' in img_url: jpg.append(img_url) #แยก jpg เข้า list กล่องชื่อ jpg
    elif 'webp' in img_url: webp.append(img_url) #แยก webp เข้า list กล่องชื่อ webp
    else: pass





# ระบุว่าเว็บที่เราต้องการให้ไปดึงรูปภาพคือเว็บอะไร /// input ของ user
# ค้นหารูปภาพที่เราต้องการจากเว็บที่เราใส่ไป /// หน้าที่ bs4
# download รูปภาพ /// img_data = requests.get(img_url).content
# ระบุว่า path ที่จะให้ download รูปไปเก็บ ไปเก็บที่ไหน /// os ชี้ path