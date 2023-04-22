import customtkinter as ctk
import pyautogui as pg
from time import sleep
from random import choice

from title_label import TitleLabel
from message_entry import MessageEntry
from count_entry import CountEntry
from delay_option import DelayOption
from send_button import SendButton
from theme_switch import ThemeSwitch
from error_label import ErrorLabel


class PyBlaster(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Window
        self.wm_title("PyBlaster")
        self.geometry("300x240")
        self.resizable(False, False)

        # Title
        self.title = TitleLabel(master=self)
        self.title.place(relx=0.5, rely=0.09, anchor="center")

        # Update title every 5 seconds
        self.after(5000, self.title.update_title)

        # Message
        self.msg = MessageEntry(self)
        self.msg.place(relx=0.5, rely=0.25, anchor="center")

        # Count
        self.count = CountEntry(self)
        self.count.place(relx=0.5, rely=0.4, anchor="center")

        # Delay
        self.delay_option = DelayOption(self)
        self.delay_option.place(relx=0.5, rely=0.55, anchor="center")

        # Send
        self.send = SendButton(self, command=self.send_msg)
        self.send.place(relx=0.5, rely=0.7, anchor="center")

        # Theme switch
        self.theme_switch = ThemeSwitch(self)
        self.theme_switch.place(relx=0.5, rely=0.85, anchor="center")

        # Error
        self.error_label = ErrorLabel(self)
        self.error_label.place(relx=0.5, rely=0.95, anchor="center")

    def send_msg(self):
        try:
            # Clear error message
            self.error_label.configure(text="")

            # Disable count input
            self.count.configure(state="disabled")

            # Get count from user input
            count = int(self.count.get())

            # To move the mouse and run
            height, width = pg.size()
            pg.click(height / 2, width / 4)
            pg.click()

            # To send the message
            pos = pg.position()
            for _ in range(count):
                # Check if the mouse position has changed to end the loop
                if pos != pg.position():
                    break

                # Send the message
                pg.typewrite(self.msg.get())
                pg.press("enter")

                match (self.delay_option.delay.get()):
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
            self.count.configure(state="normal")
