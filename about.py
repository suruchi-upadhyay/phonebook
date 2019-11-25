import tkinter as Tk

class About_Window(object):

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title("About Us")

		# Team Cowsay logo
		self.photo = Tk.PhotoImage(master = top, file = "GUI/logo.gif")
		self.photo_label = Tk.Label(top, image = self.photo)
		self.photo_label.grid(row = 0, column = 0)

		# Application information