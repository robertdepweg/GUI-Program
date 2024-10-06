# PROGRAM: Slot Machine
# AUTHOR: C Claussen
# MODIFICATION: Robert Depweg
# DESCRIPTION:  Slot machine that spits out 3 images, and if the images
#               match, additional $ is added to the total $ amount.
# INPUT:  Amount of money to be bet
# OUTPUT: Chance to get more money back, total money earned and bet
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
    fruit = [ "Apple.png", "Banana.png", "Cherries.png",  
             "Grapes.png", "Lemon.png", "Lime.png", "Orange.png",
               "Pear.png", "Strawberry.png", "Watermelon.png" ]

    # Create the main window.
    main_window = tkinter.Tk()

    # Display a title in the window
    main_window.title('Slot Machine')

    # Center the window on the screen
    window_width = 450
    window_height = 250

    # obtains absolute width and height of screen
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # obtains center points of screen on x + y axis
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    # geometry string for screen dimentions
    geo_string = f'{window_width}x{window_height}+' \
                            f'{center_x}+{center_y}'
    
    # applys dimentions of geo string to root window
    main_window.geometry(geo_string)

    # Allow the window to be resized
    main_window.resizable(True,True)

    # We need a StringVar object to associate with
    # each output label. Use the object's set method
    # to store a string of blank characters.
    prize = tkinter.StringVar()
    win = tkinter.StringVar()
    prize.set('')
    win.set('')
    
    # Create five frames.
    image_frame = tkinter.Frame()
    entry_frame = tkinter.Frame() 
    prize_frame = tkinter.Frame() 
    win_frame = tkinter.Frame() 
    button_frame = tkinter.Frame() 


    #####################
    # image frame widgets #
    #####################         
    # Create and pack the widgets for image frame.
    #self.main_window = tkinter.Tk()  
    #canvas = tkinter.Canvas(main_window, width=300, height=300) 
    #canvas.pack(anchor=tkinter.CENTER) 
    
    # https://www.pythontutorial.net/tkinter/tkinter-label/

    # create a PhotoImage widget by passing the path to the photo to 
    # the PhotoImage constructor:
    image1 = tkinter.PhotoImage(file='dollarsign.png')
    # assign the PhotoImage object to the image option of the Label widget:
    img1_label = tkinter.Label(image_frame,
                                    image=image1)
    image2 = tkinter.PhotoImage(file='dollarsign.png')
    img2_label = tkinter.Label(image_frame,
                                    image=image1)
    image3 = tkinter.PhotoImage(file='dollarsign.png')
    img3_label = tkinter.Label(image_frame,
                                    image=image1)
    # List to hold images
    image_list = [image1, image2, image3]

    # List to hold image labels
    image_label_list = [img1_label, img2_label, img3_label]

    # Pack the image frame widgets.                                 
    img1_label.pack(side='left', padx=5, pady=5)
    img2_label.pack(side='left', padx=5, pady=5)
    img3_label.pack(side='left', padx=5, pady=5) 

    #######################
    # entry frame widgets #
    #######################
    # Create the widgets for entry_frame.
    # Create the 'Amount Inserted: $'  entry label
    entry_label = tkinter.Label(entry_frame, text=f'Amount Inserted: $ ')

    # Create the bet entry text box                                    
    bet_entry = tkinter.Entry(entry_frame, textvariable=entry_label)

    # Pack the entry frame widgets.                                 
    entry_label.pack(side='left')
    bet_entry.pack(side='left')

    #######################
    # prize frame widgets #
    #######################
    # Create the widgets for prize_frame.
    # Create the 'Prize: $' prize label
    prize_label = tkinter.Label(prize_frame, text=f'Prize: $')
    
    # Create the output label for the prize value
    prize_output = tkinter.Label(prize_frame, textvariable=prize)

    # Pack the entry frame widgets.
    prize_label.pack(side='left')
    prize_output.pack(side='left')
    #####################
    # win frame widgets #
    #####################
    # Create and pack the widgets for win_frame.
    # Create the 'Total win: $' win label
    win_label = tkinter.Label(win_frame, text=f'Total Win: $')
    # Create the output label for the total win value
    win_output = tkinter.Label(win_frame, textvariable=win)

    # Pack the entry frame widgets.
    win_label.pack(side='left')
    win_output.pack(side='left')
    ########################
    # button frame widgets #
    ########################
    # Create the button widgets.
    # Hint: You will need to create the button objects using the 
    # command = lambda event_loop(arg1, arg2, arg3, ....)
    # command = lambda end_game(arg1)

    # Create spin button
    spin_button = tkinter.Button(button_frame, text='Spin', 
                                command=lambda:event_loop(bet_entry, 
                                fruit, image_list, image_label_list, 
                                                        prize, win))
    # Create quit button
    quit_button = tkinter.Button(button_frame, text='Quit', 
                                 command=lambda:end_game(main_window))
    # Pack the button frame widgets
    spin_button.pack(side='left', padx=5, pady=5)
    quit_button.pack(side='left', padx=5, pady=5)

    # Pack the frames.
    image_frame.pack()
    entry_frame.pack()
    prize_frame.pack()
    win_frame.pack()
    button_frame.pack()

    # Start the main loop.
    main_window.mainloop()

