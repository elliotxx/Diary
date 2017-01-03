#coding=gbk
import time
import datetime
def get_week_day(date):
    week_day_dict = {
    0 : '����һ',
    1 : '���ڶ�',
    2 : '������',
    3 : '������',
    4 : '������',
    5 : '������',
    6 : '������',
    }
    day = date.weekday()
    return week_day_dict[day]

def get_date():
    date = time.strftime('%Y��%m��%d��',time.localtime(time.time()))
    weekday = get_week_day(datetime.datetime.now())
    return date,weekday

def Init():
    # ��ʼ��
    date,weekday = get_date()
    try:
        f = open('Diary.txt','a+')   # ��дģʽ���ļ�
    except Exception,e:
        print '�ļ���ʧ��\n',e
    content = f.read()
    #print content

    # �жϵ����Ƿ��Ѿ�д���ռ�
    index = content.find(date)
    if index != -1:     # �Ѿ�д���ռ�
        print content[index:],
        content = ''
    else:               # ���컹ûд��
        content = '%s\t%s\t'%(date,weekday) # ����

    # ѭ��д������
    line = raw_input(content)
    while line != 'q':
        content+='%s\n'%line
        line = raw_input()
    content+='\n'

    # д���ļ�
    try:
        f.seek(0,2)     # ��λ���ļ�ĩβ
        f.write(content)
    finally:
        f.close()

def main():
    # �������
    Init()

if __name__ == "__main__":
    main()
