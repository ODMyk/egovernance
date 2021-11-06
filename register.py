import tkinter as tk
import json
import sys

PATH = f"{sys.argv[0]}\\.."
temp = [None, None, None]
FONT = "Arial 16"

def register():
	global temp
	with open(f"{PATH}\\data.json", 'r') as f:
		peoples = json.loads(f.read())

	person = {"surname": temp[1].get()}
	peoples.append(person)

	window = temp[0]
	window.title("Е-Лозуватка: довідка про реєстрацію")
	for el in temp[2]:
		el.destroy()

	text = f"""
Особа {person['surname']}
була успішно
зареєтрована
"""
	label = tk.Label(window, text=text, font=FONT)
	label.place(x=15, y=45)

	with open(f"{PATH}\\data.json", 'w') as f:
		f.write(json.dumps(peoples, indent=4))

def mainfunc():
	global temp
	window = tk.Tk()
	temp[0] = window
	window.resizable(False, False)
	window.title("E-Лозуватка: реєстрація жителя")
	window.geometry("300x200")

	lbl1 = tk.Label(text="Прізвище:", font=FONT)
	lbl1.place(x=50, y=50)
	field = tk.Entry(window)
	temp[1] = field
	field.place(x=50, y=80)
	button1 = tk.Button(window, text="Зареєструвати", font=FONT, command=register)
	button1.place(x=50, y=110)
	temp[2] = (lbl1, field, button1)

	window.mainloop()
