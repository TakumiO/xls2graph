import PySimpleGUI as sg

layout = [
   [sg.Text("参照フォルダ"), sg.InputText(), sg.FolderBrowse(initial_folder='$HOME', key='ref')],
   [sg.Text("保存フォルダ"), sg.InputText(), sg.FolderBrowse(initial_folder='$HOME', key='save')],
   [sg.Submit(), sg.Cancel()],
]

window = sg.Window("フォルダ選択", layout)

event, values = window.read()
window.close()
print(values['ref'], values['save'])