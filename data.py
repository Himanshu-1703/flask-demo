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
        
def save_registration_details(details:dict):
    json_file = root_path / 'users.json'
    
    # read the contents of the json file
    with open(json_file,mode='r') as f:
        json_contents = json.load(f)
    
    if details['email'] in json_contents:
        return 0
    
    else:
        # update the contents of the json file
        dict(json_contents).update(details)
    
        # write the updates back to the json file
        # * Write in this format {email:{user_name: username, password: password}
        with open(json_file,mode='w') as f:
            json.dump(json_contents,f)

        return 1
    
    
def verify_user(email,password):
    json_file = root_path / 'users.json'
    
    # read the contents of the json file
    with open(json_file,mode='r') as f:
        json_contents = json.load(f)
    
    # verify if email is matching
    if email in json_contents:
        # if passed, verify if password is same
        if password == json_contents['email']['password']:
            return 1
        else:
            return 0      
    else:
        return 0
    

        
        
                    


if __name__ == "__main__":
    create_file()