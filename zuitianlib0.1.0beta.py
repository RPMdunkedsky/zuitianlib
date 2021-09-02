from os import*
from time import*

from turtle import *
from random import *
from math import *

import pygame,time,emoji,sys,pygame,random
import sys
import os
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel,QSpacerItem, QSizePolicy, QPushButton, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QGridLayout
class others():
    def t(a):
        time.sleep(a)
    def o():
        os.system("clear")
    def fun(line):
        for i in range(len(line)):
            print("\r"+line[0:i+1],end="")
            t(0.1)
        print()
    def stop():
        t(1.5)
        o()
        t(1.5)
    def daimazhixingqi():

        while True:
            print("输入退出即可退出程序")
            print("---------------------------------------------")
            cz = input('请输入要执行的语句:')
            if cz == "退出":
                print("谢谢使用")
                print("---------------------------------------------")
                sys.exit(0)
            exec(cz)
            print("---------------------------------------------")
            print("回车进入下一个")
            system("read anykey")
            system("clear")


class jianli():

    def dtdklinbanmeng():
        print('''林半梦，现为醉天工作室室长兼MS工作室Python部成员。
              经历：
                   2020年2月10日，创建一世尘缘醉（灵感源于本人一句词：杀伐一世，醉尘缘。）
                   2020年2月11日，招收到5位成员。分别是：黯星神（QQ未知，职位副室长）北船余音（梦时副室长开多室籍，职位C++部部长）...（只记得这俩了555）
                   2020年2月11日，与KID（现魔幻）室长产生矛盾，遂开始找合作收旗下。
                   2020年2月15日左右，与全员恶人（分部）谈判，其愿意送出副室长来和谈。副室长有个妹妹，他把妹妹也带过来了（现在还在）
                   2020年3月3日，被PSF收旗下。2020年3月15日左右，与PSF创始人等创立SBS
                   2020年5月，在抗击彗星中表现卓著，被梦时副室长提拔。
                   同年6月，收腾易（编程猫）全员恶人（卡哒）为旗下。
                   同年7月，脱离梦时。''')


    def dtdkmonstercatquxuyangquxuing():
        print("曲栩阳、曲栩婷，关系未知，现为Monstercat双星（曲栩阳是室长，曲栩婷是副室长")
    def msstudio():
        print("2020年6月20日，与黄嘉梁，徐付成共同创建MS工作室，前身HPLO。6月23日，报名参加编程社区夏季联赛。目前，MS工作室经营妥善，挺好的。")
    def huzhaohangmsstudio():
        print('''姓名：胡朝航
工作室室籍：MS工作室
经历：2019年5月10日，创建环球工作室，同年6月20日，环球工作室解散。其退出编程社区8个月。2020年3月3日，加入SEVA工作室，同年3月10日，因被时任SEVA工作室室长怀疑是间谍（其实不是），而退出。2020年4月10日，创建德音工作室，并于同日成为PEN果公司旗下工作室，2020年5月20日，解散德音工作室。2020年5月21日，创建HPLO工作室，并于2020年5月25日，成为星斩工作室旗下，2020年6月10日，因与星斩工作室室长三千星斩产生矛盾，退出星斩工作室，并于2020年6月15日解散HPLO工作室。2020年6月20日，创建MS工作室（成员主要是原HPLO工作室成员），2020年6月25日，报名参加战队PK夏季联赛。
现任工作室职位：MS工作室室长''')


    def dunkedskystudio():
        print("醉天工作室，前身一世尘缘醉，于2020年2月10日创建。室长林半梦。于2020年6月底达到210人。")
    def huzhaohangmsstudio():
    print('''姓名：胡朝航
工作室室籍：MS工作室
经历：2019年5月10日，创建环球工作室，同年6月20日，环球工作室解散。其退出编程社区8个月。2020年3月3日，加入SEVA工作室，同年3月10日，因被时任SEVA工作室室长怀疑是间谍（其实不是），而退出。2020年4月10日，创建德音工作室，并于同日成为PEN果公司旗下工作室，2020年5月20日，解散德音工作室。2020年5月21日，创建HPLO工作室，并于2020年5月25日，成为星斩工作室旗下，2020年6月10日，因与星斩工作室室长三千星斩产生矛盾，退出星斩工作室，并于2020年6月15日解散HPLO工作室。2020年6月20日，创建MS工作室（成员主要是原HPLO工作室成员），2020年6月25日，报名参加战队PK夏季联赛。
现任工作室职位：MS工作室室长''')



