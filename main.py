import PySimpleGUI as sg

layout =[
    [sg.Text("text" , enable_events= True, key = "-TEXT-" ),sg.Spin(["item 1","item 2"])],
    [sg.Button("button" , key = "-BUTTON1-")],
    [sg.Input(  key = "-INPUT-" )],
    [sg.Text("test"), sg.Button("test button",key = "-BUTTON2-" )]
]

window = sg.Window("converter",layout)

while True:
    event,values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-BUTTON1-":
        print (values ["-INPUT-"])

    if event == "-BUTTON2-":
        print ("button pressed")

    if event == "-TEXT-":
        print ("text was pressed")
window.closed()