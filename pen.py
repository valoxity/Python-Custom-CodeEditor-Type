from pynput.keyboard import Key, Controller
import time 
keyboard = Controller()
 
def init():
    FilePath = input("File Path (index.html):  ")  
    # FilePath = 'code.html'
    sleep = input("Typeing sleep (3 , 2 , 1, 0)X:  ")
    if sleep=='3':
        sleep = .1
    elif sleep=="2":
        sleep = .01
    elif sleep=="1":
        sleep = .001
    elif sleep=="0":
        sleep = 0
    def split(words):
        return [char for char in words]
    print("Typing will start within 4 seconds.")
    print("Please click on the paper")
    time.sleep(4)
    print("Typing start ...")
    with open(FilePath, 'r')as f:
        for line in f:
            for i in split(line):
                keyboard.type(i)
                time.sleep(sleep) 
        init()        

if __name__ == '__main__': 
    init() 