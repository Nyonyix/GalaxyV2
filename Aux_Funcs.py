import json
import os

def saveToFile(new_file: bool, filename: str, extension: str, data: any) -> None:
    
    full_file_str = filename + "." + extension
    special_file_case = False
    
    if new_file == True:
        with open(full_file_str, 'w') as f:
            if type(data) == dict:
                json.dump(data, f)

            elif type(data) == list:
                new_data = []
                for i in data:
                    new_data.append(str(i) + '\n')
                f.writelines(new_data)

            else:
                f.write(data)
    else:
        if os.path.exists(full_file_str) == True:
            with open(full_file_str, 'a') as f:
                if type(data) == list:
                    new_data = []
                    for i in data:
                        new_data.append(str(i) + '\n')
                    f.writelines(new_data)
                    special_file_case = True
                f.close()

                if type(data) == dict:
                    with open(full_file_str, 'w') as f:
                        in_dict = {}
                        with open(full_file_str, 'r') as in_f:
                            in_dict = json.load(in_f)
                        new_dict = in_dict.update(data)
                        json.dump(new_dict, f)
                        f.close()
                        special_file_case = True
                        
                if special_file_case != True:
                    with open(full_file_str, 'a') as f:
                        f.write(data)
                    
        else:
            raise FileNotFoundError()


if __name__ == "__main__":
    print(f"This is a lib file, Not to be run by it's self.")