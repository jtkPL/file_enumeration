import requests
import sys

from files_directory import file_list


file_resource = open(sys.argv[1], 'r')

files = file_resource.readlines()

file_list = file_list(files)

for single_file in file_list:
    
    url = f'http://businesscorp.com.br/{single_file}'
    result = requests.get(url)

    if result.status_code == 200:

        print(f"{single_file}")


        






