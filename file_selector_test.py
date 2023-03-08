import PySimpleGUI as sg
import pandas as pd

layout = [
   [sg.Text("参照フォルダ"), sg.InputText(), sg.FolderBrowse(initial_folder='$HOME', key='ref')],
   [sg.Submit(), sg.Cancel()],
]

window = sg.Window("フォルダ選択", layout)

event, values = window.read()
window.close()

print('ref :' +values['ref'])

# パス抜き出し
import glob
import os


path = values['ref'] + '/*.xls'
files = dict()
files = glob.glob(path)

l = len(files)

figure_name = []
data = dict()
for i in range(l):
    figure_name.append(os.path.basename(files[i]).replace('.xls',''))
    data[figure_name[i]] = pd.read_excel(files[i], sheet_name='Output_Data_test', header=4, index_col=0)