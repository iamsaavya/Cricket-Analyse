import team as t
import player as p
import hand_cricket as h

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[97m'
RESET = '\033[0m'

print(MAGENTA + """
          
          CRICKET ANALYSE : PROJECT BY""" + RED +" SAAVYA AWASTHI , " + GREEN + "SAIRADITYA DESHMUKH, " + RESET + "AND " + YELLOW + """BALRAJ SINGH
          
          """)

def menu():

    print(RESET + 
          
          """ Enter the integer corresponding to your preferred Analysis :

          1. Team-List
          2. Player Profile
          3. Hand Cricket! (SPECIAL!)

          Press Any Other Key To Exit
            \n          
           """)
    rohtak = int(input())

    if rohtak==1:
            t.main()
    if rohtak==2:
            p.player()
    if rohtak==3:
           h.main()

menu()

    