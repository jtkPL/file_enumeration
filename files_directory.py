

def file_list(files):

    file_list = []

    for single_file in files:
        file_list.append(single_file.replace('\n', ''))


    return file_list
