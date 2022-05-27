word = set()

def check(word):
    #TODO
    if word.lower() in word:
        return True
    else:
        return False

def load(dictionary):
    #TODO
    file = open(dictionary, 'r')
    for line in file:
        word.add(line.strip())
    file.close()
    return True

def size():
    #TODO
    return len(word)

def unload():
    #TODO
    return True