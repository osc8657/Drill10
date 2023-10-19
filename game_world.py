

objects = [[],[]]

def add(o, depth):
    objects[depth].append(o)

def update():
    for layer in objects:
        for o in layer:
            o.update()



def render():
    for layer in objects:
        for o in layer:
            o.draw()
