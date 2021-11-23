import time 
from colorama import Fore, Back, Style, init
import art 
import sys

def redprint(s):
    print(Fore.RED + s)
    
def write(string, style=None):
    for i in range(len(string)):  
        sys.stdout.write(string[i])
        time.sleep(.02)
    print('\n')
    time.sleep(.1)
    
def ask(string, style=None):
    return(input(string + " >>> \n"))

 
def make_choice(options):
    print('\n')
    for i in range(len(options)):
        print("[{}] ".format(i+1) + options[i] + '\n')
    choice = ""
    while True:
        choice = input("Cosa fai adesso? >>> ")
        if choice in ['{}'.format(i) for i in range(1, len(options)+1)]:
            print('>>>' + options[int(choice)-1] + '\n')
            print("\n")
            return(int(choice))
        else:
            print("Inserisci un numero. \n")

def print_abandon():
     phrase = ["lasciate", "ogne", "speranza,", "voi", "ch 'intrate"]
     time.sleep(1)
     print('\n')
     for i in phrase:
         print(art.text2art(i, font='ghoulish',chr_ignore=True) + '\n')
         time.sleep(1)
#def get_next(i):
    # info = read line i of script
    # action_type = info[0]
    # text = info[1]
    # send text to correct function
    # return new_i : this is where to advance next.