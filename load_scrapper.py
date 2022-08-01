import os
dir_path = r'C:\\Users\\rtgx2\\OneDrive\\Documents\\Warcraft III\\CustomMapData\\ORD10\\'

res = []

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

path = 'C:\\Users\\rtgx2\\OneDrive\\Documents\\Warcraft III\\CustomMapData\\ORD10\\' + res[0]

with open(path, 'r') as f:
    f = f.read()
    print(f)