import os
import getpass
import shutil

def clearDirectory(path):
	directory = os.listdir(path)
	countFiles = 0
	countDirs  = 0

	print(f"ROOT DIRECTORY -> ({path})")
	for data in directory:
		try:
			if os.path.isdir(path + data):
				print(f"DELETED DIRECTORY -> ({data})")
				shtil.rmtree(path + data)
				countDirs += 1
			else:
				print(f"DELETED FILE -> ({data})")
				os.remove(path + data)
				countExcluded += 1
		except:
			print(f"COULD BE NOT DELETED -> ({data})")

	print(f"AMOUNT OF DELETED FILES -> ({countFiles})")
	print(f"AMOUNT OF DELETED DIRS  -> ({countDirs})")

clearDirectory(f"C:/Users/{getpass.getuser()}/AppData/Local/Temp/")
