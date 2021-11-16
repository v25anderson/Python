from PySimpleGUI import  PySimpleGUI as sg

#Layout
sg.theme('LightBrown3')
layout =[
[sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
[sg.Text('Senha'), sg.Input(key='senha', password_char='*',size=(20,1))],
[sg.Checkbox('Salvar Login')],
[sg.Button('Entrar')]
] 
#Janela
janela = sg.Window('Tela de Login', layout)
#Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario']=='Vini' and valores['senha']=='123':
            print('Bem Vindo')
