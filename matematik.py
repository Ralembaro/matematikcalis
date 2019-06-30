from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def isaretbelirle(self):
        isaretler = ["+", "-"]
        isart = random.choice(isaretler)
        self.isaret.setText(isart)

    def toplamaSoruOlustur(self):
        self.sonuc = random.randint(20, 100)
        self.sayi1 = random.randint(1, (self.sonuc - 7))
        self.sayi2 = self.sonuc - self.sayi1

        aralikliste = [-4, -3, -2, -1, 1, 2, 3, 4]
        aralik = random.sample(aralikliste, 3)
        self.aralik1 = aralik[0]
        self.aralik2 = aralik[1]
        self.aralik3 = aralik[2]

        self.cevaplar = [self.sonuc, (self.sonuc + self.aralik1), (self.sonuc + self.aralik2), (self.sonuc + self.aralik3)]
        random.shuffle(self.cevaplar)

        self.sayi1label.setText(str(self.sayi1))
        self.sayi2label.setText(str(self.sayi2))
        self.cevap1.setText(str(self.cevaplar[0]))
        self.cevap2.setText(str(self.cevaplar[1]))
        self.cevap3.setText(str(self.cevaplar[2]))
        self.cevap4.setText(str(self.cevaplar[3]))

    def cikarmaSoruOlustur(self):
        self.sayi1 = random.randint(20, 100)
        self.sayi2 = random.randint(1, (self.sayi1 - 7))
        self.sonuc = self.sayi1 - self.sayi2

        aralikliste = [-4, -3, -2, -1, 1, 2, 3, 4]
        aralik = random.sample(aralikliste, 3)
        self.aralik1 = aralik[0]
        self.aralik2 = aralik[1]
        self.aralik3 = aralik[2]

        self.cevaplar = [self.sonuc, (self.sonuc + self.aralik1), (self.sonuc + self.aralik2), (self.sonuc + self.aralik3)]
        random.shuffle(self.cevaplar)

        self.sayi1label.setText(str(self.sayi1))
        self.sayi2label.setText(str(self.sayi2))
        self.cevap1.setText(str(self.cevaplar[0]))
        self.cevap2.setText(str(self.cevaplar[1]))
        self.cevap3.setText(str(self.cevaplar[2]))
        self.cevap4.setText(str(self.cevaplar[3]))

    def setUI(self):
        baslik = QLabel("")
        baslik.setFont(QFont("Helvetica", 22, QFont.Bold, ))
        baslik.setText("""
                                            <h1><font color =\"red\">Matematik Çalışma</font></h1>
                        """)
        baslik.setAlignment(Qt.AlignCenter)
        cevapbaslik = QLabel("CEVAPLAR")
        cevapbaslik.setFont(QFont("Helvetica", 22, QFont.Bold, ))
        cevapbaslik.setAlignment(Qt.AlignTop)

        self.sondurum = QTextEdit()

        self.sayi1label = QLabel("")
        self.sayi2label = QLabel("")
        self.isaret = QLabel("")
        esit = QLabel(" = ")
        sonuclabel = QLabel("?")

        self.cevapanahtari = {}
        self.toplam = QLabel("DOĞRU: 0 ve YANLIŞ: 0")

        self.cevap1 = QRadioButton("")
        self.cevap2 = QRadioButton("")
        self.cevap3 = QRadioButton("")
        self.cevap4 = QRadioButton("")

        self.cevap1.setFont(QFont("Helvetica", 22, QFont.Bold))
        self.cevap2.setFont(QFont("Helvetica", 22, QFont.Bold))
        self.cevap3.setFont(QFont("Helvetica", 22, QFont.Bold))
        self.cevap4.setFont(QFont("Helvetica", 22, QFont.Bold))
        self.toplam.setFont(QFont("Helvetica", 15))

        self.sayi1label.setFont(QFont("Helvetica", 22, QFont.Bold))
        self.sayi2label.setFont(QFont("Helvetica", 22, QFont.Bold))
        self.isaret.setFont(QFont("Helvetica", 22, QFont.Bold))
        esit.setFont(QFont("Helvetica", 22, QFont.Bold))
        sonuclabel.setFont(QFont("Helvetica", 22, QFont.Bold))

        cevapla = QPushButton("Cevapla")
        self.sayac = 1

        genel = QHBoxLayout()
        v_box = QVBoxLayout()
        v_box1 = QVBoxLayout()
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()

        h_box1.addWidget(baslik)
        h_box2.addWidget(self.sayi1label)
        h_box2.addWidget(self.isaret)
        h_box2.addWidget(self.sayi2label)
        h_box2.addWidget(esit)
        h_box2.addWidget(sonuclabel)
        h_box3.addWidget(self.cevap1)
        h_box3.addWidget(self.cevap2)
        h_box3.addWidget(self.cevap3)
        h_box3.addWidget(self.cevap4)

        v_box.addLayout(h_box1)
        v_box.addStretch()
        v_box.addLayout(h_box2)
        v_box.addStretch()
        v_box.addLayout(h_box3)
        v_box.addStretch()
        v_box.addWidget(cevapla)

        v_box1.addWidget(cevapbaslik)
        v_box1.addWidget(self.sondurum)
        v_box1.addWidget(self.toplam)

        genel.addLayout(v_box)
        genel.addLayout(v_box1)

        cevapla.clicked.connect(self.uygula)

        self.isaretbelirle()
        if self.isaret.text() == "+":
            self.toplamaSoruOlustur()
        elif self.isaret.text() == "-":
            self.cikarmaSoruOlustur()
        else:
            self.isaret.setText("?")

        self.setLayout(genel)
        self.show()
        self.setWindowTitle("Matematik Çalışma")

    def goster(self):
        self.dogru = 0
        self.yanlis = 0
        self.sorular = list(self.cevapanahtari.keys())
        c = ""

        for i in self.sorular:
            a = str(i)
            b = self.cevapanahtari[i]
            c += (a + " : " + b + "\n")
        self.sondurum.setText(c)

        for i in self.cevapanahtari:
            if self.cevapanahtari[i] == "DOĞRU":
                self.dogru += 1
            else:
                self.yanlis += 1
        self.toplam.setText("DOĞRU: {} ve YANLIŞ: {}".format(self.dogru, self.yanlis))

    def uygula(self):
        if self.cevap1.isChecked():
            if self.isaret.text() == "+":
                if self.cevaplar[0] == self.sayi1 + self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
            else:
                if self.cevaplar[0] == self.sayi1 - self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()

        elif self.cevap2.isChecked():
            if self.isaret.text() == "+":
                if self.cevaplar[1] == self.sayi1 + self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
            else:
                if self.cevaplar[1] == self.sayi1 - self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()

        elif self.cevap3.isChecked():
            if self.isaret.text() == "+":
                if self.cevaplar[2] == self.sayi1 + self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
            else:
                if self.cevaplar[2] == self.sayi1 - self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()

        elif self.cevap4.isChecked():
            if self.isaret.text() == "+":
                if self.cevaplar[3] == self.sayi1 + self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
            else:
                if self.cevaplar[3] == self.sayi1 - self.sayi2:
                    self.cevapanahtari[self.sayac] = "DOĞRU"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()
                else:
                    self.cevapanahtari[self.sayac] = "YANLIŞ"
                    self.goster()
                    self.sayac += 1
                    self.isaretbelirle()
                    if self.isaret.text() == "+":
                        self.toplamaSoruOlustur()
                    else:
                        self.cikarmaSoruOlustur()

        else:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
