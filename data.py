import json
from pathlib import Path

# path of the file 
file_path = Path(__file__)

# root directory path
root_path = file_path.parent

# function to create the json file
def create_file():
    json_file = root_path / 'users.json'
    with open(json_file,'w') as f:
        json.dump({},f)
        
       

if __name__ == "__main__":
    create_file()