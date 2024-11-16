import random
# Function Outputs a circle
def draw_circle():
    print ('    -----    ','\n  /       \  ','\n |         | ','\n  \       /  ','\n    -----    ')

# Function outputs line/s based on user input    
def draw_lines():
    # Prompt user to input what character they want to repeat
    draw_character = input('Enter characters you want to repeat:')
    # Prompt the user to input how many times they want to repeat the character in one line and prevent bad input from the user 
    repeat_character = input('Please enter a number on how many times do you want to repeat the characters in one line:')
    while not repeat_character.isdigit() or int(repeat_character) <= 0:
        repeat_character = input('Please enter a number on how many times do you want to repeat the characters in one line:')
    repeat_character = int(repeat_character)
    # Prompt user to input how many lines they want to repeat 
    line_amount = input('Enter the number amount of lines you want to draw:')
    while not line_amount.isdigit() or int(line_amount) <= 0:
        line_amount = input('Enter the number amount of lines you want to draw:')
    line_amount = int(line_amount)
    # Output 
    for _ in range(line_amount):
        print(draw_character * repeat_character)
        
# Function outputs a random Ascii art 
def draw_random():
    num = random.randint(1,3)
    if num == 1:
        print('  ^--^','\n (., .)','\n (>  <)','\n_l    l_')
    elif num == 2:
        print('  n___n','\n (o - o)','\n/|     |\\','\n |__ __|','\n/       \\')
    elif num == 3:
        print('  n___n','\n (o - o)','\n/|     |\=)=====>','\n |__ __|','\n/       \\')
    
# Create the main function    
def main():
    # Create a Sentinel 
    exit = 0
    
    while exit != 4:
        # Output a description of the options for Ascii Art
        print('Choose a number between 1-4.')
        print('Choosing 1 draws a circle.') 
        print('Choosing 2 allows you to repeat and draw lines of 1 or more characters.')
        print('Choosing 3 draws a random desgin out of three random designs.')
        print('Choosing 4 exits the code.')
        
        # Prompt the user to input the matching value for the choice of drawing they want to output and prevent bad input from the user.
        draw_choice = input('Enter your choice of drawing you want to see:')
        while not draw_choice.isdigit and not (0 < draw_choice <= 4):
            draw_choice = input('Enter your choice of drawing you want to see:')
            
        # Based on the input of the draw_choice call the corresponding function to output the Ascii Art and stop the program when '4' is the input
        if draw_choice == '1':
            draw_circle()
        elif draw_choice == '2':
            draw_lines()
        elif draw_choice == '3':
            draw_random()
        elif draw_choice == '4':
            print('Thanks for using my program!')
            exit = 4
# run the main function
main()
    