def event_loop(bet_entry, fruit, image_list, image_label_list, prize, win):
    ''' 
    callback function for spin button 
    Retrieve the bet value
    Run the Event Loop until we break out
    '''
    global total_bet
    global total_wins
    
    
    # Get the bet value
    bet = bet_entry.get()
    

    # Run the Event Loop forever (until we break out) 
    # if there is a bet ( money entered into slots)
    if bet != '':

        # spin for three new fruit
        matches = spin(fruit, image_list, image_label_list)

        # Add bet to this games total bets
        bet = int(bet)
        total_bet += bet

        # Calculate prize amount based on number of matches
        if matches[0] == matches[1] or matches[1] == matches[2] or matches[2] == matches[0]:
            prize_amount = bet * 2
        elif matches[0] == matches[1] == matches[2]:
            prize_amount = bet * 4
        else:
            prize_amount = 0

        # Update prize amount
        prize.set(prize_amount)

        # Calculate total wins
        total_wins += prize_amount

    # Display message asking user to insert money before playing
    # if bet is empty (No coins entered into slot)
    else:

        # message to be displayed in small text dialog
        message_string = (f'Insert Money into Slot\n'
                f'Money must be inserted into machine before'
                f' play will start.')
        
        # title of said small dialog
        title_string = 'Insert Money into Slot Machine'

        # displays the message and title string on dialog
        tkinter.messagebox.showinfo(title=title_string, message=message_string)

    # Update win value for current slot
    win.set(total_wins)
    

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

    n1 = random.randrange(len(fruit)) # first random index # of fruit
    n2 = random.randrange(len(fruit)) # second random index # of fruit
    n3 = random.randrange(len(fruit)) # third random index # of fruit

    # changes each image in image_list to the new fruit file
    image_list[0] = tkinter.PhotoImage(file=fruit[n1])
    image_list[1] = tkinter.PhotoImage(file=fruit[n2])
    image_list[2] = tkinter.PhotoImage(file=fruit[n3])

    # switches each fruit label to new fruit image
    image_label_list[0].configure(image=image_list[0])
    image_label_list[1].configure(image=image_list[1])
    image_label_list[2].configure(image=image_list[2])

    # .config is used to change the text on a label
    # https://coderslegacy.com/python/tkinter-config/
    return n1, n2, n3

def end_game(main_window):
    '''
    Display total money entered into slots and total winnings
    in a message box.
    Stop the game.
    '''
    # message to be displayed on end dialog's title
    endtitle_string = 'Winnings'

    # the ending text to be displayed
    end_message = (f'Total money Entered: {total_bet}\n'
                f'Total Winnings: {total_wins}')
    
    # displays both title and message ending strings in dialog window
    tkinter.messagebox.showinfo(title=endtitle_string, message=end_message)

    # closes window when "OK" is clicked
    main_window.destroy()

    # pythonguides.com

# Create an instance of the main function.
if __name__ == '__main__':
    main()
    

