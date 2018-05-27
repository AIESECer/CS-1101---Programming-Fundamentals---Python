def new_line():
   print()

def three_lines():#This fonction draw three lines using new_line() three times
   new_line()
   new_line()
   new_line()

def nine_lines():#This fonction draw 9 lines using three_lines three times
    three_lines()
    three_lines()
    three_lines()

def clear_screen():#We will use the three past fonctions to arrive at 25 lines
   #25= 9+9+3+3+1
    nine_lines()  #We have 9
    nine_lines()  #We have 18
    three_lines() #We have 21
    three_lines() #We have 24
    new_line()    #We have 25

clear_screen() #Calling clear_screen