class dkprint():
    def colorprint(a):
        for x in range(len(a)):
            if a[x]=="1":
                print("\033[41m ",end="")
            elif a[x]=="2":
                print("\033[42m ",end="")
            elif a[x]=="3":
                print("\033[43m ",end="")
            elif a[x]=="4":
                print("\033[44m ",end="")
            elif a[x]=="5":
                print("\033[45m ",end="")
            elif a[x]=="6":
                print("\033[46m ",end="")
            elif a[x]=="7":
                print("\033[47m ",end="")
            elif a[x]=="8":
                print("\033[48m ",end="")
            elif a[x]=="9":
                print("\033[49m ",end="")
            elif a[x]=="0":
                print("\033[40m ",end="")
            else:
                print(a[x],end="")
        print("\033[0m")
    def shanda(a):
        p = len(a)
        for i in range(p):
            print(a[i])
            os.system("clear")
            time.sleep(0.1)




class jisuan():
    def quyu(a, b):
        p = a % b
        return p
    def add(x, y):
        p = x+y
        return p


    def minus(x, y):
        p = x-y
        return p
    def make(x, y):
        p = x*y
        return p


    def made(x, y):
        p = x/y
        return p
    def mu(x,y):
        p = x**y
        return p
    def cifang(x,y):
        p = x** y
        return p
    def zhengchu(x,y):
        p = x//y
        return p
    def quzhengchu(x,y):
        p = x//y
        return p




class webpy():
    def tree(n=12, l=100, r1=200, g1=100, b1=50):
        # def tree(n, l,r1,g1,b1):
        colormode(255)
        pd()  # 下笔
        # 阴影效果
        t = int((cos(radians(heading() + 45)) / 8 + 0.25)*255)
        pencolor(0, 0, 0)
        pensize(n / 3)
        forward(l)  # 画树枝

        if n > 0:
            b = random() * 15 + 10  # 右分支偏转角度
            c = random() * 15 + 10  # 左分支偏转角度
            d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
            # 右转一定角度，画右分支
            right(b)
            tree(n - 1, d, r1, g1, b1)
            # 左转一定角度，画左分支
            left(b + c)
            tree(n - 1, d, r1, g1, b1)

            # 转回来
            right(c)
        else:
            # 画叶子
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            #pencolor(n*r, n * g, n * b)
            pencolor(r1, g1, b1)
            circle(3)
            left(90)

            # 添加0.3倍的飘落叶子
            if (random() > 0.7):
                pu()
                # 飘落
                t = heading()
                an = -40 + random() * 40
                setheading(an)
                dis = int(800 * random() * 0.5 + 400 * random()
                          * 0.3 + 200 * random() * 0.2)
                forward(dis)
                setheading(t)

                # 画叶子
                pd()
                right(90)
                n = cos(radians(heading() - 45)) / 4 + 0.5
                #pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
                #pencolor(n *r* 0.5 + 0.5,(1 + n) *g/2,(1 + n) *b/2)
                r2 = r1+randint(10, 50)
                g2 = g1+randint(10, 50)
                b2 = b1+randint(10, 50)
                if r2 > 255:
                    r2 = 255
                elif g2 > 255:
                    g2 = 255
                elif b2 > 255:
                    b2 = 255
                pencolor(r2, g2, b2)
                circle(2)
                left(90)
                pu()

                # 返回
                t = heading()
                setheading(an)
                backward(dis)
                setheading(t)

        pu()
        backward(l)  # 退回


    def bg(color="grey", speednum="s"):
        screensize(1000, 1000, color)
        bgcolor(0.5, 0.5, 0.5)  # 背景色
        ht()  # 隐藏turtle
        if speednum != "s":
            speed(speednum)  # 速度，1-10渐进，0最快
        else:
            tracer(0, 0)
        pu()  # 抬笔
        backward(100)
        left(90)  # 左转90度
        pu()  # 抬笔
        backward(300)  # 后退300


    def w(txt):
        penup()
        goto(-200, -300)
        color(0, 0, 0)
        write(txt, font=["宋体", 50, "bold"])







