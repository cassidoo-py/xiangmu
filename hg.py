# encoding:utf-8
from turtle import *
import time
import PySimpleGUI as sg  # 弹框制作模块


def draw_count_down(i):  # 倒数
    bgcolor('black')
    speed(0)
    up()
    goto(-50, -100)
    color('white')
    write(i, align="center", font=('Times New Roman', 200, 'bold'))
    time.sleep(1)


def draw_moon():  # 画月亮
    bgcolor('#093FB7')
    color('#F4EE00', '#F4EE00')
    begin_fill()
    speed(2)
    up()
    goto(0, -300)
    down()
    circle(300)
    end_fill()


def draw_people():  # 画小人
    up()
    fillcolor()
    begin_fill()
    color('black', 'white')
    goto(-300, 50)  # 脖子坐标
    down()
    circle(75)  # 半径为75的脑袋
    end_fill()
    right(90)
    forward(175)  # 身体的长度175像素
    right(45)
    forward(100)  # 腿长100像素
    up()
    goto(-300, -120)  # 画另一条腿
    down()
    left(90)
    forward(100)
    up()
    goto(-300, -5)  # 手臂坐标
    down()
    left(45)
    forward(100)  # 第一只手臂长度
    left(45)
    forward(67)  # 手掌长度
    up()
    goto(-300, -40)  # 第二只手臂坐标
    down()
    right(45)
    forward(100)  # 第二只手臂长度
    right(45)
    forward(67)
    up()
    goto(-330, 155)  # 第一只眼睛起始坐标
    down()
    right(45)
    forward(50)  # 眼睛长度为50
    up()
    goto(-270, 155)  # 第二只眼睛起始坐标
    down()
    forward(50)
    up()
    pencolor('#F39F79')
    goto(-340, 100)  # 红脸蛋第一只眼
    seth(0)
    down()
    backward(40)
    up()
    goto(-260, 100)  # 红脸蛋第二只眼
    down()
    forward(40)
    time.sleep(1)


def draw_heart(size):  # 画爱心
    color('red', 'pink')
    down()
    setheading(150)
    begin_fill()
    forward(size)
    circle(size * -3.745, 45)
    circle(size * -1.431, 165)
    left(120)
    circle(size * -1.431, 165)
    circle(size * -3.745, 45)
    forward(size)
    end_fill()


def send_heart():  # 发射爱心
    up()
    goto(-50, -22)
    draw_heart(14)
    up()
    goto(120, -22)
    draw_heart(25)
    penup()
    goto(305, -22)
    draw_heart(43)


def wr_character():
    up()
    goto(-50, -200)
    pencolor('black')
    write('中', font=('幼圆', 60, 'bold'))
    up()
    goto(50, -200)
    write('秋', font=('幼圆', 60, 'bold'))
    up()
    goto(150, -200)
    write('快', font=('幼圆', 60, 'bold'))
    up()
    goto(250, -200)
    write('乐', font=('幼圆', 60, 'bold'))


def draw_pupu():  # 画便便
    up()
    shapesize(10, 2)
    speed(2)
    fillcolor()
    color('#805140', '#805140')
    begin_fill()
    goto(-50, -20)
    down()
    circle(20)
    end_fill()
    begin_fill()
    up()
    goto(-50, -80)
    down()
    circle(40)
    end_fill()
    begin_fill()
    up()
    goto(10, -110)
    seth(90)
    down()
    circle(60, 180)
    seth(0)
    forward(120)
    end_fill()


def setup(param, param1):
    pass


def present_good():  # 认为我是好人送的礼物
    setup(1000, 700)
    pensize(10)
    hideturtle()

    numbers = [5, 4, 3, 2, 1]  # 进行倒数
    for i in numbers:
        draw_count_down(i)
        undo()
    draw_moon()
    draw_people()
    send_heart()
    wr_character()
    done()


def present_bad():  # 认为我不好送的礼物
    setup(1000, 700)
    pensize(10)
    hideturtle()
    numbers = [5, 4, 3, 2, 1]  # 进行倒数
    for i in numbers:
        draw_count_down(i)
        undo()
    draw_moon()
    draw_people()
    draw_pupu()
    wr_character()
    done()


layout = [  # 弹框内容设计
    [sg.Text('请输入你的名字：')], [sg.Input()],
    [sg.Text('请回答下面这个问题哦！')],
    [sg.Text('xxx是个大好人是吗？')],
    [sg.Button('是的是的')], [sg.Button('不是')]
]

sg.popup('你好呀！我是你的好朋友xxx为你定制的中秋节礼物⭐', '请按OK键继续')  # 这是一个简易弹框
time.sleep(1)
window = sg.Window('中秋礼物', layout)
event, value = window.read()
window.close()
if event == '是的是的':
    sg.popup(f'{value[0]}请按OK键接收xxx的中秋礼物！')  # 这是一个简易弹框  #这里的value[0]，是因为value返回内容为字典
    time.sleep(1)
    present_good()
else:
    sg.popup(f'{value[0]}竟然对xxx有意见，你还想要礼物！！', '但是xxx是个大度的人，送你礼物吧', '请按OK键接收xxx的中秋礼物！')
    present_bad()
