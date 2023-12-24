import os
import threading
import requests
from urllib.parse import urlparse, parse_qs
def download_url(url, output_folder, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # 获取文件名
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            file_name = query_params.get('user', [])[0]+".html"
            file_path = os.path.join(output_folder, file_name)
            filename = file_path
            # 保存文件
            with open(filename, 'wb') as file:
                file.write(response.content)
            #print(f"Downloaded {url} to {filename}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def main():
    input_file = r'C:\Users\dm-windows\Desktop\brithdayWeb\output.txt'
    output_folder = r'C:\Users\dm-windows\Desktop\brithdayWeb\data'

    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 设置请求头
    headers = {
        'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Cookie': f'sst=4b8d914c-cfd8-4802-880c-828f70d3004e%7C27.11.2023%2009%3A45%3A46; Dnevnik_localization=kk-KZ; a_r_p_i=12.2; sst=4b8d914c-cfd8-4802-880c-828f70d3004e|27.11.2023 14:29:15; t0=1000004956244; t1=; t2=; curschool=1000004956244; QundelikAuth_a=btZNa77EAiZid2f7TuvL6qNRU35yQGUcZ4q5joMZArnp5xt%2BW9P1P7zBq9r1ehBip6U8td8HTD0xp21B5fIVMQCtisS%2FevgoN097vNK8QzVOyucvTlHgDp4J3%2FQMYZiFWhC99YLV%2BiXsfQLmVFPUAJME%2FX4KfgQjW%2FZGVF2gVHQySh0ySRb4QaMSUfRsn2kEc6GXQoIFaXQCJL5E9arAwTKxATk%3D',
    }

    # 读取链接列表
    with open(input_file, 'r') as file:
        urls = file.read().splitlines()

    # 设置线程数
    num_threads = 16

    # 创建线程池
    threads = []

    # 启动线程
    for i in range(0, len(urls), num_threads):
        thread_batch = urls[i:i + num_threads]
        for url in thread_batch:
            thread = threading.Thread(target=download_url, args=(url, output_folder, headers))
            threads.append(thread)
            thread.start()

        # 等待所有线程完成
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()