class pygame():
    x = 100
    y = 100
    speedx = 0.5
    speedy = 0.5
    landpic = "bg"+str(random.randint(1, 5))+".jpg"
    # 第1个参数为display,第2个参数为图片名称，第3参数为运动方式(1-3)


    def look(screen, picName, way=1):
        global x, y, speedx, speedy, landpic
        picName = picName+".png"
        myImg = pygame.image.load(picName)
        myImg2 = pygame.transform.scale(myImg, (200, 200))
        # 加载背景
        # bgImg=pygame.image.load(landpic)

        imgRect = myImg.get_rect()

        if way == 1:
            if x >= screen.get_size()[0]-120 or x <= 0:
                speedx = -speedx
            elif y >= screen.get_size()[1]-120 or y <= 0:
                speedy = -speedy
            x = x+speedx
            y = y+speedy
        elif way == 2:
            if x >= screen.get_size()[0]-120 or x <= 0:
                speedx = -speedx
                y = y+20
            elif y >= screen.get_size()[1]-120 or y <= 0:
                y = 0
            x = x+speedx
        elif way == 3:
            if x >= screen.get_size()[0]-120 or x <= 0:
                x = 0
            elif y >= screen.get_size()[1]-120 or y <= 0:
                speedy = -speedy
                x = x+20
            y = y+speedy
        # screen.blit(bgImg,(0,0))
        screen.blit(myImg2, (x, y))


    def bulid(screen, imgName, x, y):
        img = pygame.image.load(imgName)
        img2 = pygame.transform.scale(img, (200, 200))
        screen.blit(img2, (x, y))





    def bg(screen,imgload):
        img = pygame.image.load(imgload)
        img2 = pygame.transform.scale(img, (800, 600))
        screen.blit(img2, (0, 0))


    def quit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def playshortmusic(a):
        music1 = pygame.mixer.Sound(a)
        music1.play()
    def playlongmusic(a):
        pygame.mixer.music.load(a)
        pygame.mixer.music.play(-1)
        
    def drive(mycard):
        pygame.init()
        back = False #是否返航
        timeTask = random.randint(10, 20) #任务时间
        print("任务时间:", timeTask)

        screen = pygame.display.set_mode((700, 400))
        pygame.display.set_caption("时空飞船")

        bg = pygame.image.load("bg.png")
        win = pygame.image.load("成功.png")
        win = pygame.transform.scale(win, (300, 300))
        fail = pygame.image.load("失败.png")
        fail = pygame.transform.scale(fail, (300, 300))

        a1 = pygame.image.load("1.png")
        a1 = pygame.transform.scale(a1, (264, 150))
        a2 = pygame.image.load("2.png")
        a2 = pygame.transform.scale(a2, (264, 150))
        a3 = pygame.image.load("3.png")
        a3 = pygame.transform.scale(a3, (264, 150))
        b1 = pygame.image.load("5.png")
        b1 = pygame.transform.scale(b1,(88,140))
        b2 = pygame.image.load("6.png")
        b2 = pygame.transform.scale(b2, (88, 140))
        list1 = [a1, a2, a3]
        list2 = [b1, b2]

        myFont = pygame.font.SysFont("heittf", 21)
        myFont1 = pygame.font.SysFont("heittf", 30)
        coinSound = pygame.mixer.Sound("金币.wav")
        winSound = pygame.mixer.Sound("胜利.wav")
        failSound = pygame.mixer.Sound("失败.wav")
        pygame.mixer.music.load("bg.mp3")
        pygame.mixer.music.play(-1)
        t1 = time.time()
        wealth = 0
        a = 0
        b = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        wealth = wealth+1
                        coinSound.play()
                        print(wealth)
                    elif event.key == pygame.K_RETURN:
                        back = True
            #背景显示
            screen.fill((200,200,200))
            screen.blit(bg, (0, 0))
            # 经过的时间
            t2 = time.time()
            t = t2 - t1
            # 宇航员信息
            text1 = myFont.render("ID: " + str(mycard["ID"]), True, (255, 255, 255))
            screen.blit(text1, (90, 110))
            text1 = myFont.render("age: "+str(mycard["age"]),True,(255, 255, 255))
            screen.blit(text1,(90, 140))
            text1 = myFont.render("weight: "+str(mycard["weight"]),True,(255, 255, 255))
            screen.blit(text1,(90, 170))
            text1 = myFont.render("height: " + str(mycard["height"]), True, (255, 255, 255))
            screen.blit(text1, (90, 200))
            text1 = myFont.render("IQ: " + str(mycard["IQ"]), True, (255, 255, 255))
            screen.blit(text1, (90, 230))
            #财富值显示
            weatherText = myFont1.render(str(wealth), True, (255, 255, 255))
            screen.blit(weatherText, (530, 28))
            #时间显示
            timeText = myFont1.render(str(int(timeTask-t)), True, (255, 255, 255))
            screen.blit(timeText, (400, 28))
            #动效
            screen.blit(list1[a], (200, 90))
            screen.blit(list2[b], (480, 90))
            a = a + 1
            b = b + 1
            if a > 2:
                a = 0
            if b > 1:
                b = 0
            time.sleep(0.3)

            if back == True or t >= timeTask:
                if wealth > timeTask:
                    winSound.play()
                    screen.blit(win, (213, 20))
                    pygame.display.update()
                    print("完成任务!获得财富:", wealth)
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()
                else:
                    failSound.play()
                    screen.blit(fail, (213, 20))
                    pygame.display.update()
                    print("耗时太长,任务失败!获得财富:", wealth)
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

            pygame.display.update()












