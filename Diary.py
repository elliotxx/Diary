#coding=gbk
import time
import datetime
def get_week_day(date):
    week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]

def get_date():
    date = time.strftime('%Y年%m月%d日',time.localtime(time.time()))
    weekday = get_week_day(datetime.datetime.now())
    return date,weekday

def Init():
    # 初始化
    date,weekday = get_date()
    try:
        f = open('Diary.txt','a+')   # 读写模式打开文件
    except Exception,e:
        print '文件打开失败\n',e
    content = f.read()
    #print content

    # 判断当天是否已经写过日记
    index = content.find(date)
    if index != -1:     # 已经写过日记
        print content[index:],
        content = ''
    else:               # 今天还没写过
        content = '%s\t%s\t'%(date,weekday) # 内容

    # 循环写入内容
    line = raw_input(content)
    while line != 'q':
        content+='%s\n'%line
        line = raw_input()
    content+='\n'

    # 写入文件
    try:
        f.seek(0,2)     # 定位在文件末尾
        f.write(content)
    finally:
        f.close()

def main():
    # 启动入口
    Init()

if __name__ == "__main__":
    main()
