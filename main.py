import tkinter as tk
import search
import register
temp = None
def reg():
	temp.destroy()
	register.mainfunc()
	mainfunc()
def srch():
	temp.destroy()
	search.mainfunc()
	mainfunc()
def mainfunc():
	global temp
	main_window = tk.Tk()
	temp = main_window
	main_window.resizable(False, False)
	main_window.title("E-Лозуватка")
	main_window.geometry("300x200")
	main_menu = tk.Menu(main_window)
	main_window["menu"] = main_menu
	m1 = tk.Menu(main_menu)
	main_menu.add_cascade(label="Житель", menu=m1)
	m1.add_command(label="Новий", command=reg)
	m1.add_command(label='Пошук', command=srch)
	lbl1 = tk.Label(main_window, text="Е-Лозуватка", font="Arial 26 bold")
	lbl1.place(x=37, y=60)
	main_window.mainloop()
mainfunc()