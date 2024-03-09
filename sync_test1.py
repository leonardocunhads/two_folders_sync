import os


path_source = r"C:\\Users\\leona\\Desktop\\test\\source\\"

# print(os.listdir(path_source))
# print('\n'+'-' * 20 + '\n' )

# print(os.walk(path_source, type(os.walk(path_source))))

# print(list(os.walk(path_source)))
# print('\n'+'-' * 20 + '\n' )

for root, dirs, files in os.walk(path_source):
    print(root)
    print(dirs)
    print(files)
    print('-' * 15)