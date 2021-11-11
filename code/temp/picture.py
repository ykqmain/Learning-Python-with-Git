import os
import shutil
import uuid

#import pyqt

import requests
from bs4 import BeautifulSoup

content_type = {
    'application/x-jpg': '.jpg',
    'application/x-jpeg': '.jpeg',
    'application/x-png': '.png',
    'application/x-gif': '.gif',
    'image/jpg': '.jpg',
    'image/jpeg': '.jpeg',
    'image/png': '.png',
    'image/gif': '.gif'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


def main(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    img_tags = soup.findAll('img')
    img_tags_src = list(filter(lambda item: 'src' in item.attrs, img_tags))
    img_tags_src = [('' if item.attrs['src'].__contains__('http')else url) + item.attrs['src'] for item in img_tags_src]

    base_path = os.getcwd() + '/' + 'pytemp' + '/'
    if not os.path.exists(base_path) :
        os.mkdir(base_path)  #创建文件夹
    
    for item in img_tags_src:
        print(item)
        r_img = requests.get(item, stream=True)
        img_type = content_type.get(r_img.headers['Content-Type'])
        image_name = uuid.uuid1()

        image_path = '{path}/{name}{type}'.format(path=base_path, name=image_name, type=img_type)
        with open(image_path, 'wb') as out_file:
            shutil.copyfileobj(r_img.raw, out_file)


if __name__ == '__main__':
    main('https://bcy.net/coser/toppost100')
