import sys
import getopt
import Tkinter as tk
import tkMessageBox
from sys import argv
from os.path import exists
from tkFileDialog import *
import binascii
import struct



class GUI(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("Ultimate Smasher")
		self.geometry("500x300")
	
		#Open and Save Buttons
		self.btn_opensavefile = tk.Button(text="Open File", command=self.openfile)
		self.btn_opensavefile.pack(side=tk.TOP, fill=tk.X)
		
		self.btn_savefile = tk.Button(text="Save File", command=self.savefile)
		self.btn_savefile.pack(side=tk.BOTTOM, fill=tk.X)
		
		#SP
		self.sp=tk.IntVar()
		self.lbl_sp = tk.Label(text = "SP")
		self.lbl_sp.place(x=20,y=50)
		self.txtbx_sp=tk.Entry(self, width=9, textvariable=self.sp)
		self.txtbx_sp.place(x=90, y=50)
		self.btn_checksp = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checksp)
		self.btn_checksp.place(x=170,y=47)
		
		#Gold
		self.gold=tk.IntVar()
		self.lbl_gold = tk.Label(text = "Gold")
		self.lbl_gold.place(x=20,y=100)
		self.txtbx_gold=tk.Entry(self, width=9, textvariable=self.gold)
		self.txtbx_gold.place(x=90, y=100)
		self.btn_checkgold = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checkgold)
		self.btn_checkgold.place(x=170,y=97)

		#Hammers
		self.hammers=tk.IntVar()
		self.lbl_hammers = tk.Label(text = "Hammers")
		self.lbl_hammers.place(x=20,y=150)
		self.txtbx_hammers=tk.Entry(self, width=9, textvariable=self.hammers)
		self.txtbx_hammers.place(x=90, y=150)
		self.btn_checkhammers = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checkhammers)
		self.btn_checkhammers.place(x=170,y=147)
		
		#Tickets
		self.tickets=tk.IntVar()
		self.lbl_tickets = tk.Label(text = "Tickets")
		self.lbl_tickets.place(x=20,y=200)
		self.txtbx_tickets=tk.Entry(self, width=9, textvariable=self.tickets)
		self.txtbx_tickets.place(x=90, y=200)
		self.btn_checktickets = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checktickets)
		self.btn_checktickets.place(x=170,y=197)
		
		#Snack (S)
		self.snacks=tk.IntVar()
		self.lbl_snacks = tk.Label(text = "Snack (S)")
		self.lbl_snacks.place(x=300,y=50)
		self.txtbx_snacks=tk.Entry(self, width=9, textvariable=self.snacks)
		self.txtbx_snacks.place(x=370, y=50)
		self.btn_checksnacks = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checksnacks)
		self.btn_checksnacks.place(x=450,y=47)
		
		#Snack (M)
		self.snackm=tk.IntVar()
		self.lbl_snackm = tk.Label(text = "Snack (M)")
		self.lbl_snackm.place(x=300,y=100)
		self.txtbx_snackm=tk.Entry(self, width=9, textvariable=self.snackm)
		self.txtbx_snackm.place(x=370, y=100)
		self.btn_checksnackm = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checksnackm)
		self.btn_checksnackm.place(x=450,y=97)

		#Snack (L)
		self.snackl=tk.IntVar()
		self.lbl_snackl = tk.Label(text = "Snack (L)")
		self.lbl_snackl.place(x=300,y=150)
		self.txtbx_snackl=tk.Entry(self, width=9, textvariable=self.snackl)
		self.txtbx_snackl.place(x=370, y=150)
		self.btn_checksnackl = tk.Button(self, text=u'\u2713',width=2, height=1, command=self.checksnackl)
		self.btn_checksnackl.place(x=450,y=147)
		
		#Roster
		self.btn_unlockroster = tk.Button(self, text="Unlock Roster", command=self.unlockroster)
		self.btn_unlockroster.place(x=300,y=197)

	def openfile(self):
		filename = askopenfilename(initialfile="system_data.bin")
		f = open(filename, "r+b").read()
		print (binascii.hexlify(f))
		global h
		h=(binascii.hexlify(f))
		tkMessageBox.showinfo(title="", message="Savefile loaded")
		
		#Fills every box with its data
		if "h" in globals():
			
			#SP
			sp=(binascii.hexlify(f[0x4831e4:0x4831e8]))
			sp1=(binascii.unhexlify(sp))
			sp2= struct.unpack("<L",sp1)
			self.txtbx_sp.delete(0,"end")
			self.txtbx_sp.insert(tk.END,sp2)
			
			#Gold
			gold=(binascii.hexlify(f[0x5506dc:0x5506e0]))
			gold1=(binascii.unhexlify(gold))
			gold2= struct.unpack("<L",gold1)
			self.txtbx_gold.delete(0,"end")
			self.txtbx_gold.insert(tk.END,gold2)
			
			#Snack (S)
			snacks=(binascii.hexlify(f[0x4831CE:0x4831D0]))
			snacks1=(binascii.unhexlify(snacks))
			snacks2= struct.unpack("<H",snacks1)
			self.txtbx_snacks.delete(0,"end")
			self.txtbx_snacks.insert(tk.END,snacks2)
			
			#Snack (M)
			snackm=(binascii.hexlify(f[0x4831D0:0x4831D2]))
			snackm1=(binascii.unhexlify(snackm))
			snackm2= struct.unpack("<H",snackm1)
			self.txtbx_snackm.delete(0,"end")
			self.txtbx_snackm.insert(tk.END,snackm2)
			
			#Snack (L)
			snackl=(binascii.hexlify(f[0x4831D2:0x4831D4]))
			snackl1=(binascii.unhexlify(snackl))
			snackl2= struct.unpack("<H",snackl1)
			self.txtbx_snackl.delete(0,"end")
			self.txtbx_snackl.insert(tk.END,snackl2)
			
			#Hammers
			hammers=(binascii.hexlify(f[0x555E5C:0x555E5D]))
			hammers1=(binascii.unhexlify(hammers))
			hammers2= struct.unpack("<B",hammers1)
			self.txtbx_hammers.delete(0,"end")
			self.txtbx_hammers.insert(tk.END,hammers2)
			
			#Tickets
			tickets=(binascii.hexlify(f[0x5506CC:0x5506CD]))
			tickets1=(binascii.unhexlify(tickets))
			tickets2= struct.unpack("<B",tickets1)
			self.txtbx_tickets.delete(0,"end")
			self.txtbx_tickets.insert(tk.END,tickets2)			

			
	def savefile(self):
		savedir = asksaveasfile(mode='wb', defaultextension='.bin', initialfile="system_data")
		if savedir is None:
			return
		savedir.write(binascii.unhexlify(h))
		savedir.close()
		tkMessageBox.showinfo(title="", message="File saved")
			
	#Checks for each value to notify of possible save corruption and applies the textbox value
	def checksp(self):
		sp = int(self.sp.get())
		if sp <= 0xFFFFFFFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			sp1 = binascii.hexlify(struct.pack("<I",sp))
			print sp1
			global h
			h=h[:0x4831e4*2]+sp1+h[0x4831e8*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")

			
	def checkgold(self):
		gold = int(self.gold.get())
		if gold <= 0xFFFFFFFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			gold1 = binascii.hexlify(struct.pack("<I",gold))
			print gold1
			global h
			h=h[:0x5506dc*2]+gold1+h[0x5506e0*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")

		
	def checksnacks(self):
		snacks = int(self.snacks.get())
		if snacks <= 0xFFFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			snacks1 = binascii.hexlify(struct.pack("<H",snacks))
			print snacks1
			global h
			h=h[:0x4831CE*2]+snacks1+h[0x4831D0*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")
		
		
	def checksnackm(self):
		snackm = int(self.snackm.get())
		if snackm <= 0xFFFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			snackm1 = binascii.hexlify(struct.pack("<H",snackm))
			print snackm1
			global h
			h=h[:0x4831D0*2]+snackm1+h[0x4831D2*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")
		
		
	def checksnackl(self):
		snackl = int(self.snackl.get())
		if snackl <= 0xFFFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			snackl1 = binascii.hexlify(struct.pack("<H",snackl))
			print snackl1
			global h
			h=h[:0x4831D2*2]+snackl1+h[0x4831D4*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")
	
	
	def checkhammers(self):
		hammers = int(self.hammers.get())
		if hammers <= 0xFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			hammers1 = binascii.hexlify(struct.pack("<B",hammers))
			print hammers1
			global h
			h=h[:0x555E5C*2]+hammers1+h[0x555E5D*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")

	
	def checktickets(self):
		tickets = int(self.tickets.get())
		if tickets <= 0xFF:
			tkMessageBox.showinfo(title="OK", message="The value is valid.")
			tickets1 = binascii.hexlify(struct.pack("<B",tickets))
			print tickets1
			global h
			h=h[:0x555E5C*2]+tickets1+h[0x555E5D*2:]
		else:
			tkMessageBox.showerror(title="ERROR", message="The value is too big!")
	
	
	def unlockroster(self):
			tkMessageBox.showinfo(title="OK", message="Roster unlocked!")
			rosterhex="0100000001000000A52D00000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000C0000000100000001000000010000000D0000000100000001000000010000000400000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000050000000100000001000000010000000000000001000000010000000100000000000000010000000100D9000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000600000001000000010000000100000009000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000E000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000005000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001000000010000000000000001000000010000000100000000000000010000000100000001000000000000000100000001"
			global h
			h=h[:0x53FF30*2]+rosterhex+h[0x540255*2:]

	
	
	
gui = GUI()
gui.resizable(False, False)
gui.iconbitmap("icon.ico")
gui.mainloop()
sys.exit()
