import sys
from PySide6.QtWidgets import QPushButton, QMainWindow, QWidget, QApplication, QLabel, QLineEdit, QTextEdit, QVBoxLayout

class MainJanela(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.conjunto_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.conjunto_widget.setLayout(self.v_layout)

        self.label1 = QLabel("Texto aqui...")
        self.v_layout.addWidget(self.label1)
        self.setCentralWidget(self.conjunto_widget)

    def atualizar_label(self, nome, mensagem):
       
        texto = f"NOME: {nome}\nMENSAGEM: {mensagem}"
        self.label1.setText(texto)

class NovaJanela(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("VOCÊ É O DIEIMES?")
        self.setGeometry(100, 100, 300, 200)

        #1ª Caixa de Mensagem
        self.nomeLabel = QLabel("O JAMES EU QUERO UMA SALADA DE FRUTAS!")
        self.nomeInput = QLineEdit()

        #2ª Caixa de Mensagem
        self.mensagemLabel = QLabel("VOCÊ QUER A SALADA DE FRUTAS DE 5, 7 OU DE 10?")
        self.mensagemInput = QTextEdit()

        #Botão para Enviar
        self.botaoEnviar = QPushButton("OLHA QUE HABILIDADE! ME VÊ A DE 5, NO CAPRICHO")
        self.botaoEnviar.clicked.connect(self.enviar_msg)

        layout = QVBoxLayout()
        layout.addWidget(self.nomeLabel)
        layout.addWidget(self.nomeInput)
        layout.addWidget(self.mensagemLabel)
        layout.addWidget(self.mensagemInput)
        layout.addWidget(self.botaoEnviar)
        self.setLayout(layout)

    def enviar_msg(self):
       
        nome = self.nomeInput.text()
        mensagem = self.mensagemInput.toPlainText()

        self.main_window.atualizar_label(nome, mensagem)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainJanela()
    main_window.setWindowTitle("Título aqui!!")
    main_window.show()

    #Escolhendo a cor de fundo
    novaJanela = NovaJanela(main_window)
    novaJanela.setStyleSheet("background-color: gray;")
    novaJanela.show()

    sys.exit(app.exec())