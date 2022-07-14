from PyQt5 import uic, QtWidgets
import time
import sqlite3


def logar():
    usu = tela_l.usuario.text()
    pw = tela_l.senha.text()
    tela_l.usuario.clear()
    tela_l.senha.clear()
    banco = sqlite3.connect('banco_cad.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE usuario = '{}'".format(usu))
        senha = cursor.fetchall()
        print(senha[0][0])
        banco.close()
    except:
        tela_l.erro.setText("Credenciais incorretas!")

    if pw == senha[0][0]:
        tela_l.close()
        time.sleep(0.5)
        tela_ini.show()
    else:
        tela_l.erro.setText("Credenciais incorretas!")

def logout():
    tela_ini.close()
    time.sleep(0.5)
    tela_l.show()


def cadastro():
    cc.show()


def cadastrar():
    usu_c = cc.usu_cc.text()
    email = cc.email_cc.text()
    pw_cc = cc.senha_cc.text()
    cad_senha_cc = cc.c_senha_cc.text()

    if pw_cc == cad_senha_cc:
            try:
                banco = sqlite3.connect("banco_cad.db")
                cursor = banco.cursor()
                cursor.execute(""" CREATE TABLE IF NOT EXISTS cadastro (
                usuario CHAR(20) PRIMARY KEY NOT NULL,
                email CHAR(100) NOT NULL, 
                senha CHAR(20) NOT NULL
                );            
                """)
                cursor.execute("INSERT INTO cadastro VALUES ('" + usu_c + "','" + email + "','" + pw_cc + "')")
                banco.commit()
                cc.erro_cc.setText("Usuário cadastrado com sucesso")
                banco.close()
            except sqlite3.Error as error:
                print("Erro ao inserir os dados: ", error)
    else:
            cc.erro_cc.setText("As senhas digitadas estão diferentes")


app = QtWidgets.QApplication([])
tela_ini = uic.loadUi("tela_ini.ui")
tela_l = uic.loadUi("tela_l.ui")
cc = uic.loadUi("cc.ui")
tela_l.login.clicked.connect(logar)
tela_ini.logout.clicked.connect(logout)
tela_l.senha.setEchoMode(QtWidgets.QLineEdit.Password)
tela_l.cadastrar.clicked.connect(cadastro)
cc.bcc.clicked.connect(cadastrar)

tela_l.show()
app.exec()
