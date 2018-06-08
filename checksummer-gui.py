#!/usr/bin/python

# Author: graycatwhiz
# Description: stupid-simple tool for checksum gui
# Date Created: June 7, 2018
# Last Updated: June 8, 2018
# Script Name: checksummer.py

from Tkinter import *
from string import Template
import ttk
import tkFileDialog
import os
from checksummer import CheckSummer
import tkMessageBox


window = Tk()
window.resizable(False,False)
window.geometry('300x350')
window.title('Checksummer')

styledttk= ttk.Style()
styledttk.theme_use('clam')

browsePath = StringVar()
md5hash = StringVar()
sha1hash = StringVar()
sha256hash = StringVar()
sha512hash = StringVar()
genfile = ''

def showAbout():
	tkMessageBox('About','Coded by GrayCatWhiz')

menuBar = Menu(window)
menuBar.add_command(label='About',command=showAbout)

notice = Label(window,text='Please Browse for a file: ')
notice.place(x=15,y=30)

path1 = ttk.Entry(window,textvariable=browsePath,state=DISABLED)
path1.place(x = 15,y = 60)

def getFile():
	nativePath = ''
	uname = os.getlogin()
	if(os.name == 'nt'):
		nativePath = 'C:/Users/' + uname + '/Documents'
	else:
		nativePath = '/home/' + uname + '/Documents'
	window.filename = tkFileDialog.askopenfilename(initialdir=nativePath)
	browsePath.set(window.filename)
	genfile = window.filename

browseBtn = ttk.Button(window,text='Browse',command=getFile)
browseBtn.place(x = 185,y = 55)

md5Lbl = Label(text='MD5: ')
md5Lbl.place(x = 15,y = 100)
sha1Lbl = Label(text='SHA1: ')
sha1Lbl.place(x = 15,y = 130)
sha256Lbl = Label(text='SHA256: ')
sha256Lbl.place(x = 15,y = 160)
sha512Lbl = Label(text='SHA512: ')
sha512Lbl.place(x = 15,y = 190)

md5En = Entry(window,textvariable=md5hash)
md5En.place(x = 90,y = 100)
sha1En = Entry(window,textvariable=sha1hash)
sha1En.place(x = 90,y = 130)
sha256En = Entry(window,textvariable=sha256hash)
sha256En.place(x = 90,y = 160)
sha512En = Entry(window,textvariable=sha512hash)
sha512En.place(x = 90,y = 190)

def getHashed():
	checksummer= CheckSummer()
	md5hash.set(checksummer.getMD5(md5hash.get()))
	sha1hash.set(checksummer.getSHA1(sha1hash.get()))
	sha256hash.set(checksummer.getSHA256(sha256hash.get()))
	sha512hash.set(checksummer.getSHA512(sha512hash.get()))

getHash = ttk.Button(window,text='Generate Checksum',width=30,command=getHashed)
getHash.place(x = 25,y = 300)

def getSaved():
	if(md5hash.get() != ''):
		localfile = window.filename + '.txt'
		ofile = open(localfile,'w')
		data = Template('Filename: $filename \nMD5: $md5\nSHA1: $sha1\nSHA256: $sha256\nSHA512: $sha512')
		data = str(data.substitute(filename=window.filename,md5=md5hash.get(),sha1=sha1hash.get(),sha256=sha256hash.get(),sha512=sha512hash.get()))
		ofile.write(data)
		ofile.close()
		tkMessageBox.showinfo('Attention','File "' + window.filename +'" has been write successfully!' )
	else:
		tkMessageBox.showinfo('Error','No information to be saved!' )

saveHash = ttk.Button(window,text='Save Checksum',width=30,command=getSaved)
saveHash.place(x = 25,y = 240)


window.config(menu=menuBar)
window.mainloop()