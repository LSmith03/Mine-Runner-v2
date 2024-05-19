from classes import Window
from classes import Game
from graphics import GraphicsError

def run_menu():
    window = Window()
    try:
        while True:
            selected_button = window.display_menu()
            if selected_button == window.buttons[0]:  # Play button
                game = Game(window)
                run_game(game)
            elif selected_button == window.buttons[1]:  # Instructions button
                show_instructions(window)
            elif selected_button == window.buttons[2]:  # Exit button
                window.window.close()
                break
    except GraphicsError:
        print("Window was closed -> Exiting game.")


def run_game(game):
    game.play()

def show_instructions(window):
    back_button = window.display_instructions()
    while True:
        click = window.window.getMouse()
        if window.is_inside(click, back_button):
            break  