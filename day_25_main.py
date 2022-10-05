import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S States Game')
image = 'day_25_blank_states_img.gif'
screen.addshape(image)
background = turtle.shape(image)

data = pandas.read_csv('day_25_50_states.csv')
states = data.state.to_list()
states_to_learn = states

game_is_on = True
num = 0
while game_is_on:
    answer_state = screen.textinput(title=f'{num}/50 States Correct', prompt='What\'s another state\'s name?').title()
    if answer_state == 'Exit':
        data_dict = {'States to learn': states_to_learn}
        state_file = pandas.DataFrame(data_dict)
        state_file.to_csv('day_25_states_to_learn')
        break
    if answer_state in states:
        state_list = data[data.state == f'{answer_state}']
        num += 1
        x_cord = int(state_list.x)
        y_cord = int(state_list.y)
        t = turtle.Turtle()
        t.color('black')
        t.pu()
        t.hideturtle()
        t.goto(x_cord, y_cord)
        t.write(f'{answer_state}', align='center', font=('Courier', 10, 'normal'))
        states_to_learn.remove(answer_state)
        if num >= 50:
            game_is_on = False









