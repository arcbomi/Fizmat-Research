# Exploring Student Demographics at Fizmat: Analyzing Birthdates and Grades for Academic Insights

This study delves into the intricate web of Fizmat student demographics, specifically exploring the potential correlation between student names and dates of birth. The primary objective is to uncover hidden insights that may shed light on the mysterious factors influencing academic outcomes. The central research question guiding this investigation is: Is there a significant correlation between student names and dates of birth?

## Data Collection

A meticulous data collection process was employed, utilizing records from kundelik.kz and databases. The comprehensive dataset encompasses student names, birth dates, and grades, obtained through both illegal crawlers and manually tagged gender information. Python serves as the analytical tool, employing statistical methods and visualization techniques to discern potential trends or correlations within birth date clusters and academic performance across different grades.

## Analysis and Observations

Upon thorough analysis of Fizmat student data, intriguing patterns have surfaced, detailed extensively in the full paper. Initial observations hint at a plausible correlation between birth date clusters and student outcomes. The inclusion of manually labeled gender information contributes to a more comprehensive understanding of these cryptic factors.

## Conclusion

The conclusion of the study presents the observed facts derived from the data analysis without interpretation. The results summarize significant correlations or their absence, providing a basis for future research and discussion. The inclusion of gender information increases the depth of understanding of correlations and provides a nuanced perspective. The purpose is to present original findings transparently, providing space for further exploration and interpretation by researchers, educators, and policymakers.

# Introduction
We will mainly do something like analysis and predictions.

 1. List item
 2. List item

# Methods
Here we will show how we obtain the data and how to process it
## How we obtained the data
The data we mainly obtain from kundelik.kz , As you see I will show our acquisition method below.
*Please use this command to install the python package first*

python -m pip install --upgrade pip
pip install urllib3
pip install requests
pip install beautifulsoup4
pip install openpyxl
pip install matplotlib
pip install natsort
pip install scikit-learn


It is a code for downloading a file：


import os
import threading
import requests
from urllib.parse import urlparse, parse_qs

def download_url(url, output_folder, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            file_name = query_params.get('user', [])[0] + ".html"
            file_path = os.path.join(output_folder, file_name)
            filename = file_path
            with open(filename, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def main():
    input_file = r'C:\Users\your_path\output.txt' #link for download
    output_folder = r'C:\Users\your_path\data'
    os.makedirs(output_folder, exist_ok=True)

    headers = {
        #'User-Agent': f'Mozilla/5.0 ... Firefox/113.0',
        #'Cookie': f'sst=4b8d91....wTKxATk%3D',
    }

    with open(input_file, 'r') as file:
        urls = file.read().splitlines()

    num_threads = 16
    threads = []

    for i in range(0, len(urls), num_threads):
        thread_batch = urls[i:i + num_threads]
        for url in thread_batch:
            thread = threading.Thread(target=download_url, args=(url, output_folder, headers))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()



This code is used to process downloaded files and add them to excel for storage：


import os
import glob
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook
from urllib.parse import urlparse, parse_qs

html_folder_path = r'C:\Users\your_path\data'
excel_save_path = r'C:\Users\your_path\all.xlsx'
months = [
    'қаңтар', 'ақпан', 'наурыз', 'сәуір', 'мамыр', 'маусым',
    'шілде', 'тамыз', 'қыркүйек', 'қазан', 'қараша', 'желтоқсан'
]

def remove_200(input_string):
    index_200 = input_string.find("200")
    if index_200 != -1:
        result_string = input_string[:index_200]
        return result_string
    else:
        return input_string
    
wb = Workbook()
ws = wb.active

html_files = glob.glob(os.path.join(html_folder_path, '*.html'))

for html_file in html_files:
    number = re.search(r'\d+', html_file).group()

    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        name_element = soup.find('a', {'title': 'Пайдаланушы парақшасына жаңарту'})
        birthday_element = soup.find('dd', {'class': 'noMargin'})

        parts = soup.find('dd').get_text(strip=True).split(',')
        if len(parts) > 1:
            grade = re.search(r'\(([^)]*)\)', str(parts[1])).group(1).replace('-', '')
        else:
            grade = re.search(r'\(([^)]*)\)', str(parts[0])).group(1).replace('-', '')

        if name_element:
            userid = name_element.get_text(strip=True)
        else:
            userid = ""
        if birthday_element:
            birthday = remove_200(birthday_element.get_text(strip=True))
            if "жыл" in birthday:
                birthday = ""
            if len(birthday.split()) == 2:
                day, month_name = birthday.split()
                day = int(day)
                month_number = months.index(month_name) + 1
                birthday = f"{month_number:02d}-{day:02d}"
        else:
            birthday = ""
   
        if len(birthday) > 1 and len(userid) > 1 and len(grade) > 1:
            ws.append([number, userid, grade, birthday])

wb.save(excel_save_path)


This is all the process used for us to download and process the data.
## further analysis




import  pandas  as  pd
excel_file_path  =  r'D:\desktop\brithdayWeb\data\all.xlsx'
df  =  pd.read_excel(excel_file_path)
student_names  =  df.iloc[:, 1]
class_names  =  df.iloc[:, 2]



import  pandas  as  pd

import  matplotlib.pyplot  as  plt

from  natsort  import  natsorted

  

# 更新Excel文件路径

excel_file_path  =  r'D:\desktop\brithdayWeb\data\all.xlsx'

  

# 使用pandas的read_excel函数读取Excel文件

df  =  pd.read_excel(excel_file_path)

  

# 读取学生名字和班级的数据

student_names  =  df.iloc[:, 1]

class_names  =  df.iloc[:, 2]

  

# 将学生名字和班级数据合并为一个DataFrame

data  =  pd.DataFrame({'Student Name': student_names, 'Class Name': class_names})

  

# 使用value_counts方法统计每个班级的学生数量，按班级名称进行自然排序

class_counts  =  data['Class Name'].value_counts().reindex(natsorted(data['Class Name'].unique()))

  

# 绘制排序后的条形图

class_counts.plot(kind='bar', rot=0, color='skyblue')

plt.xlabel('Class Name')

plt.ylabel('Number of Students')

plt.title('Number of Students in Each Class (Natural Sort)')

plt.show()
