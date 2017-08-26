
import sys

def sysPathList():
    print("[Python System Path List]")
    for item in sys.path:
        print(item)    

if __name__ == '__main__':

    sysPathList()