
from pathlib import Path

# Current working directory

current_path = Path.cwd()

print("Current Directory:")
print(current_path)

# Create a new folder

data_folder = current_path / "datasets"

data_folder.mkdir(exist_ok=True)

print("\nFolder Created:")
print(data_folder)


# Create a file path safely


file_path = data_folder / "training_data.csv"

print("\nFile Path:")
print(file_path)


# Write data into file


file_path.write_text("id,name\n1,Aryan\n2,John")

print("\nData written successfully!")


# Read file content


content = file_path.read_text()

print("\nFile Content:")
print(content)

# Check if file exists
print("\nDoes file exist?")
print(file_path.exists())