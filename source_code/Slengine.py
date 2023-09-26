
from tkinter import *

class Slider(object):
	def __init__(self,title,settings,orient=True):
		self.title    = title
		self.settings = settings
		self.orient   = HORIZONTAL
		if not(orient):
			self.orient = VERTICAL
		self.length   = "default" 

def sliders_to_values(sliders,root):
	arr = []
	for s in sliders:
		arr.append(s.get())
	root.destroy()
	return arr

def create_window(info, return_function, window_size=(800,600), title="Slengine", scheme="classic"):
	root = Tk()
	root.title(title)
	root.minsize(window_size[0],window_size[1])
	root.geometry(f"{window_size[0]}x{window_size[1]+10}+0+0")
	root.configure(bg="#222222")

	frmMain = Frame(root, bg="#222222")

	frmMain.grid(row=0, column=0, columnspan=2, rowspan=len(info), sticky="NESW")
	for i in range(len(info)):
		frmMain.grid_rowconfigure(i, weight=1)
		root.grid_rowconfigure(i, weight=1)
	frmMain.grid_columnconfigure(0, weight=1)
	frmMain.grid_columnconfigure(1, weight=1)
	root.grid_columnconfigure(0, weight=1)
	root.grid_columnconfigure(1, weight=1)

	labels  = []
	sliders = []
	count = 0
	for element in info:
		label = Label(frmMain, 
			text=element.title,
			bg="#222222",
			fg="white",
			font=("Courier", 16),

		)
		if count%2==0:
			label.grid(column=0, row=count,padx=20)
		else:
			label.grid(column=1, row=count-1,padx=20)
		labels.append(label)
		slid_length = window_size[0]
		slid_height = (window_size[1]/(len(info))) - 25
		slider = Scale(frmMain, 
			from_=element.settings[0], 
			to=element.settings[1], 
			orient=element.orient, 
			resolution=element.settings[2],
			sliderrelief="flat",
			sliderlength=slid_length/5,
			length=slid_length - 50,
			bg="#333333",
			fg="white",
			troughcolor="#555555",
			highlightbackground="#222222",
			width=slid_height,
			cursor="hand2",
			font=("Courier", 14)
		)
		if count%2==0:
			slider.grid(column=0, row=count+1,padx=20)
		else:
			slider.grid(column=1, row=count,padx=20)
		count += 1
		sliders.append(slider)

	Button(frmMain, 
		text='Enter', 
		relief="flat",
		bg="white",
		fg="#333333",
		width=10,
		cursor="hand2",
		font=("Courier", 18),
		command=lambda: return_function(sliders_to_values(sliders,root))
	).grid(columnspan=2, row=count+2, pady=10)

	root.mainloop()
	return
