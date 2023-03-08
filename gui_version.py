import PySimpleGUI as sg

layout = [
   [sg.Text("参照フォルダ"), sg.InputText(), sg.FolderBrowse(initial_folder='$HOME', key='ref')],
   [sg.Text("保存フォルダ"), sg.InputText(), sg.FolderBrowse(initial_folder='$HOME', key='save')],
   [sg.Submit(), sg.Cancel()],
]

window = sg.Window("フォルダ選択", layout)

event, values = window.read()
window.close()

print('ref :' + values['ref'])
print('save :' +values['save'])

# for reading .xls files, use pandas
import pandas as pd
# for searching files, use glob
import glob
# for making directory, use os
import os
# for plotting, use matplotlib
import matplotlib.pyplot as plt

path = values['ref'] + '/*.xls'
files = dict()
files = glob.glob(path)

l = len(files)

figure_name = []
data = dict()
for i in range(l):
    figure_name.append(os.path.basename(files[i]).replace('.xls',''))
    data[figure_name[i]] = pd.read_excel(files[i], sheet_name='Output_Data_test', header=4, index_col=0)


# return true if theres 'fig' folder
tf = os.path.isdir(values['save'] + '/fig')
print(tf)
# if theres no 'fig' folder, make it
if tf == False:
    os.mkdir(values['save'] +'/fig')

# plot

for i in range(l):
    fig = plt.figure(figsize=(5,3), dpi=300)
    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx()
    ax1.set_xlim(0,10000)
    ax1.set_ylim(0,1.0)
    ax2.set_ylim(0,100)
    ax1.grid(True, which='major', axis='y', color='gray', linestyle='--', linewidth=0.5)
    ax1.set_xlabel("繰り返し数")
    ax1.set_ylabel("摩擦係数[-]")
    ax2.set_ylabel(r"振幅[$\mu$m], 湿度[%]")
    ax1.set_title(figure_name[i])
    ax2.scatter(data[figure_name[i]].index, data[figure_name[i]]['振幅，μm'], s=0.1, label='相対振幅', c="#90B34F")
    ax2.scatter(data[figure_name[i]].index, data[figure_name[i]]['相対湿度'], s=0.1, label='相対湿度' , c="#4676B5")
    ax1.scatter(data[figure_name[i]].index, data[figure_name[i]]['摩擦係数'], s=0.1, label='摩擦係数' , c="#B84644")
    ax1.legend(markerscale = 5, frameon = False, loc = "upper right")
    ax2.legend(markerscale = 5, frameon = False, loc = "upper right", bbox_to_anchor = (1 ,0.9))
    plt.savefig(values['save'] + '/fig/' + figure_name[i] + '.pdf', bbox_inches='tight')
    print(figure_name[i])