from pynput.mouse import Listener

def writetofile(x, y): #x,y are pixels
    print('position is {0}'.format((x,y)))
  

with Listener(on_move=writetofile) as l:
    l.join()