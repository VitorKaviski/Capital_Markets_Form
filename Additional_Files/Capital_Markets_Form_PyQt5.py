# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_janelaprincipal(object):
    def setupUi(self, janelaprincipal):
        janelaprincipal.setObjectName("janelaprincipal")
        janelaprincipal.setWindowModality(QtCore.Qt.WindowModal)
        janelaprincipal.resize(930, 1000)
        janelaprincipal.setMinimumSize(QtCore.QSize(930, 1000))
        janelaprincipal.setMaximumSize(QtCore.QSize(930, 1000))
        self.centralwidget = QtWidgets.QWidget(janelaprincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_azul = QtWidgets.QFrame(self.centralwidget)
        self.frame_azul.setMaximumSize(QtCore.QSize(930, 1000))
        self.frame_azul.setStyleSheet("background-color: rgb(0, 4, 255);")
        self.frame_azul.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_azul.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_azul.setObjectName("frame_azul")
        self.frame_verde = QtWidgets.QFrame(self.frame_azul)
        self.frame_verde.setGeometry(QtCore.QRect(-10, 50, 945, 200))
        self.frame_verde.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_verde.setStyleSheet("background-color: rgb(12, 255, 0);")
        self.frame_verde.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_verde.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_verde.setObjectName("frame_verde")
        self.frame_azulclaro = QtWidgets.QFrame(self.frame_verde)
        self.frame_azulclaro.setGeometry(QtCore.QRect(424, 15, 111, 41))
        self.frame_azulclaro.setStyleSheet("background-color: rgb(135, 243, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 3px solid rgb(45,45,45);\n"
"padding: 1px;\n"
"border-radius: 5px;\n"
"")
        self.frame_azulclaro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_azulclaro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_azulclaro.setObjectName("frame_azulclaro")
        self.RelacoesTitulo = QtWidgets.QLabel(self.frame_azulclaro)
        self.RelacoesTitulo.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.RelacoesTitulo.setObjectName("RelacoesTitulo")
        self.frame_bege = QtWidgets.QFrame(self.frame_verde)
        self.frame_bege.setGeometry(QtCore.QRect(209, 70, 541, 121))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.frame_bege.setFont(font)
        self.frame_bege.setStyleSheet("background-color:rgb(255, 170, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 3px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.frame_bege.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bege.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bege.setObjectName("frame_bege")
        self.RelacoesTexto = QtWidgets.QLabel(self.frame_bege)
        self.RelacoesTexto.setGeometry(QtCore.QRect(0, 0, 541, 121))
        self.RelacoesTexto.setStyleSheet("")
        self.RelacoesTexto.setObjectName("RelacoesTexto")
        self.frame_branco1 = QtWidgets.QFrame(self.frame_azul)
        self.frame_branco1.setGeometry(QtCore.QRect(380, 260, 181, 31))
        self.frame_branco1.setAutoFillBackground(False)
        self.frame_branco1.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 1px;\n"
"border-radius: 5px;")
        self.frame_branco1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_branco1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_branco1.setObjectName("frame_branco1")
        self.Box_formulaescolhida = QtWidgets.QComboBox(self.frame_branco1)
        self.Box_formulaescolhida.setGeometry(QtCore.QRect(0, 0, 181, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Box_formulaescolhida.setFont(font)
        self.Box_formulaescolhida.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color:rgb(85, 170, 127);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 1px;\n"
"border-radius: 5px;\n"
"")
        self.Box_formulaescolhida.setObjectName("Box_formulaescolhida")
        self.Box_formulaescolhida.addItem("")
        self.Box_formulaescolhida.addItem("")
        self.Box_formulaescolhida.addItem("")
        self.Box_formulaescolhida.addItem("")
        self.Box_formulaescolhida.addItem("")
        self.frame_azulpiscina = QtWidgets.QFrame(self.frame_azul)
        self.frame_azulpiscina.setGeometry(QtCore.QRect(290, 300, 361, 231))
        self.frame_azulpiscina.setStyleSheet("background-color:rgb(147, 255, 223);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 3px;\n"
"border-radius: 10px;\n"
"")
        self.frame_azulpiscina.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_azulpiscina.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_azulpiscina.setObjectName("frame_azulpiscina")
        self.label_opcoesdaformulaescolhida = QtWidgets.QLabel(self.frame_azulpiscina)
        self.label_opcoesdaformulaescolhida.setGeometry(QtCore.QRect(0, 0, 361, 231))
        self.label_opcoesdaformulaescolhida.setTextFormat(QtCore.Qt.AutoText)
        self.label_opcoesdaformulaescolhida.setObjectName("label_opcoesdaformulaescolhida")
        self.frame_branco2 = QtWidgets.QFrame(self.frame_azul)
        self.frame_branco2.setGeometry(QtCore.QRect(414, 540, 111, 31))
        self.frame_branco2.setAutoFillBackground(False)
        self.frame_branco2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 1px;\n"
"border-radius: 5px;\n"
"")
        self.frame_branco2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_branco2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_branco2.setObjectName("frame_branco2")
        self.Box_escolhadasopcoes = QtWidgets.QComboBox(self.frame_branco2)
        self.Box_escolhadasopcoes.setGeometry(QtCore.QRect(0, 0, 111, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Box_escolhadasopcoes.setFont(font)
        self.Box_escolhadasopcoes.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 1px;\n"
"border-radius: 5px;\n"
"")
        self.Box_escolhadasopcoes.setObjectName("Box_escolhadasopcoes")
        self.frame_verde_2 = QtWidgets.QFrame(self.frame_azul)
        self.frame_verde_2.setGeometry(QtCore.QRect(199, 580, 541, 281))
        self.frame_verde_2.setStyleSheet("background-color:rgb(85, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 3px;\n"
"border-radius: 10px;\n"
"")
        self.frame_verde_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_verde_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_verde_2.setObjectName("frame_verde_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_verde_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 541, 281))
        self.textEdit.setObjectName("textEdit")
        self.frame_vermelho2 = QtWidgets.QFrame(self.frame_azul)
        self.frame_vermelho2.setGeometry(QtCore.QRect(-10, 870, 981, 61))
        self.frame_vermelho2.setAutoFillBackground(False)
        self.frame_vermelho2.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.frame_vermelho2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vermelho2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vermelho2.setObjectName("frame_vermelho2")
        self.frame_vermelho_2 = QtWidgets.QFrame(self.frame_azul)
        self.frame_vermelho_2.setGeometry(QtCore.QRect(0, 0, 929, 50))
        self.frame_vermelho_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_vermelho_2.setStyleSheet("background-color: rgb(255, 0, 4);")
        self.frame_vermelho_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_vermelho_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vermelho_2.setObjectName("frame_vermelho_2")
        self.frame_amarelo_2 = QtWidgets.QFrame(self.frame_vermelho_2)
        self.frame_amarelo_2.setGeometry(QtCore.QRect(240, 0, 461, 50))
        self.frame_amarelo_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.frame_amarelo_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame_amarelo_2.setStyleSheet("background-color: rgb(255, 255, 56);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 4px solid rgb(45,45,45);\n"
"padding: 1px;\n"
"border-radius: 5px;\n"
"")
        self.frame_amarelo_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_amarelo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_amarelo_2.setObjectName("frame_amarelo_2")
        self.Titulo_2 = QtWidgets.QLabel(self.frame_amarelo_2)
        self.Titulo_2.setGeometry(QtCore.QRect(0, 0, 460, 50))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.Titulo_2.setFont(font)
        self.Titulo_2.setMouseTracking(True)
        self.Titulo_2.setObjectName("Titulo_2")
        self.verticalLayout.addWidget(self.frame_azul)
        janelaprincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaprincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaprincipal)

    def retranslateUi(self, janelaprincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaprincipal.setWindowTitle(_translate("janelaprincipal", "MainWindow"))
        self.RelacoesTitulo.setText(_translate("janelaprincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Rela????es</span></p></body></html>"))
        self.RelacoesTexto.setText(_translate("janelaprincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">vp: Valor Presente | VF: Valor Futuro </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TI: Tempo de Investimento | TJ: Taxa de Juros</span></p></body></html>"))
        self.Box_formulaescolhida.setItemText(0, _translate("janelaprincipal", "  Selecione a F??rmula Desejada"))
        self.Box_formulaescolhida.setItemText(1, _translate("janelaprincipal", "                         vp"))
        self.Box_formulaescolhida.setItemText(2, _translate("janelaprincipal", "                         VF"))
        self.Box_formulaescolhida.setItemText(3, _translate("janelaprincipal", "                         TI"))
        self.Box_formulaescolhida.setItemText(4, _translate("janelaprincipal", "                         TJ"))
        self.label_opcoesdaformulaescolhida.setText(_translate("janelaprincipal", "<html><head/><body><p align=\"center\">Escolha uma form??la para obter o reultado desejado</p></body></html>"))
        self.Titulo_2.setText(_translate("janelaprincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:35pt; font-weight:600;\">Formul??rio do Mercado Financeiro</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    janelaprincipal = QtWidgets.QMainWindow()
    ui = Ui_janelaprincipal()
    ui.setupUi(janelaprincipal)
    janelaprincipal.show()
    sys.exit(app.exec_())
