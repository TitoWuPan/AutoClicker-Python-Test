import win32api, win32gui, win32con
import pyautogui
import tkinter as tk
from tkinter import CENTER, ttk

ventana = tk.Tk()
ventana.title("Autoclik Mouse")
ventana.config(width=400, height=200)
ventana.resizable(False, False)

# Funciones
def reiniciar():
    app.Stop()
    app.labe_ajuste.config(text= "Reiniciando...")
    ventana.after(5000, app.Reiniciar)

def Move_size(hwnd, x, y):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP , x , y, 434, 255, win32con.SWP_SHOWWINDOW)

def Ajustar_ventana(game):
        hWnd = win32gui.FindWindow(None,game)
        if (hWnd != 0):
            x,y,w,h = win32gui.GetWindowRect(hWnd)
            Move_size(hWnd, x, y)
            a = (f"Inicio Exitoso - Ventana {game}")
            return hWnd , a
        else:
            a = ("No se encuentra el Nox")
            return None, a

def Click(pos):
    global window
    client_pos = win32gui.ScreenToClient(win32gui.WindowFromPoint(pos), pos)
    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
    win32api.SendMessage(window, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp) 
    win32api.SendMessage(window, win32con.WM_LBUTTONUP, None, tmp)

def Key_press(arg):
    pyautogui.press(arg)

def Key_time(arg, time = 1000):
    pyautogui.keyDown(arg)
    Click((80,80))
    ventana.after(time, Key_End, arg)

def Key_End(arg):
    Click((80,80))
    pyautogui.keyUp(arg)
    
def click_image(imagen, x, y, w, h, Ncoin = 0.9):
    start = pyautogui.locateCenterOnScreen(imagen, region=(x, y, w, h), grayscale=True, confidence=Ncoin)
    if start is not None:
        Click(start)
        return

def seach_image(imagen, x, y, w, h, Ncoin = 0.9):
    app.labe_ajuste.config(text= f"Buscando {imagen}")
    aux = pyautogui.locateCenterOnScreen(imagen, region=(x, y, w, h), grayscale=True, confidence=Ncoin)
    if aux is not None:
        return True
    else:
        return False

def inicio(x,y,i):
    global condition
    if condition:
        Click((x,y))
        app.labe_mouse.config(text= f"X {pyautogui.position().x} - Y {pyautogui.position().y}")
        ventana.after(i, inicio, x, y, i)

class Aplicacion(ttk.Frame):
    def __init__(self, main_window):

        super().__init__(main_window)

        self.labe_name = ttk.Label(main_window, text="X - ")
        self.labe_name.place(x=30, y=20)
        
        self.box_name_x = ttk.Entry(main_window)
        self.box_name_x.place(x=55, y=20, width=80)

        self.labe_name = ttk.Label(main_window, text="Y - ")
        self.labe_name.place(x=150, y=20)
        
        self.box_name_y = ttk.Entry(main_window)
        self.box_name_y.place(x=175, y=20, width=80)

        self.labe_name = ttk.Label(main_window, text="S - ")
        self.labe_name.place(x=270, y=20)
        
        self.box_name_i = ttk.Entry(main_window)
        self.box_name_i.place(x=295, y=20, width=80)

        self.labe_mouse = ttk.Label(main_window, text="---")
        self.labe_mouse.place(x=200, y=65, anchor=CENTER)

        self.boton_Inicio = ttk.Button(main_window, text="Inicio", command=self.Iniciar)
        self.boton_Inicio.place(x=20, y=80, width=160)

        self.boton_Stop = ttk.Button(main_window, text="Stop", command=self.Stop)
        self.boton_Stop.place(x=220, y=80, width=160)

        self.labe_ajuste = ttk.Label(main_window, text="Detenido", font='Arial 13 bold')
        self.labe_ajuste.place(x=200, y=150, anchor=CENTER)
        
    def Reiniciar(self):
        global condition
        condition=True
        if (condition):
            self.labe_ajuste.config(text= "Iniciar")
            ventana.after(3000, inicio, int(self.box_name_x.get()), int(self.box_name_y.get()), int(self.box_name_i.get())*1000)

    def Iniciar(self):
        global condition
        global window
        condition=True
        if (condition):
            window = win32gui.WindowFromPoint((80, 80))
            self.labe_ajuste.config(text= "Iniciado")
            ventana.after(3000, inicio, int(self.box_name_x.get()), int(self.box_name_y.get()), int(self.box_name_i.get())*1000)

    def Stop(self):
        global condition
        condition=False
        self.labe_ajuste.config(text= f"Detenido")

app = Aplicacion(ventana)
ventana.mainloop()


