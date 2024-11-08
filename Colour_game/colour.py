import tkinter
import random

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30
def startGame(event):
	
	if timeleft == 30:
		# start the timer
		countdown()
		
	# run the function to choose the next colour.
	nextColour()

# Function to choose and display the next colour.
def nextColour():

	# take globally declared score and timeleft
	global score
	global timeleft

    #runs till timeleft  is not 0 second
	if timeleft > 0:

		# make the text entry box 
		e.focus_set()
		# if the colour typed is equal to the colour of the text
		if e.get().lower() == colours[1].lower():
			
			score += 1

		# clear the text entry box.
		e.delete(0, tkinter.END)
		
		#using random shuffle the list 
		random.shuffle(colours)
		
		# change the display colour of text and  to new colour name .........  
		label.config(fg = str(colours[1]), text = str(colours[0]))
		
		# update the score.
		scoreLabel.config(text = "Score: " + str(score))


# timer function 
def countdown():
    
	global timeleft

	# if a game is in play
	if timeleft > 0:

		# decrease the time which is being displayed
		timeleft -= 1
		
		# update the time left label
		timeLabel.config(text = "Time left: "+ str(timeleft))
								
		# run the function again after 1 second ,here 1000 is in milliseconds    recursion
		timeLabel.after(1000, countdown)



# create a  window
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("500x600")

# add an instructions label
instructions = tkinter.Label(root, text = "What's ta color ?🤪",font = ('Arial', 34))
instructions.pack() 

# add a score label
scoreLabel = tkinter.Label(root, text = "enter to start",font = ('Arial', 22))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "time " +str(timeleft), font = ('Arial', 22))			
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Arial', 60))
label.pack()

# add a text entry box for typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function  when the enter key is pressed    | <Return> means enter key 
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box so that we can type using keyboard
e.focus_set()

# start the GUI
root.mainloop()
