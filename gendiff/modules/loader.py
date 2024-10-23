def file_load(file_path):
    with open(file_path, 'r') as file_object:
        string = file_object.read()
    return string
