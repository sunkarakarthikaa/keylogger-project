from pynput.mouse import Controller

def controlmouse():
    #call controller object and store it in a variable
    mouseobj = Controller()
    #use mouse variable to control the mouse by checking its position
    mouseobj.position = (10,20)
    # Move the mouse pointer to the position (20, 10) on the screen
    # (0, 0) is the top-left corner of the screen
    # So this moves the cursor 20 pixels right and 10 pixels down

controlmouse()