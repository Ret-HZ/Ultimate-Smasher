# -*- coding: utf-8 -*-
import sys, os
import getopt
from os.path import exists
import binascii
import struct
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import functools



class App(QMainWindow):

	def __init__(self):
		super().__init__()
		global dir
		dir="img/"
		#dir=sys._MEIPASS+"/"
		self.title = "Ultimate Smasher 2.0-alpha1"
		self.setWindowIcon(QIcon(dir+'icon.ico'))
		width = 580
		height = 240
		qtRectangle = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())
		self.width = width
		self.height = height
		self.setFixedSize(width,height)
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)


		#########################################
		#				MENUBAR					#
		#########################################

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		helpMenu = menubar.addMenu('&Help')

		fileMenu_open = QAction(QIcon(dir+'open_file.png'), '&Open', self)
		fileMenu_open.setShortcut('Ctrl+O')
		fileMenu_open.setStatusTip('Open File')
		fileMenu_open.triggered.connect(self.openfile)

		fileMenu_save = QAction(QIcon(dir+'save_file.png'), '&Save', self)
		fileMenu_save.setShortcut('Ctrl+S')
		fileMenu_save.setStatusTip('Save File')
		fileMenu_save.triggered.connect(self.savefile)

		fileMenu_exit = QAction(QIcon(dir+'exit.png'), '&Exit', self)
		fileMenu_exit.setShortcut('Ctrl+Q')
		fileMenu_exit.setStatusTip('Exit')
		fileMenu_exit.triggered.connect(qApp.quit)

		helpMenu_usage = QAction(QIcon(dir+'help.png'), '&How to use', self)
		helpMenu_usage.setShortcut('Ctrl+H')
		helpMenu_usage.setStatusTip('How to use')
		helpMenu_usage.triggered.connect(self.show_howto)

		helpMenu_about = QAction(QIcon(dir+'about.png'), '&About', self)
		helpMenu_about.setStatusTip('About')
		helpMenu_about.triggered.connect(self.show_about)

		fileMenu.addAction(fileMenu_open)
		fileMenu.addAction(fileMenu_save)
		fileMenu.addAction(fileMenu_exit)
		helpMenu.addAction(helpMenu_usage)
		helpMenu.addAction(helpMenu_about)

		#########################################
		#				TOOLBAR					#
		#########################################

		toolbar = self.addToolBar("File")
		toolbar.setMovable(False)

		toolbar_openfile = QAction(QIcon(dir+"open_file.png"),"Open File",self)
		toolbar_openfile.triggered.connect(self.openfile)

		toolbar_savefile = QAction(QIcon(dir+"save_file.png"),"Save File",self)
		toolbar_savefile.triggered.connect(self.savefile)

		toolbar.addAction(toolbar_openfile)
		toolbar.addAction(toolbar_savefile)


		#########################################
		#				TABS					#
		#########################################

		centralWidget = QWidget(self)
		centralWidgetLayout = QVBoxLayout(centralWidget)
		centralWidget.setLayout(centralWidgetLayout)

		tabContainer = QTabWidget(centralWidget)

		tab1 = QWidget(tabContainer)
		tab2 = QWidget(tabContainer)
		tab3 = QWidget(tabContainer)
		tab4 = QWidget(tabContainer)
		tab5 = QWidget(tabContainer)

		tab1layout = QVBoxLayout(tab1)

		tabContainer.setLayout(tab1layout)

		tabContainer.addTab(tab1, "General")
		tabContainer.addTab(tab2, "Items")
		tabContainer.addTab(tab3, "Characters")
		tabContainer.addTab(tab4, "Adventure Mode")
		tabContainer.addTab(tab5, "Stats")
		tabContainer.setCurrentIndex(0)
		tabContainer.setTabEnabled(3,False)  #WIP
		centralWidgetLayout.addWidget(tabContainer)
		self.setCentralWidget(centralWidget)


		#########################################
		#				BUTTONS					#
		#########################################
		def showSprite(tab,image,x,y):
			sprite = QLabel(tab)
			spr=QPixmap(image)
			spr2=spr.scaled(20,20,Qt.KeepAspectRatio)
			sprite.setPixmap(spr2)
			sprite.move(x,y)
			sprite.show()


		#GENERAL#

		btn_language = QPushButton('Language', tab1)
		btn_language.setToolTip('Change the current language')
		btn_language.move(35,30)
		btn_language.clicked.connect(self.inputLanguage)

		btn_gold = QPushButton('Gold', tab1)
		btn_gold.setToolTip('Gold amount')
		btn_gold.move(135,30)
		btn_gold.clicked.connect(self.inputGold)

		btn_sp = QPushButton('SP', tab1)
		btn_sp.setToolTip('SP amount')
		btn_sp.move(235,30)
		btn_sp.clicked.connect(self.inputSP)

		btn_hammers = QPushButton('Hammers', tab1)
		btn_hammers.setToolTip('Hammers amount')
		btn_hammers.move(335,30)
		btn_hammers.clicked.connect(self.inputHammers)

		btn_tickets = QPushButton('Tickets', tab1)
		btn_tickets.setToolTip('Ticket amount')
		btn_tickets.move(435,30)
		btn_tickets.clicked.connect(self.inputTickets)

		btn_milestones = QPushButton('Milestones', tab1)
		btn_milestones.setToolTip('Unlocks all Milestones')
		btn_milestones.move(35,90)
		btn_milestones.clicked.connect(self.unlockmilestones)

		btn_miiclothes = QPushButton('Mii Clothes', tab1)
		btn_miiclothes.setToolTip('Unlocks all Mii Clothes')
		btn_miiclothes.move(135,90)
		btn_miiclothes.clicked.connect(self.unlockmiiclothes)

		btn_cores = QPushButton('Cores', tab1)
		btn_cores.setToolTip('Unlocks all Cores')
		btn_cores.move(235,90)
		#btn_cores.clicked.connect()
		btn_cores.setEnabled(False)

		btn_spirits = QPushButton('Spirits', tab1)
		btn_spirits.setToolTip('Unlocks all Spirits')
		btn_spirits.move(335,90)
		#btn_spirits.clicked.connect()
		btn_spirits.setEnabled(False)

		btn_spiritboard = QPushButton('Spirit Board', tab1)
		btn_spiritboard.setToolTip('Unlocks all Spirit Board slots')
		btn_spiritboard.move(435,90)
		#btn_spiritboard.clicked.connect()
		btn_spiritboard.setEnabled(False)


		#ITEMS#

		showSprite(tab2,dir+"snacks.png",10,20)
		showSprite(tab2,dir+"snackm.png",10,60)
		showSprite(tab2,dir+"snackl.png",10,100)
		showSprite(tab2,dir+"shuffle.png",120,21)
		showSprite(tab2,dir+"allprimaries.png",120,61)
		showSprite(tab2,dir+"allsupports.png",120,101)
		showSprite(tab2,dir+"rematch.png",230,21)
		showSprite(tab2,dir+"filler.png",230,61)
		showSprite(tab2,dir+"damage50.png",230,101)
		showSprite(tab2,dir+"slowfscharging.png",340,21)
		showSprite(tab2,dir+"weakenminions.png",340,61)
		showSprite(tab2,dir+"healthdrain.png",340,101)
		showSprite(tab2,dir+"disableitems.png",450,21)
		showSprite(tab2,dir+"shieldspacer.png",450,61)
		showSprite(tab2,dir+"sluggishshield.png",450,101)


		btn_snackS = QPushButton('Snack (S)', tab2)
		btn_snackS.setToolTip('Snack (S) amount')
		btn_snackS.move(30,20)
		btn_snackS.clicked.connect(self.inputSnackS)

		btn_snackM = QPushButton('Snack (M)', tab2)
		btn_snackM.setToolTip('Snack (M) amount')
		btn_snackM.move(30,60)
		btn_snackM.clicked.connect(self.inputSnackM)

		btn_snackL = QPushButton('Snack (L)', tab2)
		btn_snackL.setToolTip('Snack (L) amount')
		btn_snackL.move(30,100)
		btn_snackL.clicked.connect(self.inputSnackL)

		btn_shuffleAll = QPushButton('Shuffle All', tab2)
		btn_shuffleAll.setToolTip('Shuffle All amount')
		btn_shuffleAll.move(140,20)
		btn_shuffleAll.clicked.connect(self.inputShuffleAll)

		btn_allPrimaries = QPushButton('All Primaries', tab2)
		btn_allPrimaries.setToolTip('Shuffle All amount')
		btn_allPrimaries.move(140,60)
		btn_allPrimaries.clicked.connect(self.inputAllPrimaries)

		btn_allSupports = QPushButton('All Supports', tab2)
		btn_allSupports.setToolTip('Shuffle All amount')
		btn_allSupports.move(140,100)
		btn_allSupports.clicked.connect(self.inputAllSupports)

		btn_rematch = QPushButton('Rematch', tab2)
		btn_rematch.setToolTip('Rematch amount')
		btn_rematch.move(250,20)
		btn_rematch.clicked.connect(self.inputRematch)

		btn_filler = QPushButton('Filler', tab2)
		btn_filler.setToolTip('Filler amount')
		btn_filler.move(250,60)
		btn_filler.clicked.connect(self.inputFiller)

		btn_damage50 = QPushButton('Damage 50%', tab2)
		btn_damage50.setToolTip('Damage 50% amount')
		btn_damage50.move(250,100)
		btn_damage50.clicked.connect(self.inputDamage50)

		btn_slowFSCharging = QPushButton('Slow FS Chrg.', tab2)
		btn_slowFSCharging.setToolTip('Slow FS Charging amount')
		btn_slowFSCharging.move(360,20)
		btn_slowFSCharging.clicked.connect(self.inputSlowFSCharging)

		btn_weakenMinions = QPushButton('Wkn. Minions', tab2)
		btn_weakenMinions.setToolTip('Weak. Minions amount')
		btn_weakenMinions.move(360,60)
		btn_weakenMinions.clicked.connect(self.inputWeakenMinions)

		btn_healthDrain = QPushButton('Health Drain', tab2)
		btn_healthDrain.setToolTip('Health Drain amount')
		btn_healthDrain.move(360,100)
		btn_healthDrain.clicked.connect(self.inputHealthDrain)

		btn_disableItems = QPushButton('Disable Items', tab2)
		btn_disableItems.setToolTip('Disable Items amount')
		btn_disableItems.move(470,20)
		btn_disableItems.clicked.connect(self.inputDisableItems)

		btn_shieldSpacer = QPushButton('Shield Spacer', tab2)
		btn_shieldSpacer.setToolTip('Shield Spacer amount')
		btn_shieldSpacer.move(470,60)
		btn_shieldSpacer.clicked.connect(self.inputShieldSpacer)

		btn_sluggishShield = QPushButton('Sluggish Shld.', tab2)
		btn_sluggishShield.setToolTip('Sluggish Shield amount')
		btn_sluggishShield.move(470,100)
		btn_sluggishShield.clicked.connect(self.inputSluggishShield)


		#CHARACTERS#
		btn_charmenu = QPushButton('Character Menu', tab3)
		btn_charmenu.setToolTip('(Un)Lock specific characters')
		btn_charmenu.move(235,60)
		btn_charmenu.clicked.connect(self.show_charmenu)


		#ADVENTURE MODE#


		#STATS#
		btn_combined = QPushButton('Combined', tab5)
		btn_combined.setToolTip('"Combined" Stat Section')
		btn_combined.move(35,30)
		btn_combined.clicked.connect(lambda: self.show_statwindow("Combined"))

		btn_combined = QPushButton('Smash', tab5)
		btn_combined.setToolTip('"Smash" Stat Section')
		btn_combined.move(235,30)
		btn_combined.clicked.connect(lambda: self.show_statwindow("Smash"))

		btn_combined = QPushButton('Spirits', tab5)
		btn_combined.setToolTip('"Spirits" Stat Section')
		btn_combined.move(435,30)
		btn_combined.clicked.connect(lambda: self.show_statwindow("Spirits"))

		btn_combined = QPushButton('Games && More', tab5)
		btn_combined.setToolTip('"Games & More" Stat Section')
		btn_combined.move(35,90)
		btn_combined.clicked.connect(lambda: self.show_statwindow("Games & More"))

		btn_combined = QPushButton('Vault', tab5)
		btn_combined.setToolTip('"Vault" Stat Section')
		btn_combined.move(235,90)
		btn_combined.clicked.connect(lambda: self.show_statwindow("Vault"))

		btn_combined = QPushButton('Online', tab5)
		btn_combined.setToolTip('"Online" Stat Section')
		btn_combined.move(435,90)
		btn_combined.clicked.connect(lambda: self.show_statwindow("Online"))


		comboBox = QComboBox(tab4)
		comboBox.addItem("Slot 1")
		comboBox.addItem("Slot 2")
		comboBox.addItem("Slot 3")
		comboBox.move(50, 50)
		#comboBox.activated.activated[str].connect(self.slot_select)


		self.show()




