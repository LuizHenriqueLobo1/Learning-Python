import os
import getpass

def clearDirectory(path):
	directoryData = os.listdir(path)
	countExcluded = 0

	print("Apagando arquivos...")
	for index in range(len(directoryData)):
		try:
			os.remove(path + directoryData[index])
			print(f"{directoryData[index]} apagado com sucesso.")
			countExcluded += 1
		except:
			print(f"{directoryData[index]} não pôde ser apagado.")

	print(f"{countExcluded} arquivos apagados.")

clearDirectory(f"C:/Users/{getpass.getuser()}/AppData/Local/Temp/")
clearDirectory("C:/Windows/Prefetch/")
clearDirectory("C:/Windows/SoftwareDistribution/Download")
