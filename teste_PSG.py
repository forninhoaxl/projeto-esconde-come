import PySimpleGUI as psg
# import rascunho_psg as rasc


class jogopsg_pt2():
    def __init__(self):
        c = True
        layout = [
            [psg.Text('Palavra determinada!')],
            [psg.Text('aí dento')],
            [psg.Button('enviar')]
        ]
        self.janela = psg.Window('Jogo da minha chibata').layout(layout)

    def Iniciar(self):
        cont = 0
        while True:
            self.button, self.values = self.janela.Read()
            lista2 = self.values


jogo2 = jogopsg_pt2()
jogo2.Iniciar()