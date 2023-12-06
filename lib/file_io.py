def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as my_file:
        my_file.write(file_content)
        pass
    pass

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as my_file:
        my_file.write(append_content)
    pass

def read_file(file_name):
    # my_file = open(f"{file_name}.txt", "r", encoding="utf-8")
    # return(my_file.read())

    with open(f"{file_name}.txt", mode="rt", encoding="utf-8") as my_file:
        return(my_file.read())
    pass
