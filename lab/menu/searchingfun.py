def search_string_in_file(): 
    file_path = 'newproject.txt'
    search_string=input("enter date want to search about \n")
    with open(file_path, 'r') as file: 
        for line_number, line in enumerate(file, start=1): 
            if search_string in line: 
                print(f'Found "{search_string}" in line {line_number}: {line.strip()}') 
 
""""date=input("enter date want to search about \n")
file_path = 'project.txt'
search_string_in_file(file_path,date)"""""

search_string_in_file()