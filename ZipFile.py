from zipfile import ZipFile

file_path = "Desktop:\\Classification and its issues"

with ZipFile(file_path,"r") as zip:
	zip.printdir()