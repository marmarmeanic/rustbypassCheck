import sys, getpass, glob, ctypes, os, datetime, random, time, psutil, pyperclip, shutil
from colorama import Fore, init
import time

userprofile = os.getenv('USERPROFILE')
date_old = 'date ' + time.strftime('%d.%m.%Y')
time_old = 'time ' + time.strftime('%H.%M')
directory_list = list()

for root, dirs, files in os.walk(userprofile + r'\AppData\Local\LGHUB\scripts', topdown=False):
	for name in dirs:
		directory_list.append(os.path.join(root, name))
		str_directory_list = ''.join(directory_list)

def paste():
	for i in directory_list:
		my_file = open(i + '\script.lua', "w")
		my_file.write('function OnEvent(event, arg)\n     --OutputLogMessage("Event: "..event.." Arg: "..arg.."\\n");\nend')
		my_file.close()

def input_time():
	try:
		os.system('cls||clear')
		install_date = os.popen('systeminfo | find "Дата установки"').read()
		install_date = install_date[34:54]
		print (f"{Fore.MAGENTA}Дата установки системы:{Fore.MAGENTA}", install_date)
		data = input(f"{Fore.CYAN}Какую дату поставить?:{Fore.CYAN}")
		time_ = input(f"{Fore.CYAN}Какое время поставить?:{Fore.CYAN}")
		command = 'date ' + data
		command2 = 'time ' + time_
		os.system(command)
		os.system(command2)
	except:
		print("231")

def old_time():
	try:
		os.system(date_old)
		os.system(time_old)
	except:
		ctypes.windll.user32.MessageBoxW("Произошла системная ошибка.", "Error")

def kill_hub():
	for process in psutil.process_iter():
		if process.name() == 'lghub.exe':
			process.kill()
	for process in psutil.process_iter():
		if process.name() == 'lghub_agent.exe':
			process.kill()
	for process in psutil.process_iter():
		if process.name() == 'lghub_updater.exe':
			process.kill()


h = int(input("Введите кол-во ваших пицц:"))
if h == 32151:
	ctypes.windll.kernel32.SetConsoleTitleW("BypassRustCheck")
	start_time = time.monotonic()
	input_time()
	kill_hub()
	paste()
	os.system('cls||clear')
	with open("D:\HomeworkEnglish.txt", "r") as file:
		line = file.readline()
	pyperclip.copy(line)
	old_time()
	os.system('cls||clear')
	print(f"{Fore.GREEN}Ваш дискорд скопирован!\nУдачного Времяпрепровождения!\nЧистка была выполнена за: {time.monotonic() - start_time}c")
	time.sleep(5)
	sys.exit()
else:
	print("Ваш заказ принят, ожидайте...")
	print("Вы заказали", h, "пиццу.")
	print("Нажмите Enter")
	input()
