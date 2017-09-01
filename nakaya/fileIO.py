
def read(path):
    dst = []
    filename = path
    fin = open(filename, "r")
    dst = [ item.strip() for item in fin.readlines()]
    fin.close()
    return dst