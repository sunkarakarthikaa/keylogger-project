from pynput.mouse import Listener

def writetofile(x, y): #x,y represent the current position of the mouse cursor on the screen, in pixels.
    print('position is {0}'.format((x,y)))
  

with Listener(on_move=writetofile) as l:
    l.join()