import os 

country_folder_path = os.getcwd()+'/country'
print(os.listdir(country_folder_path))

country_folder_name_list = []
for var in os.listdir(country_folder_path):
    Path = country_folder_path+'/'+var
    if os.path.isdir(Path):  
        country_folder_name_list.append(var)  
    else:  
        continue
result_list = []
for var in country_folder_name_list:
    country_temp_path = country_folder_path+'/'+var
    file_folder_path = country_temp_path+'/files'
    if os.path.isdir(file_folder_path):
        for file_var in os.listdir(file_folder_path):
            csv_file_path = file_folder_path+'/'+file_var
            if os.path.isfile(csv_file_path) and file_var[-4:] == '.csv':
                result_list.append(var)
            else:
                continue
    else:
        continue
result_list =  list(set(result_list))
print(result_list)