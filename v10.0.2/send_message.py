import pyautogui as pg
from time import sleep
from random import randint, choice
from os import path


def send_message(error_label, count, message_options, message_entry, delay_options):
    try:
        # Clear error message
        error_label.configure(text="")

        # To move the mouse and run
        height, width = pg.size()
        pg.click(height / 2, width / 4)
        pg.click()

        # To send the message
        pos = pg.position()
        for i in range(int(count)):
            # Check if the mouse position has changed to end the loop
            if pos != pg.position():
                break

            # Send the message
            dir_path = path.dirname(path.abspath(__file__))

            match (message_options):
                case "Normal message":
                    pg.typewrite(message_entry)
                case "With numbers":
                    pg.typewrite(f"{i + 1}. {message_entry}")
                case "Random number":
                    pg.typewrite(f"{randint(0, 99)}")

                case "Random word":
                    words = []
                    with open(path.join(dir_path, "data", "words.txt"), "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            words.append(line.strip().capitalize())
                    pg.typewrite(choice(words))

                case "Random animal":
                    animals = []
                    with open(path.join(dir_path, "data", "animals.txt"), "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            animals.append(line.strip())
                    pg.typewrite(choice(animals))

                case "Random pokemon":
                    pokemons = []
                    with open(path.join(dir_path, "data", "pokemons.txt"), "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            pokemons.append(line.strip().capitalize())
                    pg.typewrite(choice(pokemons))

            pg.press("enter")

            # Time delay
            match (delay_options):
                case "Instant":
                    pass
                case "0.5 second":
                    sleep(0.5)
                case "1 second":
                    sleep(1)
                case "2 seconds":
                    sleep(2)
                case "Random":
                    delay_times = [0.5, 1, 2]
                    sleep(choice(delay_times))

    except ValueError:
        raise ValueError("Error: Invalid number in count.")
