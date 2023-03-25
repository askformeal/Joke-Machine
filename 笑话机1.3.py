#1.x版都没有图形界面
import sys

def end(): #出现错误时，用户可以输入exit来退出程序
    while True:
        if input() == 'exit':
            sys.exit()
#导入需要的库
try:
    import urllib
except ModuleNotFoundError:
    print("错误：您还未安装'urllib'库")
    end()
try:
    import requests
except ModuleNotFoundError:
    print("错误：您还未安装'requests'库")
    end()

#显示版本
VERSION = '1.3'
print(f"笑话机{VERSION}版 所有笑话来源于网络，仅作娱乐用途\n")


def get_joke(msg): #从青云客机器人的API获取信息
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    try:
        html = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("无法连接到互联网")
        end()
    return str(html.json()["content"])

n = input('要收集多少个笑话？ ')

#检查用户输入是否符合格式
if '.' in n:
    print('请输入一个整数')
    end()
try:
    n = int(n)
except ValueError:
    print('请输入一个数字')
    end()
if n < 1:
    print('请输入一个正数')
    end()
#主函数
def main():
    for i in range(n):
        joke = get_joke('讲个笑话').replace('{br}', '\n') 
        #^^^ 读取到的数据中换行符用{br}表示，所有要替换一下 ^^^
        print(f"{i + 1}. ", end='')
        print(f'{joke[2:-19]}\n')
        #^^^头部和尾部有一些无用的信息，所以要“掐头去尾”^^^
    print('收集完毕') 
    end()

main()