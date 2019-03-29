# -*- coding: utf-8 -*-
import qrcode
from PIL import Image
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
'''
version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
ROR_CORRECT_H：大约30%或更少的错误能被纠正。

box_size：控制二维码中每个小格子包含的像素数。

border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）。

img.save：是将生成二维码图片保存到哪里。
'''

class Myqrcode(object):
    def __init__(self):
        self.image_size = {}
        self.qr = None
    
    def make_qrcode(self, data, image_size = 2):
        self.qr=qrcode.QRCode(version = image_size,error_correction = qrcode.constants.ERROR_CORRECT_L,box_size=10,border=10,)
        if data is not None:
            self.qr.add_data(data)
            self.qr.make(fit=True)
            img = self.qr.make_image()
            img.show()
            img.save('test.jpg')
        pass
    def high_make_qrcode(self, data, image_size = 2):
        qr = qrcode.QRCode(version=image_size,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4)
        qr.add_data("cxtan")
        qr.make(fit=True)
        img = qr.make_image()
        img = img.convert("RGBA")

        img_w,img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        print (size_w, size_h)
        print (img_w, img_h)
        icon = Image.open("icon.jpg")
        icon_w,icon_h = icon.size
        print (icon_w, icon_h)
        if icon_w >size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

        w = int((img_w - icon_w)/2)
        h = int((img_h - icon_h)/2)
        icon = icon.convert("RGBA")
        img.paste(icon,(w,h),icon)
        img = img.convert("RGB");
        # img.show()
        img.save('createlogo.jpg')


class Mywigdet(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        pass
    def initui(self):
        self.setWindowTitle("qrcode")
        self.center()
        self.setWindowIcon(QIcon("icon.jpg"))

        btn = QPushButton('Button', self)
        print("hint size ", btn.sizeHint())
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        quit_btn = QPushButton('Quit', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(quit_btn.sizeHint())
        quit_btn.move(200, 200)
        self.show()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, '消息', "确认退出", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        print("center is ", cp)
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.resize(self.sizeHint())


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # qr=qrcode.QRCode(None,error_correction = qrcode.constants.ERROR_CORRECT_L,box_size=10,border=10,)
    qr = Myqrcode()
    # qr.make_qrcode("cxtan", 2)
    qr.high_make_qrcode("cxtan")
    mwigdet = Mywigdet()
    sys.exit(app.exec_())
    pass