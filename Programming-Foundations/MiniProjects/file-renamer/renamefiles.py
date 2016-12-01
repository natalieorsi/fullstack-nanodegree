import os
def rename_files():
	#get file names from a folder
	file_list = os.listdir(r"C:\OOP\prank")
	saved = os.getcwd()
	os.chdir(r"C:\OOP\prank")
	print(file_list)
	#for each file, rename filename
	for filename in file_list:
		os.rename(file,file.translate(None,range(9)))
	os.chdir(saved)
rename_files()