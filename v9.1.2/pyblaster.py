import customtkinter as ctk
import pyautogui as pg
from time import sleep
from random import randint, choice

from title_label import TitleLabel
from message_options import MessageOptions
from message_entry import MessageEntry
from count_entry import CountEntry
from delay_options import DelayOptions
from send_button import SendButton
from theme_switch import ThemeSwitch
from error_label import ErrorLabel


class PyBlaster(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Window
        self.wm_title("PyBlaster")
        self.geometry("300x260")
        self.resizable(False, False)

        # Title
        self.title = TitleLabel(self)
        self.title.place(relx=0.5, rely=0.05, anchor="center")

        # Update title every 5 seconds
        self.after(5000, self.title.update_title)

        # Message
        self.message_entry = MessageEntry(self)
        self.message_entry.place(relx=0.5, rely=0.31, anchor="center")

        # Message options
        self.message_options = MessageOptions(self, self.message_entry)
        self.message_options.place(relx=0.5, rely=0.17, anchor="center")

        # Count
        self.count_entry = CountEntry(self)
        self.count_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Delay
        self.delay_options = DelayOptions(self)
        self.delay_options.place(relx=0.5, rely=0.59, anchor="center")

        # Send
        self.send = SendButton(self, command=self.send_msg)
        self.send.place(relx=0.5, rely=0.76, anchor="center")

        # Theme switch
        self.theme_switch = ThemeSwitch(self)
        self.theme_switch.place(relx=0.5, rely=0.88, anchor="center")

        # Error
        self.error_label = ErrorLabel(self)
        self.error_label.place(relx=0.5, rely=0.97, anchor="center")

    def send_msg(self):
        try:
            # Clear error message
            self.error_label.configure(text="")

            # Disable count input
            self.count_entry.configure(state="disabled")

            # Get count from user input
            count = int(self.count_entry.get())

            # To move the mouse and run
            height, width = pg.size()
            pg.click(height / 2, width / 4)
            pg.click()

            # To send the message
            pos = pg.position()
            for i in range(count):
                # Check if the mouse position has changed to end the loop
                if pos != pg.position():
                    break

                # Send the message
                match (self.message_options.message_option.get()):
                    case "Normal message":
                        pg.typewrite(self.message_entry.get())
                    case "With numbers":
                        pg.typewrite(f"{i + 1}. {self.message_entry.get()}")
                    case "Random number":
                        pg.typewrite(randint(0, 99))
                    case "Random word":
                        pass
                    case "Random pokemon":
                        pass
                pg.press("enter")

                # Time delay
                match (self.delay_options.time_delay.get()):
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
            # Show the error in app
            self.error_label.configure(text="Error: Invalid number in count.")

        finally:
            # Enable count input after message sending is complete or error handle
            self.count_entry.configure(state="normal")
