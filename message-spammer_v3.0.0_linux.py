import customtkinter as ctk
import pyautogui as pg
import time


class MessageSpammer:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("300x210")
        self.master.resizable(False, False)
        self.master.wm_title("Spammer")

        # Message
        self.msg = ctk.CTkEntry(
            self.master,
            placeholder_text="Message",
            width=250,
            height=30,
            border_width=2,
            corner_radius=10,
            font=("Jetbrains Mono", 14),
        )
        self.msg.place(relx=0.5, rely=0.2, anchor="center")

        # Message count
        self.count = ctk.CTkEntry(
            self.master,
            placeholder_text="Count",
            width=250,
            height=30,
            border_width=2,
            corner_radius=10,
            font=("Jetbrains Mono", 14),
        )
        self.count.place(relx=0.5, rely=0.4, anchor="center")

        # Send
        self.send = ctk.CTkButton(
            self.master,
            width=100,
            height=30,
            border_width=0,
            corner_radius=8,
            text="Send",
            command=self.send_msg,
            hover_color="red",
        )
        self.send.place(relx=0.5, rely=0.6, anchor="center")

        # Dark mode
        self.switch = ctk.CTkSwitch(
            self.master,
            text="Dark Mode",
            command=self.theme,
        )
        self.switch.place(relx=0.5, rely=0.8, anchor="center")
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
            self.error_label.configure(text="Error: Invalid number in count.")

    def theme(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


if __name__ == "__main__":
    app = ctk.CTk()
    gui = MessageSpammer(master=app)
    app.mainloop()
