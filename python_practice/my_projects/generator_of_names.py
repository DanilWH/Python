import random

glasl=['а','е','и','о','у','э','ю','я']
sogll=['б','в','г','д','з','к','л','м','н','п','р','с','т','ф','х','ц']

name = []

count = int(input("How many names do you want to see?"))
i = 0

while i < count:
    for a in range(3):
        ran_glas = random.randint(0, len(glasl) - 1)
        name.append(glasl[ran_glas])

        ran_sogl = random.randint(0, len(sogll) - 1)
        name.append(sogll[ran_sogl])

    name_foramt = ''.join(name)
    print(name_foramt.title())

    name = []
    i += 1
