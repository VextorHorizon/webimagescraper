import os
import requests
from bs4 import BeautifulSoup 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str)
args = parser.parse_args()

user_input = args.url #url ของเว็บ 
url = requests.get(user_input).content #ขอ content(เปรียบเทียบเป็นกล่องพัสดุ content คือเอาแค่ของในพัสดุ ตัดชื่อผู้ส่งผู้รับที่อยู่บ้านเบอร์โทร)
html_content = BeautifulSoup(url, "html.parser") #กำหนดกฎที่เราจะอ่านไอเจ้านี่ให้เป็นกฎของ html

imgs_in_targetweb = html_content.find_all('img') #หา tags img ในตัวของ content ที่ได้มา
for image in imgs_in_targetweb:
    image_url = image['src']



# ระบุว่าเว็บที่เราต้องการให้ไปดึงรูปภาพคือเว็บอะไร /// input ของ user
# ค้นหารูปภาพที่เราต้องการจากเว็บที่เราใส่ไป /// หน้าที่ bs4
# download รูปภาพ /// img_data = requests.get(img_url).content
# ระบุว่า path ที่จะให้ download รูปไปเก็บ ไปเก็บที่ไหน /// os ชี้ path