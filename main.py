import random

def draw_circle():
    circle = ('    -----    ','\n  /       \  ','\n |         | ','\n  \       /  ','\n    -----    ')
    print (circle)
    
def draw_lines():
    draw_character = input('Enter characters you want to repeat:')
    repeat_character = input('Please enter a number on how many times do you want to repeat the characters in one line:')
    while not repeat_character.isdigit and repeat_character < 0:
        repeat_character = input('Please enter a number on how many times do you want to repeat the characters in one line:')
    line_amount = input('Enter the number amount of lines you want to draw:')
    while not line_amount.isdigit and line_amount < 0:
        line_amount = input('Enter the number amount of lines you want to draw:')
    for _ in range(line_amount):
        print(draw_character * repeat_character)
        
def draw_random():
    num = random.randint(1,3)
    if num = 1:
        print('^')
    
    
def main():
    exit = 0
    
    print('Choose a number between 1-4.')
    print('Choosing 1 draws a circle.') 
    print('Choosing 2 allows you to repeat and draw lines of 1 or more characters.')
    print('Choosing 3 draws a random desgin out of three random designs.')
    print('Choosing 4 exits the code.')
    
    while exit != 4
    
        draw_choice = input('Enter your choice of drawing you want to see:')
        while not draw_choice.isdigit and not (0 < draw_choice <= 4)
            draw_choice = input('Enter your choice of drawing you want to see:')

        if draw_choice == '1':
            draw_circle()
        elif draw_choice == '2':
            draw_lines()
        elif draw_choice == '3':
            draw_random()
        elif draw_choice == '4':
            print('Thanks for using my program!')
            exit = 4

main()
    
    
    
    # Code goes here and DO NOT FORGET INTRO COMMENTS
