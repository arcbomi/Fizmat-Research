import os
import glob
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook
from urllib.parse import urlparse, parse_qs


# 设置文件夹路径和Excel文件保存路径
html_folder_path = r'C:\Users\dm-windows\Desktop\brithdayWeb\data'
excel_save_path = r'C:\Users\dm-windows\Desktop\brithdayWeb\all.xlsx'
months = [
    'қаңтар', 'ақпан', 'наурыз', 'сәуір', 'мамыр', 'маусым',
    'шілде', 'тамыз', 'қыркүйек', 'қазан', 'қараша', 'желтоқсан'
]

def remove_200(input_string):
    index_200 = input_string.find("200")
    if index_200 != -1:
        # 找到"200"，删除它以及它后面的部分
        result_string = input_string[:index_200]
        return result_string
    else:
        # 没有找到"200"
        return input_string
    
# 创建一个新的Excel工作簿和工作表
wb = Workbook()
ws = wb.active


# 获取所有HTML文件路径
html_files = glob.glob(os.path.join(html_folder_path, '*.html'))

# 遍历每个HTML文件
for html_file in html_files:
    number = re.search(r'\d+', html_file).group()

    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        name_element = soup.find('a', {'title': 'Пайдаланушы парақшасына жаңарту'})
        birthday_element = soup.find('dd', {'class': 'noMargin'})

        parts = soup.find('dd').get_text(strip=True).split(',')
        if len(parts) > 1:
            grade= re.search(r'\(([^)]*)\)', str(parts[1])).group(1).replace('-', '')
        else:
            grade= re.search(r'\(([^)]*)\)', str(parts[0])).group(1).replace('-', '')

        #print(number)
        if(name_element):
            userid = name_element.get_text(strip=True)
        else:
            userid=""
        if(birthday_element):
            birthday = remove_200(birthday_element.get_text(strip=True))
            if("жыл" in birthday):
                birthday=""
            if len(birthday.split()) == 2:
                day, month_name = birthday.split()
                day=int(day)
                month_number = months.index(month_name) + 1
                birthday = f"{month_number:02d}-{day:02d}"
        else:
            birthday=""
   
        #print(number,userid, grade, birthday)
        if(len(birthday)>1 and len(userid)>1 and len(grade)>1):
            ws.append([number, userid, grade, birthday])

# 保存Excel文件
wb.save(excel_save_path)
