import json

def saveToFile(new_file: bool, filename: str, extension: str, data: any) -> None:
    
    full_file_str = filename + "." + extension
    
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
        pass


if __name__ == "__main__":
    print(f"This is a lib file, Not to be run by it's self.")