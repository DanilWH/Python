import os

fileslist = os.walk('filesort')
for i in fileslist:
    fileslist = i[-1]
    break
print(fileslist)

def num_write(file, old_file):
    with open(old_file) as f:
        obj = f.read()

    with open('filesort/nums/' + file, 'w') as f:
        f.write(obj)

    os.remove(old_file)

for file in fileslist:
    old_file = 'filesort/' + file
    try:
        int(file[:2])
    except ValueError:
        try:
            int(file[:1])
        except ValueError:
            with open(old_file) as f:
                obj = f.read()

            with open('filesort/chars/' + file, 'w') as f:
                f.write(obj)

            os.remove(old_file)
        else:
            num_write(file, old_file)
    else:
        num_write(file, old_file)