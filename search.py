import tkinter as tk
import json
import sys

PATH = f"{sys.argv[0]}\\.."
FONT = "Arial 16"
temp = [None, None, None]
i = 0

def search(event):
	global temp, i
	if temp[1]:
		try:
			temp[1].destroy()
		except:
			pass
		temp[1] = None

	surname = temp[2].get()
	window2 = tk.Toplevel(temp[0])
	temp[1] = window2
	window2.title("Е-Лозуватка: результат пошуку")
	window2.geometry("300x200")
	window2.resizable(False, False)

	with open(f"{PATH}\\data.json", 'r') as f:
		peoples = json.loads(f.read())
	finded = []
	
	for people in peoples:
		if people['surname'] == surname:
			finded.append(people)

	if len(finded) == 0:
		label = tk.Label(window2, text="Нічого не знайдено", font=FONT)
		label.place(x=50, y=50)
	else:
		i = 0

		def nxt():
			global i
			if i != len(finded):
				i += 1
			else:
				i = 1
			label_c.config(text=f"{i}/{len(finded)}")
			label_b.config(text=finded[i-1]["surname"])

		def prev():
			global i
			if i != 1:
				i -= 1
			else:
				i = len(finded)
			label_c.config(text=f"{i}/{len(finded)}")
			label_b.config(text=finded[i-1]["surname"])

		label_c = tk.Label(window2, text="", font=FONT)
		label_a = tk.Label(window2, text="Прізвище:", font=FONT)
		label_b = tk.Label(window2, text="", font=FONT)
		label_c.place(x=125, y=20)
		label_a.place(x=20, y=50)
		label_b.place(y=50, x=120)
		button_next = tk.Button(window2, text="→", command=nxt)
		button_prev = tk.Button(window2, text="←", command=prev)
		button_prev.place(y=80, x=115)
		button_next.place(y=80, x=145)
		nxt()

def mainfunc():
	global temp
	window = tk.Tk()
	temp[0] = window
	window.resizable(False, False)
	window.title("E-Лозуватка: пошук жителя")
	window.geometry("300x200")

	lbl1 = tk.Label(text="Прізвище:", font=FONT)
	lbl1.place(x=50, y=50)
	field = tk.Entry(window)
	temp[2] = field
	field.place(x=50, y=80)
	field.bind('<Return>', search)
	button1 = tk.Button(window, text="Знайти", font=FONT)
	button1.bind("<Button-1>", search)
	button1.place(x=50, y=110)

	window.mainloop()
