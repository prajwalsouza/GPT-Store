
import os

def read_readme(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
        
        return markdown_content
        
folder_path = 'gpts/'

# Use os.listdir to get a list of all items in the folder
all_items = os.listdir(folder_path)

# Filter the list to include only files (not directories)
file_list = [item for item in all_items if os.path.isfile(os.path.join(folder_path, item))]

gpts_content = ""
for file_name in file_list:
    file_content = read_readme(folder_path + "/" + file_name)
    gpts_content = gpts_content + "\n" + file_content
    

print(gpts_content)

    