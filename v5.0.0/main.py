#!/usr/bin/env python3

import customtkinter as ctk
import pyautogui as pg
import time

from message_input import MessageInput
from count_input import CountInput
from send_button import SendButton

from title import TitleUpdater
from theme import ThemeSwitch


class MessageSpammer:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("300x210")
        self.master.resizable(False, False)
        self.master.wm_title("Spammer")

        # Title
        self.title = TitleUpdater(master=self.master)

        # Call update_title method every 3 seconds
        self.master.after(3000, self.title.update_title)

        # Message
        self.msg = MessageInput(self.master)
        self.msg.place(relx=0.5, rely=0.2, anchor="center")

        # Count
        self.count = CountInput(self.master)
        self.count.place(relx=0.5, rely=0.4, anchor="center")

        # Send
        self.send = SendButton(self.master, command=self.send_msg)
        self.send.place(relx=0.5, rely=0.6, anchor="center")

        # Theme switch
        self.theme_switch = ThemeSwitch(self.master)

        # Error
        self.error_label = ctk.CTkLabel(
            self.master,
            text="",
            font=("Jetbrains Mono", 12, "bold"),
            text_color="red",
        )
        self.error_label.place(relx=0.5, rely=0.93, anchor="center")

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

                # Will end the execution if the mouse hovers
                if pos == pg.position():
                    pg.typewrite(self.msg.get())
                    pg.press("Enter")
                    time.sleep(0.3)

        except ValueError:
            # Show the error in app
            self.error_label.configure(text="Error: Invalid number in count.")


if __name__ == "__main__":
    app = ctk.CTk()
    gui = MessageSpammer(master=app)
    app.mainloop()
