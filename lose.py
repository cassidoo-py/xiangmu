# encoding:utf-8
import os,sys,time
from PyQt5 import QtCore,QtWidgets,QtGui

class guanji(object):

  def pageShow(self,page):
    #设置窗口的位置和大小
    page.setGeometry(400,400,400,200)
    #设置窗口的标题
    page.setWindowTitle('Window shutdown')
    #设置窗口的图标
    #page.setWindowIcon(QtGui.QIcon('#ddffgg'))
    #设置工具中提示的字体样式
    QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif',10))
    #创建一个提示
    page.setToolTip('这是Window关机工具')

    self.label = QtWidgets.QLabel(page)
    self.label.setGeometry(QtCore.QRect(60, 20, 120, 45))
    self.label.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
    self.label2 = QtWidgets.QLabel(page)
    self.label2.setGeometry(QtCore.QRect(100, 55, 40, 51))
    self.label2.setFont(QtGui.QFont("Roman times",10,QtGui.QFont.Bold))
    self.time = QtWidgets.QDateTimeEdit(page)
    self.time.setGeometry(QtCore.QRect(140, 70, 180, 25))
    self.time.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
    self.time.setCalendarPopup(True)
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    self.time.setDateTime(QtCore.QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm:ss'))

    self.btn = QtWidgets.QPushButton(page,clicked=self.shut)
    self.btn.setToolTip('这里是提交按钮')
    self.btn.move(110,110)

    self.btn1 = QtWidgets.QPushButton(page,clicked=self.cleart)
    self.btn1.setToolTip('这里是清除任务按钮')
    self.btn1.move(210,110)
    self.text = QtWidgets.QLabel(page)
    self.text.setGeometry(QtCore.QRect(25, 150, 350, 25))
    self.text.setFont(QtGui.QFont("Roman times",14,QtGui.QFont.Bold))

    self.setUI(page)
    page.show()
  def setUI(self,page):
    _translate = QtCore.QCoreApplication.translate

    self.label.setText(_translate("page","请输入关机时间"))
    self.label2.setText(_translate("page","日期："))
    self.btn.setText(_translate("page","提交"))
    self.btn1.setText(_translate("page","清除"))
    self.text.setText(_translate("page","请设置关机时间！"))

  def shut(self,page):
    datetime = self.time.text()
    t1 = time.strptime(datetime,"%Y-%m-%d %H:%M:%S")
    t = int(time.mktime(t1))
    nq = int(time.time())
    d = t-nq
    if d>0:
      try:
        os.system('shutdown -s -t %d' % d)
        self.text.setText("电脑将在%s关机！" % datetime)
      except:
        self.text.setText("设置失败！")
    else:
      self.text.setText("日期设置错误！")

  def cleart(self,page):
    try:
      os.system('shutdown -a')
      self.text.setText("已经清除关机任务！")
    except:
      self.text.setText("清除任务失败！")

if __name__=='__main__':
  app = QtWidgets.QApplication(sys.argv)
  page = QtWidgets.QWidget()
  ui = guanji()
  ui.pageShow(page)
  sys.exit(app.exec_())