#RPM水印
class TitleBardialog(QWidget):

	# 窗口最小化信号
	windowMinimumed = pyqtSignal()
	# 窗口最大化信号
	windowMaximumed = pyqtSignal()
	# 窗口还原信号
	windowNormaled = pyqtSignal()
	# 窗口关闭信号
	windowClosed = pyqtSignal()
	# 窗口移动
	windowMoved = pyqtSignal(QPoint)

	def __init__(self, window, state="normal", *args, **kwargs):
		self.state=state
		super(TitleBardialog, self).__init__(*args, **kwargs)
		
		self.setStyleSheet('''
		TitleBardialog {
			background-color: #c7edcc;
		}
		#buttonClose {
			border: none;
			color: black;
			background-color: #c7edcc;
		}
		#buttonClose:hover {
			color: red;
		}
		''')
		# 支持qss设置背景
		self.setAttribute(Qt.WA_StyledBackground, True)
		self.mPos = None
		self.iconSize = 20  # 图标的默认大小
		# 设置默认背景颜色,否则由于受到父窗口的影响导致透明
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(palette.Window, QColor(240, 240, 240))
		self.setPalette(palette)
		# 布局
		layout = QHBoxLayout(self, spacing=0)
		layout.setContentsMargins(0, 0, 0, 0)
		# 窗口图标
		self.iconLabel = QLabel(self)
		# self.iconLabel.setScaledContents(True)
		layout.addWidget(self.iconLabel)
		# 窗口标题
		self.titleLabel = QLabel(self,font=QFont("Microsoft Yahei",14))
		self.titleLabel.setMargin(2)
		layout.addWidget(self.titleLabel)
		# 中间伸缩条
		
		layout.addSpacerItem(QSpacerItem(
			40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
		# 利用Webdings字体来显示图标
		font = QFont('Webdings',14)
		if self.state=="normal":
			self.buttonClose = QPushButton(
				'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
			self.buttonClose.setToolTip("关闭")
			layout.addWidget(self.buttonClose)
		# 初始高度
		self.setHeight()

	def showMaximized(self):
		pass

	def setHeight(self, height=38):
		self.setFixedHeight(height)
		if self.state=="normal":
			self.buttonClose.setMinimumSize(height, height)
			self.buttonClose.setMaximumSize(height, height)

	def setTitle(self, title):
		"""设置标题"""
		
		self.titleLabel.setText(title)
		self.setToolTip(title)

	def setIcon(self, icon):
		"""设置图标"""
		self.iconLabel.setPixmap(icon.pixmap(30, 30))

	def setIconSize(self, size):
		"""设置图标大小"""
		self.iconSize = size

	def enterEvent(self, event):
		self.setCursor(Qt.ArrowCursor)
		super(TitleBardialog, self).enterEvent(event)

	def mouseDoubleClickEvent(self, event):
		pass

	def mousePressEvent(self, event):
		"""鼠标点击事件"""
		if event.button() == Qt.LeftButton:
			self.mPos = event.pos()
		event.accept()

	def mouseReleaseEvent(self, event):
		'''鼠标弹起事件'''
		self.mPos = None
		event.accept()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton and self.mPos:
			self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
		event.accept()

# 枚举左上右下以及四个定点
Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

class FramelessDialog(QDialog):

	# 四周边距
	Margins = 5

	def __init__(self, state=None, *args, **kwargs):
		self.big=False
		self.state=state
		super(FramelessDialog, self).__init__(*args, **kwargs)

		self._pressed = False
		self.Direction = None
		# 背景透明
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		# 无边框
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.MSWindowsFixedSizeDialogHint|Qt.WindowStaysOnTopHint)  # 隐藏边框
		# 鼠标跟踪
		self.setMouseTracking(True)
		# 布局
		layout = QVBoxLayout(self, spacing=0)
		# 预留边界用于实现无边框窗口调整大小
		layout.setContentsMargins(
			self.Margins, self.Margins, self.Margins, self.Margins)
		# 标题栏
		self.titleBar = TitleBardialog(self,state=self.state)
		layout.addWidget(self.titleBar)
		# 信号
		self.titleBar.windowClosed.connect(self.close)
		self.titleBar.windowMoved.connect(self.move)
		self.windowTitleChanged.connect(self.titleBar.setTitle)
		self.windowIconChanged.connect(self.titleBar.setIcon)

	def setTitleBarHeight(self, height=38):
		"""设置标题栏高度"""
		self.titleBar.setHeight(height)

	def setIconSize(self, size):
		"""设置图标的大小"""
		self.titleBar.setIconSize(size)

	def setWidget(self, widget):
		"""设置自己的控件"""
		if hasattr(self, '_widget'):
			return
		self._widget = widget
		# 设置默认背景颜色,否则由于受到父窗口的影响导致透明
		self._widget.setAutoFillBackground(True)
		palette = self._widget.palette()
		palette.setColor(palette.Window, QColor(240, 240, 240))
		self._widget.setPalette(palette)
		self._widget.installEventFilter(self)
		self.layout().addWidget(self._widget)

	def move(self, pos):
		if self.big==False:
			super(FramelessDialog, self).move(pos)

	def showMaximized(self):
		"""最大化,要去除上下左右边界,如果不去除则边框地方会有空隙"""
		self.big=True
		super(FramelessDialog, self).showMaximized()
		self.layout().setContentsMargins(0, 0, 0, 0)

	def showNormal(self):
		"""还原,要保留上下左右边界,否则没有边框无法调整"""
		self.big=False
		super(FramelessDialog, self).showNormal()
		self.layout().setContentsMargins(
			self.Margins, self.Margins, self.Margins, self.Margins)

	def eventFilter(self, obj, event):
		"""事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式"""
		if isinstance(event, QEnterEvent):
			self.setCursor(Qt.ArrowCursor)
		return super(FramelessDialog, self).eventFilter(obj, event)

	def paintEvent(self, event):
		"""由于是全透明背景窗口,重绘事件中绘制透明度为1的难以发现的边框,用于调整窗口大小"""
		super(FramelessDialog, self).paintEvent(event)
		painter = QPainter(self)
		painter.setPen(QPen(QColor(255, 255, 255, 1), 2 * self.Margins))
		painter.drawRect(self.rect())

	def mousePressEvent(self, event):
		"""鼠标点击事件"""
		super(FramelessDialog, self).mousePressEvent(event)
		if event.button() == Qt.LeftButton:
			self._mpos = event.pos()
			self._pressed = True

	def mouseReleaseEvent(self, event):
		'''鼠标弹起事件'''
		super(FramelessDialog, self).mouseReleaseEvent(event)
		self._pressed = False
		self.Direction = None

	def mouseMoveEvent(self, event):
		"""鼠标移动事件"""
		super(FramelessDialog, self).mouseMoveEvent(event)
		pos = event.pos()
		xPos, yPos = pos.x(), pos.y()
		wm, hm = self.width() - self.Margins, self.height() - self.Margins
		if self.isMaximized() or self.isFullScreen():
			self.Direction = None
			self.setCursor(Qt.ArrowCursor)
			return
		if event.buttons() == Qt.LeftButton and self._pressed:
			self._resizeWidget(pos)
			return

	def _resizeWidget(self, pos):
		if self.Direction == None:
			return
		mpos = pos - self._mpos
		xPos, yPos = mpos.x(), mpos.y()
		geometry = self.geometry()
		x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
		if self.Direction == LeftTop:  # 左上角
			if w - xPos > self.minimumWidth():
				x += xPos
				w -= xPos
			if h - yPos > self.minimumHeight():
				y += yPos
				h -= yPos
		elif self.Direction == RightBottom:  # 右下角
			if w + xPos > self.minimumWidth():
				w += xPos
				self._mpos = pos
			if h + yPos > self.minimumHeight():
				h += yPos
				self._mpos = pos
		elif self.Direction == RightTop:  # 右上角
			if h - yPos > self.minimumHeight():
				y += yPos
				h -= yPos
			if w + xPos > self.minimumWidth():
				w += xPos
				self._mpos.setX(pos.x())
		elif self.Direction == LeftBottom:  # 左下角
			if w - xPos > self.minimumWidth():
				x += xPos
				w -= xPos
			if h + yPos > self.minimumHeight():
				h += yPos
				self._mpos.setY(pos.y())
		elif self.Direction == Left:  # 左边
			if w - xPos > self.minimumWidth():
				x += xPos
				w -= xPos
			else:
				return
		elif self.Direction == Right:  # 右边
			if w + xPos > self.minimumWidth():
				w += xPos
				self._mpos = pos
			else:
				return
		elif self.Direction == Top:  # 上面
			if h - yPos > self.minimumHeight():
				y += yPos
				h -= yPos
			else:
				return
		elif self.Direction == Bottom:  # 下面
			if h + yPos > self.minimumHeight():
				h += yPos
				self._mpos = pos
			else:
				return
		self.setGeometry(x, y, w, h)

class TitleBar(QWidget):

	# 窗口最小化信号
	windowMinimumed = pyqtSignal()
	# 窗口最大化信号
	windowMaximumed = pyqtSignal()
	# 窗口还原信号
	windowNormaled = pyqtSignal()
	# 窗口关闭信号
	windowClosed = pyqtSignal()
	# 窗口移动
	windowMoved = pyqtSignal(QPoint)

	def __init__(self, window, state=None, *args, **kwargs):
		self.state=state
		super(TitleBar, self).__init__(*args, **kwargs)
		self.setToolTip("九宫格游戏")
		# 支持qss设置背景
		self.setAttribute(Qt.WA_StyledBackground, True)
		self.mPos = None
		self.iconSize = 20  # 图标的默认大小
		# 设置默认背景颜色,否则由于受到父窗口的影响导致透明
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(palette.Window, QColor(240, 240, 240))
		self.setPalette(palette)
		# 布局
		layout = QHBoxLayout(self, spacing=0)
		layout.setContentsMargins(0, 0, 0, 0)
		# 窗口图标
		self.iconLabel = QLabel(self)
		# self.iconLabel.setScaledContents(True)
		layout.addWidget(self.iconLabel)
		# 窗口标题
		self.titleLabel = QLabel(self,font=QFont("Microsoft Yahei",14))
		self.titleLabel.setMargin(2)
		self.titleLabel.setText("九宫格...")
		layout.addWidget(self.titleLabel)
		# 中间伸缩条
		layout.addSpacerItem(QSpacerItem(
			40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
		# 利用Webdings字体来显示图标
		font = QFont('Webdings',14)
		if state!="d":
			# 最小化按钮
			self.buttonMinimum = QPushButton(
				'0', self, clicked=self.windowMinimumed.emit, font=font, objectName='buttonMinimum')
			self.buttonMinimum.setToolTip("最小化")
			layout.addWidget(self.buttonMinimum)
		# 关闭按钮
		self.buttonClose = QPushButton(
			'r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
		self.buttonClose.setToolTip("关闭")
		layout.addWidget(self.buttonClose)
		# 初始高度
		self.setHeight()

	def showMaximized(self):
		if self.buttonMaximum.text() == '1':
			self.buttonMaximum.setToolTip("还原")
			# 最大化
			self.buttonMaximum.setText('2')
			self.windowMaximumed.emit()
		else:  # 还原
			self.buttonMaximum.setToolTip("最大化")
			self.buttonMaximum.setText('1')
			self.windowNormaled.emit()

	def setHeight(self, height=38):
		"""设置标题栏高度"""
		self.setMinimumHeight(height)
		
		self.setMaximumHeight(height)
		# 设置右边按钮的大小
		self.buttonMinimum.setMinimumSize(height, height)
		self.buttonMinimum.setMaximumSize(height, height)
		self.buttonClose.setMinimumSize(height, height)
		self.buttonClose.setMaximumSize(height, height)

	def setTitle(self, title):
		pass
	def setIcon(self, icon):
		"""设置图标"""
		self.iconLabel.setPixmap(icon.pixmap(30, 30))

	def setIconSize(self, size):
		"""设置图标大小"""
		self.iconSize = size

	def enterEvent(self, event):
		self.setCursor(Qt.ArrowCursor)
		super(TitleBar, self).enterEvent(event)

	def mouseDoubleClickEvent(self, event):
		pass

	def mousePressEvent(self, event):
		"""鼠标点击事件"""
		if event.button() == Qt.LeftButton:
			self.mPos = event.pos()
		event.accept()

	def mouseReleaseEvent(self, event):
		'''鼠标弹起事件'''
		self.mPos = None
		event.accept()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton and self.mPos:
			self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
		event.accept()

# 枚举左上右下以及四个定点
Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

class FramelessWindow(QWidget):

	# 四周边距
	Margins = 5

	def __init__(self, state=None, *args, **kwargs):
		self.big=False
		self.state=state
		super(FramelessWindow, self).__init__(*args, **kwargs)

		self._pressed = False
		self.Direction = None
		# 背景透明
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		# 无边框
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.MSWindowsFixedSizeDialogHint|Qt.WindowStaysOnTopHint)  # 隐藏边框
		# 鼠标跟踪
		self.setMouseTracking(True)
		# 布局
		layout = QVBoxLayout(self, spacing=0)
		# 预留边界用于实现无边框窗口调整大小
		layout.setContentsMargins(
			self.Margins, self.Margins, self.Margins, self.Margins)
		# 标题栏
		self.titleBar = TitleBar(self)
		layout.addWidget(self.titleBar)
		# 信号槽
		self.titleBar.windowMinimumed.connect(self.showMinimized)
		self.titleBar.windowMaximumed.connect(self.showMaximized)
		self.titleBar.windowNormaled.connect(self.showNormal)
		self.titleBar.windowClosed.connect(self.close)
		self.titleBar.windowMoved.connect(self.move)
		self.windowTitleChanged.connect(self.titleBar.setTitle)
		self.windowIconChanged.connect(self.titleBar.setIcon)

	def setTitleBarHeight(self, height=38):
		"""设置标题栏高度"""
		self.titleBar.setHeight(height)

	def setIconSize(self, size):
		"""设置图标的大小"""
		self.titleBar.setIconSize(size)

	def setWidget(self, widget):
		"""设置自己的控件"""
		if hasattr(self, '_widget'):
			return
		self._widget = widget
		# 设置默认背景颜色,否则由于受到父窗口的影响导致透明
		self._widget.setAutoFillBackground(True)
		palette = self._widget.palette()
		palette.setColor(palette.Window, QColor(240, 240, 240))
		self._widget.setPalette(palette)
		self._widget.installEventFilter(self)
		self.layout().addWidget(self._widget)

	def move(self, pos):
		if self.big==False:
			super(FramelessWindow, self).move(pos)

	def showMaximized(self):
		"""最大化,要去除上下左右边界,如果不去除则边框地方会有空隙"""
		self.big=True
		super(FramelessWindow, self).showMaximized()
		self.layout().setContentsMargins(0, 0, 0, 0)

	def showNormal(self):
		"""还原,要保留上下左右边界,否则没有边框无法调整"""
		self.big=False
		super(FramelessWindow, self).showNormal()
		self.layout().setContentsMargins(
			self.Margins, self.Margins, self.Margins, self.Margins)

	def eventFilter(self, obj, event):
		"""事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式"""
		if isinstance(event, QEnterEvent):
			self.setCursor(Qt.ArrowCursor)
		return super(FramelessWindow, self).eventFilter(obj, event)

	def paintEvent(self, event):
		"""由于是全透明背景窗口,重绘事件中绘制透明度为1的难以发现的边框,用于调整窗口大小"""
		super(FramelessWindow, self).paintEvent(event)
		painter = QPainter(self)
		painter.setPen(QPen(QColor(255, 255, 255, 1), 2 * self.Margins))
		painter.drawRect(self.rect())

	def mousePressEvent(self, event):
		"""鼠标点击事件"""
		super(FramelessWindow, self).mousePressEvent(event)
		if event.button() == Qt.LeftButton:
			self._mpos = event.pos()
			self._pressed = True

	def mouseReleaseEvent(self, event):
		'''鼠标弹起事件'''
		super(FramelessWindow, self).mouseReleaseEvent(event)
		self._pressed = False
		self.Direction = None

	def mouseMoveEvent(self, event):
		"""鼠标移动事件"""
		super(FramelessWindow, self).mouseMoveEvent(event)
		pos = event.pos()
		xPos, yPos = pos.x(), pos.y()
		
		wm, hm = self.width() - self.Margins, self.height() - self.Margins
		if self.isMaximized() or self.isFullScreen():
			self.Direction = None
			self.setCursor(Qt.ArrowCursor)
			return
		if event.buttons() == Qt.LeftButton and self._pressed:
			self._resizeWidget(pos)
			return


	def _resizeWidget(self, pos):
		pass


class neizhihanshu():
    def huoquneicunbianhao(a):
        return id(a)
    def createTuple():
        return tuple()
    def createList():
        return list()
    def createDictionary():
        return {}

if __name__ == '__main__':

	app = QApplication(sys.argv)
	app.setStyleSheet(StyleSheet)
	mainWnd = FramelessWindow()
	
	mainWnd.setWindowTitle('测试标题栏')
	mainWnd.setWindowIcon(QIcon('Qt.ico'))
	mainWnd.resize(QSize(1250,780))
	mainWnd.show()
	sys.exit(app.exec_())


eMap1 = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 2, 1],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
eMap2 = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 2, 0],
    [1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
eMap3 = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0]]
mapList = [eMap1, eMap2, eMap3]
index = random.randint(0, 2)
eMap = mapList[index]
enemyErectList = []
#  获取障碍物Rect列表
def get_eRect():
    for i in range(10):
        for j in range(10):
            if eMap[j][i] == 1:
                rect = pygame.Rect(i * 50, j * 50, 50, 50)
                enemyErectList.append(rect)
    return enemyErectList
#   获取保险Rect
def get_winRect():
    for i in range(10):
        for j in range(10):
            if eMap[j][i] == 2:
                rect = pygame.Rect(i * 50, j * 50, 50, 50)
    return rect


def get_keyRect():
    for i in range(10):
        for j in range(10):
            if eMap[j][i] == 3:
                rect = pygame.Rect(i * 50, j * 50, 50, 50)
    return rect


class map:
    def __init__(self):
        self.flyRect = pygame.Rect(50, 200, 50, 50)
        self.dSpeedX = 1
        self.dSpeedY = 1

    def fly(self, flag):
        if flag == 0:
            # fImg = pygame.image.load("dragon.png")
            # 绘制龙
            self.flyRect.x = self.flyRect.x + self.dSpeedX
            self.flyRect.y = self.flyRect.y + self.dSpeedY
    
            if self.flyRect.x <= 0 or self.flyRect.x >= 450:
                self.dSpeedX = -self.dSpeedX
            # 上下边界反弹的处理
            if self.flyRect.y <= 0 or self.flyRect.y >= 450:
                self.dSpeedY = -self.dSpeedY
    
            # screen.blit(fImg, self.flyRect)


mg = map()


def dragon(flag):
    mg.fly(flag)
    return mg.flyRect
