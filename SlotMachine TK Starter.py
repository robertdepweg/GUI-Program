# PROGRAM: Slot Machine
# AUTHOR: C Claussen
# MODIFICATION:
# DESCRIPTION:  
#               
# INPUT:  
# OUTPUT: 
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Canvas or panels not needed

import tkinter
import tkinter.messagebox
import random

# Only Global Variables Needed
total_bet = 0
total_wins = 0



def main():

    total_bet = 0
    total_wins = 0

    # List to hold fruit file names


    # Create the main window.
    

    # Display a title in the window
    

    # Center the window on the screen
    
    # Allow the window to be resized
    

    # We need a StringVar object to associate with
    # each output label. Use the object's set method
    # to store a string of blank characters.
    prize = tkinter.StringVar()
    win = tkinter.StringVar()
    prize.set('')
    win.set('')
    
    # Create five frames.
 

    #####################
    # image frame widgets #
    #####################         
    # Create and pack the widgets for image frame.
    # self.root = tkinter.Tk()  
        #self.canvas = tkinter.Canvas(self.root, width = 300, height = 300)  
    
    # https://www.pythontutorial.net/tkinter/tkinter-label/

    # create a PhotoImage widget by passing the path to the photo to 
    # the PhotoImage constructor:
    image1 = tkinter.PhotoImage(file = 'dollarsign.png')
    # assign the PhotoImage object to the image option of the Label widget:
    img1_label = tkinter.Label(image_frame,
                                    image = image1)
    image2 = tkinter.PhotoImage(file = 'dollarsign.png')
    img2_label = tkinter.Label(image_frame,
                                    image = image1)
    image3 = tkinter.PhotoImage(file = 'dollarsign.png')
    img3_label = tkinter.Label(image_frame,
                                    image = image1)
    # List to hold images
    image_list = [image1, image2, image3]

    # List to hold image labels
    image_label_list = [img1_label, img2_label, img3_label]

    # Pack the image frame widgets.                                 
    img1_label.pack(side='left', padx = 5, pady = 5)
    img2_label.pack(side='left', padx = 5, pady = 5)
    img3_label.pack(side='left', padx = 5, pady = 5) 

    #######################
    # entry frame widgets #
    #######################
    # Create the widgets for entry_frame.
    # Create the 'Amount Inserted: $'  entry label
    
    # Create the bet entry text box                                    
    

    # Pack the entry frame widgets.                                 
    

    #######################
    # prize frame widgets #
    #######################
    # Create the widgets for prize_frame.
    # Create the 'Prize: $' prize label
    
    # Create the output label for the prize value
    

    # Pack the entry frame widgets.
    

    #####################
    # win frame widgets #
    #####################
    # Create and pack the widgets for win_frame.
    # Create the 'Total win: $' win label
    
    # Create the output label for the total win value
    

    # Pack the entry frame widgets.
    

    ########################
    # button frame widgets #
    ########################
    # Create the button widgets.

    # Hint: You will need to create the button objects using the 
    # command = lambda event_loop(arg1, arg2, arg3, ....)
    # command = lambda end_game(arg1)

    # Create spin button
 
    # Create quit button

    # Pack the button frame widgets


    # Pack the frames.
 

    # Start the main loop.
 

def event_loop(bet_entry, fruit, image_list, image_label_list, prize, win):
    ''' 
    callback function for spin button 
    Retrieve the bet value
    Run the Event Loop until we break out
    '''
    global total_bet
    global total_wins
    
    
    # Get the bet value
    
    
    

    # Run the Event Loop forever (until we break out) 
    # if there is a bet ( money entered into slots)
    if (bet) != '':

        # spin for three new fruit
       

        # Add bet to this games total bets
        

        # Calculate prize amount based on number of matches


        # Update prize amount
 

        # Calculate total wins
 

    # Display message asking user to insert money before playing
    # if bet is empty (No coins entered into slot)
    
        message_string = f"Insert Money into Slot \n" + \
                f"Money must be inserted into machine before play will start."
 

    # Update win value for current slot
    
    

def spin(fruit, image_list, image_label_list):
    '''
    Generate random numbers to simulate spin.
    Display fruit image corresponding to random numbers.
    update images
    return random integers
    '''
 
    # Update image of Tkinter label widget
    # Once the PhotoImage has gone out of scope 
    # it is no longer active and NOT shown on the display
    # https://stackoverflow.com/questions/3482081/how-to-update-the-image-of-a-tkinter-label-widget
    # image1 = tkinter.PhotoImage(file = fruit[n1])
    # image2 = tkinter.PhotoImage(file = fruit[n2])
    # image3 = tkinter.PhotoImage(file = fruit[n3])


    # .config is used to change the text on a label
    # https://coderslegacy.com/python/tkinter-config/

    pass

def end_game(main_window):
    '''
    Display total money entered into slots and total winnings
    in a message box.
    Stop the game.
    '''
    # pythonguides.com
    pass

# Create an instance of the TestAvg class.
if __name__ == '__main__':
    main()
    

