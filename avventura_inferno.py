from fns import write, ask, make_choice, print_abandon
import time 
from stages import *
from colorama import Fore, Back, Style, init
import art as a
import pandas as pd

version = 1.0 

url_data = (r'https://raw.githubusercontent.com/oderofrancis/rona/main/Countries-Continents.csv')

df = pd.read_csv(url_data)

newest_version = df.iloc[0]

if (version < newest_version):
    print("Una nuova versione è disponibile qui: https://github.com/tea-tm/avventura_inferno/blob/main/avventura_inferno.exe")

info = {'mtn': False, 'ciacco': False}
 
write('Instruzioni: \n Per fare una scelta, inserire il numero che corrisponde a quello che vuoi fare. \n Per continuare, premere \'Enter\' \n')

next_step, info = start_game(info)

while True:
    next_step, info = next_step(info)
