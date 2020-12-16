import glob

path = '.\\Directory'
for file in glob.iglob(path + "**/**", recursive=True):
    print(file)
