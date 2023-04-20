#!/usr/bin/env python3

import customtkinter as ctk
import pyautogui as pg
import time
from message_input import MessageInput
from count_input import CountInput
from send_button import SendButton
from title import TitleUpdater
from theme import ThemeSwitch
from error import ErrorLabel


class MessageSpammer:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("300x220")
        self.master.resizable(False, False)
        self.master.wm_title("Spammer")

        # Title
        self.title = TitleUpdater(master=self.master)
        # Update title every 5 seconds
        self.master.after(5000, self.title.update_title)

        # Message
        self.msg = MessageInput(self.master)
        self.msg.place(relx=0.5, rely=0.25, anchor="center")

        # Count
        self.count = CountInput(self.master)
        self.count.place(relx=0.5, rely=0.45, anchor="center")

        # Send
        self.send = SendButton(self.master, command=self.send_msg)
        self.send.place(relx=0.5, rely=0.65, anchor="center")

        # Theme switch
        self.theme_switch = ThemeSwitch(self.master)
        self.theme_switch.place(relx=0.5, rely=0.85, anchor="center")

        # Error
        self.error_label = ErrorLabel(self.master)
        self.error_label.place(relx=0.5, rely=0.95, anchor="center")

    def send_msg(self):
        try:
            # Clear error message
            self.error_label.configure(text="")

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
                time.sleep(0.3)

        except ValueError:
            # Show the error in app
            self.error_label.configure(text="Error: Invalid number in count.")


if __name__ == "__main__":
    app = ctk.CTk()
    gui = MessageSpammer(master=app)
    app.mainloop()
