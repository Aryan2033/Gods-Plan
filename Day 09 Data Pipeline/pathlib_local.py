from pathlib import Path
 

#current working directory

currnet_path= Path.cwd()

print("current path")
print(current_path)

#create new folder

data_folder=current_path/"dataset"

data_folder.mkdir(exist_ok=True)

print("\n folder created")
print(data_folder)


#create file path safely

file_path=data_folder/"training.csv"
print("\n file path")
print(file_path)


#write into file

file_path.write_text("id,name\n1,Aryan\n2,omkar")
print("data written successfully")


#read file content

content=file_path.read_text()

print("file content")
print(content)

#check if file exist

print("does file exist")
print(file_path.exist())


