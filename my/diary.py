# coding=utf-8
import os
import re

import calendar
import datetime
from bs4 import BeautifulSoup
import urllib
import re
import pyperclip


# world操作
# 传入三个参数, 旧字符串, 新字符串, 文件对象7 8
def replace_text(old_text, new_text, file):
    # 遍历文件对象  33400    32647
    for f in file.paragraphs:
        # 如果 旧字符串 在 某个段落 中
        if old_text in f.text:
            print("替换前:", f.text)
            # 将段落存入 inline
            inline = f.runs
            # 遍历 段落 生成 i
            for i in inline:
                # 如果 旧字符串 在 i 中
                if old_text in i.text:
                    # 替换 i.text 内文本资源
                    text = i.text.replace(old_text, new_text)
                    i.text = text
            print("替换后===>", f.text)


def getday():
    allday = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]
    newday = datetime.datetime.now().day
    finallyday = str(allday - newday)
    return finallyday


def getweather():
    # 获取天气信息
    # base_url = "http://www.weather.com.cn/weather1d/101010100.shtml"
    base_url = "https://www.tianqi.com/beijing/"

    url = base_url

    html = urllib.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    # print(html)
    # 天气
    wea = soup.find('dd', class_='weather')
    kongqi=soup.find('dd', class_='kongqi')
    sstr=kongqi.h5.text+kongqi.h6.text

    kongqistr=sstr.replace(u'空气质量：', '')

    weather = u"天气：" + wea.span.text + "    " + kongqistr

    return weather


if __name__ == '__main__':
    # 三个参数: 旧的字符串, 新的字符串, 文件对象
    weather = getweather()

    day = u'本月余额' + getday() + u'天'

    # replace_text('天气', weather, file)
    # replace_text('本月余额', day, file)
    # file.save(docx_file_name1)

    str = weather + u'\n' + day
    pyperclip.copy(str)

    print(u"成功\n"+str)
    # print(docx_file_name1, "替换成功"+str)
# main()