#Value Inputs
	@pyqtSlot()
	def openfile(self):
		filename = QFileDialog.getOpenFileName(self, 'Open File', 'system_data.bin',"Binary files (*.bin)")
		if filename[0] is '':
			return
		if (os.path.getsize(filename[0])==5982968): #Filesize check
			f = open(filename[0], "rb").read()
			global h
			h=(binascii.hexlify(f))
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Not a valid savefile!")
			msg.setWindowTitle("Not valid")
			msg.setWindowIcon(QIcon(dir+'icon.ico'))
			msg.exec_()


	def savefile(self):
		if self.checkforsave():
			savedir = QFileDialog.getSaveFileName(self, 'Save File', 'system_data.bin',"Binary files (*.bin)")
			if savedir[0] is '':
				return
			file = open(savedir[0],"wb")
			file.write(binascii.unhexlify(h))
			file.close()

	#Check if a savefile is open
	def checkforsave(self):
		if "h" in globals():
			return True
		else:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Open a <b>Save File</b> first!")
			msg.setWindowTitle("No Save File")
			msg.setWindowIcon(QIcon(dir+'icon.ico'))
			msg.exec_()
			return False


	def show_howto(self):
		global dir
		howto = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
		howto.setWindowTitle("How To Use")
		howto.setWindowIcon(QIcon(dir+'help.png'))
		width=360
		height=160
		howto.resize(width,height)
		howto.setFixedSize(width,height)
		howto.setWindowModality(Qt.ApplicationModal)

		l1=QLabel()
		l2=QLabel()

		l1.setText("<center><b>HOW TO USE</b><br><br></center>")
		l2.setText("<ul><li>1. Dump your save with your preferred save manager</li><li>2. Open your save (system_data.bin)</li><li>3. Edit stuff to your liking</li><li>4. Save it (Ctrl + S)</li><li>5. Overwrite your save with the one you just edited</li><li>6. That's it!</li></ul>")
		
		
		l1.setAlignment(Qt.AlignLeft)
		l2.setAlignment(Qt.AlignLeft)
		

		vbox = QVBoxLayout()
		vbox.addWidget(l1)
		vbox.addWidget(l2)
		vbox.addStretch()
		howto.setLayout(vbox)
		howto.exec_()


	def show_about(self):
		global dir
		about = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
		about.setWindowTitle("About")
		about.setWindowIcon(QIcon(dir+'about.png'))
		width=420
		height=300
		about.resize(width,height)
		about.setFixedSize(width,height)
		about.setWindowModality(Qt.ApplicationModal)

		l1=QLabel()
		l1.setText("<b>THIS SOFTWARE MUST NOT BE SOLD,<br>NEITHER ALONE NOR AS PART OF A BUNDLE.<br><br>IF YOU PAID FOR THIS SOFTWARE OR RECEIVED<br>IT AS PART OF A BUNDLE FOLLOWING PAYMENT,<br>YOU HAVE BEEN SCAMMED AND SHOULD<br>DEMAND YOUR MONEY BACK IMMEDIATELY.</b><br>")
		l1.setAlignment(Qt.AlignCenter)
		l2=QLabel()
		l2.setText("Created by: <a href=\"https://github.com/CapitanRetraso\"><b>Capitán Retraso</b></a>")
		l2.setOpenExternalLinks(True)
		l2.setAlignment(Qt.AlignLeft)
		l3=QLabel()
		l3.setText("<br>Special Thanks: <a href=\"https://gbatemp.net/members/stoned.347253\">Stoned</a>")
		l3.setOpenExternalLinks(True)
		l3.setAlignment(Qt.AlignLeft)
		l4=QLabel()
		l4.setText("<a href=\"https://github.com/CapitanRetraso/Ultimate-Smasher/issues\"><b>Report a problem</b></a>")
		l4.setOpenExternalLinks(True)
		l4.setAlignment(Qt.AlignRight)
		l5=QLabel()
		l5.setText("<b>DISCLAIMER</b><br> This tool can damage your savegame or cause a ban if not used correctly.<br><b>By using it you are responsible for any data lost or ban.</b><br>Be careful when editing your savegame and always keep a clean backup.")
		l5.setAlignment(Qt.AlignCenter)

		vbox = QVBoxLayout()
		vbox.addWidget(l1)
		vbox.addStretch()
		vbox.addWidget(l5)
		vbox.addStretch()
		vbox.addWidget(l2)
		vbox.addWidget(l3)
		vbox.addWidget(l4)
		about.setLayout(vbox)

		about.exec_()


	def show_statwindow(self,category):
		if self.checkforsave():
			statwindow = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
			statwindow.setWindowTitle("Stats - "+category)
			statwindow.setWindowIcon(QIcon(dir+'icon.ico'))
			width=550
			height=400
			statwindow.resize(width,height)
			statwindow.setFixedSize(width,height)
			self.layout = QVBoxLayout()



			if (category == "Combined"):
				statNames=['Power-On Count','Smash Bros. Powered Time Count','Play Time (seconds)','Local Wireless Battles Fought','Time Battles Fought','Stock Battles Fought','Stamina Battles Fought','Battles Fought with 5 or more people','Battles Fought with 8 people','Vs. Play Contestants','Battles Cut Short','Total Damage','KOs','Self-Destructs']
				statOffsets=[0x540258,0x54025C,0x540260,0x540264,0x540268,0x54026C,0x540270,0x540274,0x540278,0x54027C,0x540280,0x540284,0x540288,0x54028C]

			elif (category == "Smash"):
				statNames=['Smash Play Time (seconds)','Collective Smash Play Time (seconds)','Standard Smash Battles Fought','Squad Strikes Battles Fought','Custom Smash Battles Fought','Super Sudden Death Battles Fought','Smashdown Battles Fought','Tourney Battles Fought']
				statOffsets=[0x54029C,0x5402A0,0x5402A4,0x5402A8,0x5402AC,0x5402B0,0x5402B4,0x5402B8]

			elif (category == "Spirits"):
				statNames=['Spirits Summoned','Spirits Dismissed','Spirits Enhanced','Lv.99 Spirits','Adventure Wins','Times Adventure Completed','Styles Mastered in the Dojo','Time Spent Training at the Gym (seconds)','Spirit Exploration Time (seconds)','Spirit Board Battles Won']
				statOffsets=[0x5402C0,0x5402C4,0x5402C8,0x5402CC,0x5402D4,0x5402D8,0x5402DC,0x5402E0,0x5402E4,0x5402D0]

			elif (category == "Games & More"):
				statNames=['Classic Mode Clears','Bonus Game High Score','Credits High Score','Mii Fighters Customized']
				statOffsets=[0x5402E8,0x5402F0,0x5402F4,0x5402FC]

			elif (category == "Vault"):
				statNames=['Snapshots Taken','Replays Recorded','Videos Created','Smash Tags Claimed']
				statOffsets=[0x54030C,0x540310,0x540314,0x540318]

			elif (category == "Online"):
				statNames=['Online Play Time','Solo Quickplay Battles','Solo Quickplay Wins','Highest Global Smash Power','Highest Total Global Smash Power','Co-op Quickplay Battles','Co-op Quickplay Wins','Elite Quickplay Battles','Elite Quickplay Wins','Arena Battles']
				statOffsets=[0x540320,0x540324,0x540328,0x54032C,0x540330,0x540334,0x540338,0x54033C,0x540340,0x540344]


			self.tableWidget = QTableWidget()
			self.tableWidget.setColumnCount(2)
			self.tableWidget.setRowCount(len(statNames))

			for x in range (len(statOffsets)):
				self.tableWidget.setItem(x,0, QTableWidgetItem(statNames[x]))
				self.tableWidget.setItem(x,1, QTableWidgetItem(str(self.readFromPosition(statOffsets[x],statOffsets[x]+4,"<L"))))

			def writeStats():
				for x in range (len(statOffsets)):
					value=int(self.tableWidget.item(x,1).text())
					if (value <= 0x3B9AC9FF):
						self.writeToPosition(value,statOffsets[x],statOffsets[x]+4,"<L")
					else:
						msg = QMessageBox()
						msg.setIcon(QMessageBox.Warning)
						msg.setText("One or more values are too high!")
						msg.setWindowTitle("Error")
						msg.exec_()
						return
					

					if (x == len(statOffsets)-1):
						statwindow.done(0)


			button_save = QPushButton("Save Changes")
			button_save.clicked.connect(writeStats)
			button_cancel = QPushButton("Cancel")
			button_cancel.clicked.connect(statwindow.done)
			hbox = QHBoxLayout()
			hbox.addWidget(button_save)
			hbox.addWidget(button_cancel)
			self.layout.addLayout(hbox)


			self.tableWidget.setHorizontalHeaderLabels(['Name', 'Value'])
			self.tableWidget.verticalHeader().hide()
			self.tableWidget.setColumnWidth(0,350)
			self.tableWidget.setColumnWidth(1,150)
			self.layout.addWidget(self.tableWidget)
			statwindow.setLayout(self.layout)
			statwindow.setWindowModality(Qt.ApplicationModal)
			statwindow.exec_()


	def show_charmenu(self):
		global dir
		charmenu = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
		charmenu.setWindowTitle("Character Menu")
		charmenu.setWindowIcon(QIcon(dir+'icon.ico'))
		width=958
		height=510
		charmenu.resize(width,height)
		charmenu.setFixedSize(width,height)
		charmenu.setStyleSheet("background-color: black;")



		##CHARMENU BUTTONS##

		def char_button(charactername, image, offset, x, y):
			btn_char = QPushButton('', charmenu)
			btn_char.setIcon(QIcon(dir+image))
			btn_char.setIconSize(QSize(94,62))
			btn_char.resize(QSize(94,62))
			btn_char.move(x,y)
			btn_char.clicked.connect(lambda: self.characterwrite(offset,charactername))


		#char_button(Character Name, Image, Offset, x, y)
		char_button("Mario","mario.png",0x53FF40,0,0)
		char_button("Donkey Kong","dk.png",0x53FF48,96,0)
		char_button("Link","link.png",0x53FF50,192,0)
		char_button("Samus","samus.png",0x53FF58,288,0)
		char_button("Dark Samus","darksamus.png",0x53FF60,384,0)
		char_button("Yoshi","yoshi.png",0x53FF68,480,0)
		char_button("Kirby","kirby.png",0x53FF70,576,0)
		char_button("Fox","fox.png",0x53FF78,672,0)
		char_button("Pikachu","pikachu.png",0x53FF80,768,0)
		char_button("Luigi","luigi.png",0x53FF88,864,0)
		char_button("Ness","ness.png",0x53FF90,0,64)
		char_button("Captain Falcon","captainfalcon.png",0x53FF98,96,64)
		char_button("Jigglypuff","jigglypuff.png",0x53FFA0,192,64)
		char_button("Peach","peach.png",0x53FFA8,288,64)
		char_button("Daisy","daisy.png",0x53FFB0,384,64)
		char_button("Bowser","bowser.png",0x53FFB8,480,64)
		char_button("Ice Climbers","iceclimbers.png",0x53FFC0,576,64)
		char_button("Sheik","sheik.png",0x53FFC8,672,64)
		char_button("Zelda","zelda.png",0x53FFD0,768,64)
		char_button("Dr. Mario","drmario.png",0x53FFD8,864,64)
		char_button("Pichu","pichu.png",0x53FFE0,0,128)
		char_button("Falco","falco.png",0x53FFE8,96,128)
		char_button("Marth","marth.png",0x53FFF0,192,128)
		char_button("Lucina","lucina.png",0x53FFF8,288,128)
		char_button("Young Link","younglink.png",0x540000,384,128)
		char_button("Ganondorf","ganondorf.png",0x540008,480,128)
		char_button("Mewtwo","mewtwo.png",0x540010,576,128)
		char_button("Roy","Roy.png",0x540018,672,128)
		char_button("Chrom","Chrom.png",0x540020,768,128)
		char_button("Mr. Game & Watch","mrgameandwatch.png",0x540028,864,128)
		char_button("Meta Knight","metaknight.png",0x540030,0,192)
		char_button("Pit","pit.png",0x540038,96,192)
		char_button("Dark Pit","darkpit.png",0x540040,192,192)
		char_button("Zero Suit Samus","zerosuitsamus.png",0x540048,288,192)
		char_button("Wario","wario.png",0x540050,384,192)
		char_button("Snake","snake.png",0x540058,480,192)
		char_button("Ike","ike.png",0x540060,576,192)
		char_button("Pokémon Trainer","pokemontrainer.png",0x540068,672,192)
		char_button("Diddy Kong","diddykong.png",0x540070,768,192)
		char_button("Lucas","lucas.png",0x540078,864,192)
		char_button("Sonic","sonic.png",0x540080,0,256)
		char_button("King Dedede","kingdedede.png",0x540088,96,256)
		char_button("Olimar","olimar.png",0x540090,192,256)
		char_button("Lucario","lucario.png",0x540098,288,256)
		char_button("R.O.B.","rob.png",0x5400A0,384,256)
		char_button("Toon Link","toonlink.png",0x5400A8,480,256)
		char_button("Wolf","wolf.png",0x5400B0,576,256)
		char_button("Villager","villager.png",0x5400B8,672,256)
		char_button("Mega Man","megaman.png",0x5400C0,768,256)
		char_button("Wii Fit Trainer","wiifittrainer.png",0x5400C8,864,256)
		char_button("Rosalina & Luma","rosalinaandluma.png",0x5400D0,0,320)
		char_button("Little Mac","littlemac.png",0x5400D8,96,320)
		char_button("Greninja","greninja.png",0x5400E0,192,320)
		char_button("Palutena","palutena.png",0x5400E8,288,320)
		char_button("PAC-MAN","pacman.png",0x5400F0,384,320)
		char_button("Robin","robin.png",0x5400F8,480,320)
		char_button("Shulk","shulk.png",0x540100,576,320)
		char_button("Bowser Jr.","bowserjr.png",0x540108,672,320)
		char_button("Duck Hunt Duo","duckhuntduo.png",0x540110,768,320)
		char_button("Ryu","ryu.png",0x540118,864,320)
		char_button("Ken","ken.png",0x540120,0,384)
		char_button("Cloud","cloud.png",0x540128,96,384)
		char_button("Corrin","corrin.png",0x540130,192,384)
		char_button("Bayonetta","bayonetta.png",0x540138,288,384)
		char_button("Inkling","inkling.png",0x540138,384,384)
		char_button("Ridley","ridley.png",0x540140,480,384)
		char_button("Simon","simon.png",0x540148,576,384)
		char_button("Richter","richter.png",0x540150,672,384)
		char_button("King K. Rool","kingkrool.png",0x540158,768,384)
		char_button("Isabelle","isabelle.png",0x540160,864,384)
		char_button("Incineroar","incineroar.png",0x540168,336,448)

		btn_unlockall = QPushButton('', charmenu)
		btn_unlockall.setIcon(QIcon(dir+"unlockall.png"))
		btn_unlockall.setIconSize(QSize(94,62))
		btn_unlockall.resize(QSize(94,62))
		btn_unlockall.move(432,448)
		btn_unlockall.clicked.connect(lambda: self.characterlockunlockall("unlock"))

		btn_lockall = QPushButton('', charmenu)
		btn_lockall.setIcon(QIcon(dir+"lockall.png"))
		btn_lockall.setIconSize(QSize(94,62))
		btn_lockall.resize(QSize(94,62))
		btn_lockall.move(528,448)
		btn_lockall.clicked.connect(lambda: self.characterlockunlockall("lock"))

		charmenu.setWindowModality(Qt.ApplicationModal)
		charmenu.exec_()


	def readFromPosition (self, startOffset, endOffset, type):
		valueToRead=(binascii.unhexlify(h[startOffset*2:endOffset*2]))
		valueToRead1=struct.unpack(type,valueToRead)
		valueToRead2=functools.reduce(lambda rst, d: rst * 10 + d, (valueToRead1))
		return valueToRead2


	def writeToPosition (self, value, startOffset, endOffset, type):
		global h
		valueToWrite = binascii.hexlify(struct.pack(type, value))
		h=h[:startOffset*2]+valueToWrite+h[endOffset*2:]


	def writeToPositionStr (self, hexstring, startOffset, endOffset):
		global h
		h=h[:startOffset*2]+hexstring+h[endOffset*2:]


	def characterwrite(self, charoffset,charactername):
		if self.checkforsave():
			global h
			position=self.readFromPosition(charoffset,charoffset+1,"<B")

			if position==1:
				self.writeToPosition(0,charoffset,(charoffset+1),"<B")

				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("<b>"+charactername+"</b>"+" locked!")
				msg.setWindowTitle("Character Menu")
				msg.setWindowIcon(QIcon(dir+'icon.ico'))
				msg.exec_()

			elif position==0:
				self.writeToPosition(1,charoffset,charoffset+1,"<B")

				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("<b>"+charactername+"</b>"+" unlocked!")
				msg.setWindowTitle("Character Menu")
				msg.setWindowIcon(QIcon(dir+'icon.ico'))
				msg.exec_()


	def characterlockunlockall(self,mode): #Modes are "lock" and "unlock"
		if self.checkforsave():
			global h
			startoffset=0x53FF40	#First character offset (Mario)
			numberofcharacters=70	#Number of characters (until Incineroar)

			for x in range(0,numberofcharacters+1):
				position=self.readFromPosition(startoffset,startoffset+1,"<B")
				if (mode=="lock"):
					self.writeToPosition(0,startoffset,(startoffset+1),"<B")
					startoffset+=(8)

				if (mode=="unlock"):
					self.writeToPosition(1,startoffset,(startoffset+1),"<B")
					startoffset+=(8)

			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			if (mode=="lock"):
				msg.setText("<b>Locked</b> all characters!")
			if (mode=="unlock"):
				msg.setText("<b>Unlocked</b> all characters!")
			msg.setWindowTitle("Character Menu")
			msg.setWindowIcon(QIcon(dir+'icon.ico'))
			msg.exec_()


	def unlockmiiclothes(self):
		if self.checkforsave():
			hexstr1="FFFFFFFFFFFFFFFFFFFF".encode()
			hexstr2="FFFFFFFFFFFFFFFFFFFFFFFF".encode()
			self.writeToPositionStr(hexstr1,0x20,0x2A)
			self.writeToPositionStr(hexstr2,0x54,0x60)

			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setText("<b>Unlocked</b> all Mii Clothes!")
			msg.setWindowTitle("Mii Clothes")
			msg.setWindowIcon(QIcon(dir+'icon.ico'))
			msg.exec_()


	def unlockmilestones(self):
		if self.checkforsave():
			hexstr="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF".encode()
			self.writeToPositionStr(hexstr,0x555BB8,0x555BE8)

			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setText("<b>Unlocked</b> all Milestones!")
			msg.setWindowTitle("Milestones")
			msg.setWindowIcon(QIcon(dir+'icon.ico'))
			msg.exec_()

		#########################################
		#			  BUTTON DIALOGS			#
		#########################################

	def inputLanguage(self):
		if self.checkforsave():
			languages=("日本語","English","Français","Español","Deutsch","Italiano","Nederlands","Pусский","简体中文","繁體中文","한국어")
			language=self.readFromPosition(0x3C6098,0x3C6099,"<B")
			item, okPressed = QInputDialog.getItem(self, "Language","Language:", languages, language, False)
			if okPressed and item:
				self.writeToPosition(languages.index(item),0x3C6098,0x3C6099,"<B")

	def inputGold(self):
		if self.checkforsave():
			gold=self.readFromPosition(0x5506DC,0x5506E0,"<L")
			amount, okPressed = QInputDialog.getInt(self, "Gold","Amount:", gold, 0, 0x98967F, 10000)
			if okPressed:
				self.writeToPosition(amount,0x5506DC,0x5506E0,"<I") #Gold
				self.writeToPosition(amount,0x540290,0x540294,"<I") #Obtained Gold record data
				self.writeToPosition(0,0x540294,0x540298,"<I") #Gold Spent record data (set to 0)

	def inputSP(self):
		if self.checkforsave():
			SP=self.readFromPosition(0x4831E4,0x4831E8,"<L")
			amount, okPressed = QInputDialog.getInt(self, "SP","Amount:", SP, 0, 0x98967F, 10000)
			if okPressed:
				self.writeToPosition(amount,0x4831E4,0x4831E8,"<I") #SP
				self.writeToPosition(amount,0x540298,0x54029C,"<I") #Obtained SP record data

	def inputSnackS(self):
		if self.checkforsave():
			snackS=self.readFromPosition(0x4831CE,0x4831D0,"<H")
			amount, okPressed = QInputDialog.getInt(self, "Snack (S)","Amount:", snackS, 0, 0x03E7, 50)
			if okPressed:
				self.writeToPosition(amount,0x4831CE,0x4831D0,"<H") #Snack(S)

	def inputSnackM(self):
		if self.checkforsave():
			snackM=self.readFromPosition(0x4831D0,0x4831D2,"<H")
			amount, okPressed = QInputDialog.getInt(self, "Snack (M)","Amount:", snackM, 0, 0x03E7, 50)
			if okPressed:
				self.writeToPosition(amount,0x4831D0,0x4831D2,"<H") #Snack(M)

	def inputSnackL(self):
		if self.checkforsave():
			snackL=self.readFromPosition(0x4831D2,0x4831D4,"<H")
			amount, okPressed = QInputDialog.getInt(self, "Snack (L)","Amount:", snackL, 0, 0x03E7, 50)
			if okPressed:
				self.writeToPosition(amount,0x4831D2,0x4831D4,"<H") #Snack(L)

	def inputHammers(self):
		if self.checkforsave():
			hammers=self.readFromPosition(0x555E5C,0x555E5D,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Hammers","Amount:", hammers, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x555E5C,0x555E5D,"<B") #Hammers

	def inputTickets(self):
		if self.checkforsave():
			tickets=self.readFromPosition(0x5506CC,0x5506CD,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Tickets","Amount:", tickets, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x5506CC,0x5506CD,"<B") #Tickets

	def inputShuffleAll(self):
		if self.checkforsave():
			shuffleAll=self.readFromPosition(0x4831C0,0x4831C1,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Shuffle All","Amount:", shuffleAll, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C0,0x4831C1,"<B") #Shuffle All

	def inputAllPrimaries(self):
		if self.checkforsave():
			allPrimaries=self.readFromPosition(0x4831C1,0x4831C2,"<B")
			amount, okPressed = QInputDialog.getInt(self, "All Primaries","Amount:", allPrimaries, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C1,0x4831C2,"<B") #All Primaries

	def inputAllSupports(self):
		if self.checkforsave():
			allSupports=self.readFromPosition(0x4831C2,0x4831C3,"<B")
			amount, okPressed = QInputDialog.getInt(self, "All Supports","Amount:", allSupports, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C2,0x4831C3,"<B") #All Supports

	def inputRematch(self):
		if self.checkforsave():
			rematch=self.readFromPosition(0x4831C4,0x4831C5,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Rematch","Amount:", rematch, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C4,0x4831C5,"<B") #Rematch

	def inputFiller(self):
		if self.checkforsave():
			filler=self.readFromPosition(0x4831C3,0x4831C4,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Filler","Amount:", filler, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C3,0x4831C4,"<B") #Filler

	def inputDamage50(self):
		if self.checkforsave():
			damage50=self.readFromPosition(0x4831C6,0x4831C7,"<B")
			amount, okPressed = QInputDialog.getInt(self, "50% Damage","Amount:", damage50, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C6,0x4831C7,"<B") #50% Damage

	def inputSlowFSCharging(self):
		if self.checkforsave():
			slowFSCharging=self.readFromPosition(0x4831C7,0x4831C8,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Slow FS Charging","Amount:", slowFSCharging, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C7,0x4831C8,"<B") #Slow FS Charging

	def inputWeakenMinions(self):
		if self.checkforsave():
			weakenMinions=self.readFromPosition(0x4831C8,0x4831C9,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Weaken Minions","Amount:", weakenMinions, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C8,0x4831C9,"<B") #Weaken Minions

	def inputHealthDrain(self):
		if self.checkforsave():
			healthDrain=self.readFromPosition(0x4831C9,0x4831CA,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Health Drain","Amount:", healthDrain, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831C9,0x4831CA,"<B") #Health Drain

	def inputDisableItems(self):
		if self.checkforsave():
			disableItems=self.readFromPosition(0x4831CA,0x4831CB,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Disable Items","Amount:", disableItems, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831CA,0x4831CB,"<B") #Disable Items

	def inputShieldSpacer(self):
		if self.checkforsave():
			shieldSpacer=self.readFromPosition(0x4831CB,0x4831CC,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Shield Spacer","Amount:", shieldSpacer, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831CB,0x4831CC,"<B") #Shield Spacer

	def inputSluggishShield(self):
		if self.checkforsave():
			sluggishShield=self.readFromPosition(0x4831CC,0x4831CD,"<B")
			amount, okPressed = QInputDialog.getInt(self, "Sluggish Shield","Amount:", sluggishShield, 0, 0x63, 10)
			if okPressed:
				self.writeToPosition(amount,0x4831CC,0x4831CD,"<B") #Sluggish Shield


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle("fusion")
	if (sys.platform.startswith('linux')):
		font=app.font()
		font.setPointSize(9)
		app.setFont(font)
	ex = App()
	sys.exit(app.exec_())
