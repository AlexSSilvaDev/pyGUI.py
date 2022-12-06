# from PySimpleGUI import PySimpleGUI as sg
#
# #Layout
# sg.theme('reddit')
# layout = [
#     [sg.Text('usuário'), sg.Input(key='usuario')],
#     [sg.Text('senha'), sg.Input(key='senha',password_char='*')],
#     [sg.Checkbox('Salvar o login?')],
#     [sg.Button('Entrar')]
# ]
# #Janela
# janela = sg.Window('Tela de Login', layout)
# #Ler os eventos
# while True:
#     eventos, valores = janela.read()
#     if eventos == sg.WINDOW_CLOSED:
#         break

from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('BluePurple')
layout = [
     [sg.Text('Usuário'),sg.Input(key = 'alex')],
     [sg.Text('Senha'),sg.Input (key = '1234',password_char = '*')],
     [sg.Checkbox('Salvar o login?')],
     [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
     eventos, valores = janela.read()
     if eventos == sg.WINDOW_CLOSED:
          break
