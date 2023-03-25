#2.x版开始有图形界面了
#图像界面之基于Tkinter的
from tkinter import *
import requests

root = Tk()
root.geometry('500x400')#设置窗口大小

VERSION = 2.1
root.title(f'笑话机{VERSION},由青云客机器人提供支持')

joke_count = 1 #笑话的编号
RETURN_CUT = 38 #设置在每行达到多少个字符时换行

def close_window(*args): #关闭窗口函数
    root.destroy()

def get_joke(*args): #获取笑话的函数
    global joke_count

    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=讲个笑话'
    #青云客机器人的API
    joke = requests.get(url)
    joke = str(joke.json()["content"])

    joke = joke.replace('{br}', '\n')
    #^^^ 读取到的数据中换行符用{br}表示，所有要替换一下 ^^^
    joke = joke[2:-19]
    #^^^头部和尾部有一些无用的信息，所以要“掐头去尾”^^^
    joke = f"{joke_count}. {joke}\n"
    #添加编号

    jokes = joke.split(sep='\n')
    #^^^将获取的信息分装到列表中，每个元素对应一行^^^
    for k in jokes:
        if len(k) <= RETURN_CUT:#如果这行小于RETURN_CUT，直接输出
            show.insert(END,k)
        else:
            while len(k) > RETURN_CUT: #否则每RETURN_CUT个字符换一行
                show.insert(END,k[0:RETURN_CUT+1])
                k = k[RETURN_CUT+1:]
            if k: #如果还有剩余的，也要加入进去
                show.insert(END,k)
    joke_count+=1 #更新编号


root.bind('<Return>',get_joke) #绑定按键，在按回车是调用get_joke
root.bind('<Escape>',close_window)

Button(text='收集一个笑话',command=get_joke).pack(side=TOP,fill=BOTH)
#^^^收集笑话的按钮^^^
Button(text='关闭窗口',command=close_window).pack(side=BOTTOM,fill=X)
#^^^关闭窗口的按钮^^^

bar = Scrollbar(width=20)#滚动条
bar.pack(side=RIGHT,fill=Y)

show = Listbox(height=20,yscrollcommand=bar.set)#显示笑话的窗口
show.pack(side=BOTTOM,fill=BOTH)

bar.config(command=show.yview)

root.mainloop()