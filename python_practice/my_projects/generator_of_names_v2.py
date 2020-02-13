import random

glasl=['а','е','и','о','у','э','ю','я']
sogll=['б','в','г','д','з','к','л','м','н','п','р','с','т','ф','х','ц']

names = []
letters = []
answer = int(input("How many names do you want to see? "))

for time in range(answer):
    for name in range(3):
        random_g = random.randint(0, len(glasl) - 1)
        gl = glasl[random_g]
        letters.append(gl)

        random_s = random.randint(0, len(sogll) - 1)
        sog = sogll[random_s]
        letters.append(sog)

    name = ''.join(letters).title()
    names.append(name)
    letters = []
print(names)
