import os
import subprocess
import platform

class SystemEngineer:
    def check_folder_contents(self):
        print("Checking directory contents...")
        if platform.system() == "Windows":
            result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
        else:
            result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
        return result.stdout

    def create_log_dir(self, folder_name: str = "logs"):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Directory '{folder_name}' created successfully.")
        else:
            print("Directory already exists.")

engineer = SystemEngineer()
print(engineer.check_folder_contents())
engineer.create_log_dir()
