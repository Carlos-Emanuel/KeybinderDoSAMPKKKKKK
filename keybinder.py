import tkinter
import keyboard
import clipboard
from winsound import Beep
from time import sleep



def escrever_na_tela(text):
    global label
    label = tkinter.Label(text=text, font=('Times New Roman','50'), fg='white', bg='black')
    label.master.overrideredirect(True)
    label.master.geometry("+950+650")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "black")
    label.pack()
    label.update()
    label.destroy()
    label.quit()


def executar():
    global id
    keyboard.send('t')
    keyboard.send('ctrl+a')
    keyboard.send('backspace')
    keyboard.send('ctrl+v')
    keyboard.send('return')
    Beep(1000, 200)
    sleep(2)
    clipboard.copy(id)


print("//__ (: Bem vindo ao keybinder :) __\\\\")
id = 'desconhecido'
id2 = ''
beep = True

def Abordar():
    #keyboard.send('1')
    clipboard.copy(f"/abordar {id}")
    sleep(0.01)
    print('abordardando id: ' + id)
    executar()


def Perseguir():
    #keyboard.send('2')
    clipboard.copy('/perseguicao ' + id)
    sleep(0.01)
    print('iniciando perseguicao no id: ' + id)
    executar()


def Algemar():
    #keyboard.send('3')
    clipboard.copy('/algemar ' + id)
    sleep(0.01)
    print('algemando id: ' + id)
    executar()


def Prender():
    #keyboard.send('4')
    clipboard.copy('/prender ' + id)
    sleep(0.01)
    keyboard.send('backspace')
    print('prendendo id: ' + id)
    executar()


def Localizar():
    #keyboard.send('5')
    clipboard.copy('/localizar ' + id)
    sleep(0.01)
    print('localizando id: ' + id)
    executar()


def SetarID():
    global id2, id
    #keyboard.send('0')
    escrever_na_tela('Aguardando id...')
    print('digite o id...')
    Beep(1000, 200)
    id = next(keyboard.get_typed_strings(keyboard.record(until='backspace'), allow_backspace=False))
    for number in id:
        if number in '0123456789':
            id2 += number
    id = id2[0:3]
    id2 = ''
    clipboard.copy(id)
    print(f'id: {id} copiado para o clip board')
    escrever_na_tela(id)
    Beep(1500, 500)


def SetarID2():
    global setarid
    setarid = True


def UsarKit():
    #keyboard.send('k')
    clipboard.copy('/usarkit')
    sleep(0.01)
    print('usando kit...')
    keyboard.send('t')
    keyboard.send('ctrl+a')
    keyboard.send('backspace')
    keyboard.send('ctrl+v')
    keyboard.send('return')
    Beep(1000, 200)
    sleep(2)
    clipboard.copy(id)


def MandarSMS():
    #keyboard.send('9')
    clipboard.copy(f'/sms {id} ')
    sleep(0.01)
    print(f'mandando sms para {id}')
    keyboard.send('t')
    keyboard.send('ctrl+a')
    keyboard.send('backspace')
    keyboard.send('ctrl+v')
    Beep(1000, 200)
    sleep(2)
    clipboard.copy(id)


def Procurados():
    #keyboard.send('p')
    clipboard.copy('/procurados')
    sleep(0.01)
    print('vendo lista de procurados...')
    keyboard.send('t')
    keyboard.send('ctrl+a')
    keyboard.send('backspace')
    keyboard.send('ctrl+v')
    keyboard.send('return')
    Beep(1000, 200)
    sleep(2)
    clipboard.copy(id)

def Bafometro():
    clipboard.copy(f"/bafometro {id}")
    sleep(0.01)
    print('fazendo teste do bafômetro no id: ' + id)
    executar()


key = 'space + '
key = ''


keyboard.add_hotkey(f"{key}' + 1", Abordar, args=())
keyboard.add_hotkey(f"{key}' + 2", Perseguir, args=())
keyboard.add_hotkey(f"{key}' + 3", Algemar, args=())
keyboard.add_hotkey(f"{key}' + 4", Prender, args=())
keyboard.add_hotkey(f"{key}' + 5", Localizar, args=())
keyboard.add_hotkey(f"{key}' + 0", SetarID2, args=())
keyboard.add_hotkey(f"{key}' + k", UsarKit, args=())
keyboard.add_hotkey(f"{key}' + 9", MandarSMS, args=())
keyboard.add_hotkey(f"{key}' + p", Procurados, args=())
keyboard.add_hotkey(f"{key}' + b", Bafometro, args=())
setarid = False
while True:
    sleep(0.01)
    if setarid:
        keyboard.remove_hotkey(f"{key}' + 0")
        SetarID()
        setarid = False
        keyboard.add_hotkey(f"{key}' + 0", SetarID2, args=())


