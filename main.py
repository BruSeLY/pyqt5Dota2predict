import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import io
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap, QTransform, QColor
import random
import pymysql
from PIL import Image
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_codolo1',
                                 password='codologia1',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_test")
    print("successfully...")
except Exception as ex:
    print(ex)

templ = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Log</class>
 <widget class="QMainWindow" name="Log">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>902</width>
    <height>597</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(7, 153, 147, 255), stop:1 rgba(255, 110, 255, 255));</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="photo">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>50</y>
      <width>531</width>
      <height>291</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="btn_profile">
    <property name="geometry">
     <rect>
      <x>770</x>
      <y>20</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Профиль</string>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>400</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label_warning">
       <property name="text">
        <string>Выберите сторону</string>
       </property>
       <property name="scaledContents">
        <bool>false</bool>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>450</y>
      <width>611</width>
      <height>81</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="1" column="0">
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QPushButton" name="btn_radiant">
         <property name="text">
          <string>Выиграют силы света!</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="btn_dire">
         <property name="text">
          <string>Выиграют силы тьмы!</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item row="0" column="0">
      <widget class="QPushButton" name="btn_confirm">
       <property name="text">
        <string>Поставить на матч</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="btn_find_match">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>360</y>
      <width>221</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Найти матч</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>902</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

SCREEN_SIZE = [400, 400]
user_side = ''
currentMatch = ''
direThis = ''
radiantThis = ''
radiantWin = ''
count_confirm = 0


def get_photo(radiantThis, direThis):
    radiantThis = radiantThis.split()
    direThis = direThis.split()
    photoRadiant = Image.open("Background.jpg").resize((512 * 5, 1520))
    im1 = Image.open(f"IconHero\{radiantThis[0]}_icon.webp").convert("RGB").resize((512, 288))
    im2 = Image.open(f"IconHero\{radiantThis[1]}_icon.webp").convert("RGB").resize((512, 288))
    im3 = Image.open(f"IconHero\{radiantThis[2]}_icon.webp").convert("RGB").resize((512, 288))
    im4 = Image.open(f"IconHero\{radiantThis[3]}_icon.webp").convert("RGB").resize((512, 288))
    im5 = Image.open(f"IconHero\{radiantThis[4]}_icon.webp").convert("RGB").resize((512, 288))
    im6 = Image.open(f"IconHero\{direThis[0]}_icon.webp").convert("RGB").resize((512, 288))
    im7 = Image.open(f"IconHero\{direThis[1]}_icon.webp").convert("RGB").resize((512, 288))
    im8 = Image.open(f"IconHero\{direThis[2]}_icon.webp").convert("RGB").resize((512, 288))
    im9 = Image.open(f"IconHero\{direThis[3]}_icon.webp").convert("RGB").resize((512, 288))
    im10 = Image.open(f"IconHero\{direThis[4]}_icon.webp").convert("RGB").resize((512, 288))
    photoRadiant.paste(im1, (0, 0))
    photoRadiant.paste(im2, (512, 0))
    photoRadiant.paste(im3, (512*2, 0))
    photoRadiant.paste(im4, (512*3, 0))
    photoRadiant.paste(im5, (512*4, 0))
    photoRadiant.paste(im6, (0, 1230))
    photoRadiant.paste(im7, (512, 1230))
    photoRadiant.paste(im8, (512*2, 1230))
    photoRadiant.paste(im9, (512*3, 1230))
    photoRadiant.paste(im10, (512*4, 1230))
    photoRadiant.save("photo1.jpg")
    photoRadiant = Image.open("photo1.jpg").resize((531, 291))
    photoRadiant.save("photo.jpg")
    return photoRadiant


def get_match():
    with connection.cursor() as cursor:
        find_query = f"SELECT * FROM match1"
        cursor.execute(find_query)
        matches = list(cursor.fetchall())
        match = matches[random.randint(0, len(matches))]
        print(match)
    currentMatch = match["ID_MATCH"]
    direThis = match["DIRE"]
    radiantThis = match["RADIANT"]
    radiantWin = match["RADIANT_WIN"]
    photo = get_photo(radiantThis, direThis)
    return currentMatch, photo, radiantWin


class Log(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO()
        uic.loadUi(f, self)


class BetWindow(QMainWindow):
    def __init__(self):
        super(BetWindow, self).__init__()
        f = io.StringIO(templ)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.btn_radiant.clicked.connect(self.bet_radiant)
        self.btn_dire.clicked.connect(self.bet_dire)
        self.btn_confirm.clicked.connect(self.confirm)
        self.btn_find_match.clicked.connect(self.find_match)

    def find_match(self):
        global user_side, currentMatch, direThis, radiantThis, radiantWin, count_confirm
        count_confirm = 0
        with connection.cursor() as cursor:
            find_query = f"SELECT * FROM match1"
            cursor.execute(find_query)
            matches = list(cursor.fetchall())
            match = matches[random.randint(0, len(matches))]
            print(match)
        currentMatch = match["ID_MATCH"]
        direThis = match["DIRE"]
        radiantThis = match["RADIANT"]
        radiantWin = match["RADIANT_WIN"]
        photo = get_photo(radiantThis, direThis)
        self.pixmap = QPixmap('photo.jpg')
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.photo.setPixmap(self.pixmap)
        self.label_warning.setText("Выберите сторону")

    def bet_radiant(self):
        global user_side
        user_side = 0

    def bet_dire(self):
        global user_side
        user_side = 1

    def confirm(self):
        global user_side, currentMatch, direThis, radiantThis, radiantWin, count_confirm
        if count_confirm != 0:
            self.label_warning.setText(f'Выберите новый матч')

        elif user_side == '':
            self.label_warning.setText("Выберите сторону")
        else:
            if user_side == 0:

                if user_side == 0 and radiantWin != 0 or user_side == 1 and radiantWin != 1:
                    count_confirm = 1
                    self.label_warning.setText("Вы проиграли")
                else:
                    count_confirm = 1
                    self.label_warning.setText("Вы победили")
            if user_side == 1:

                if user_side == 0 and radiantWin != 0 or user_side == 1 and radiantWin != 1:
                    count_confirm = 1
                    self.label_warning.setText("Вы проиграли")
                else:
                    count_confirm = 1
                    self.label_warning.setText("Вы победили")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BetWindow()
    window.show()

    sys.exit(app.exec())