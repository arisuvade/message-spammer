import customtkinter as ctk
import pyautogui as pg


class MessageSpammer:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("300x200")
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

    def send_msg(self):
        # To move the mouse and run
        height, width = pg.size()
        pg.click(height / 2, width / 4)
        pg.click()

        # To send the message
        # Will start the execution if the mouse hovers
        pos = pg.position()
        for _ in range(int(self.count.get())):
            if pos == pg.position():
                pg.typewrite(self.msg.get())
                pg.press("Enter")

    def theme(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


if __name__ == "__main__":
    app = ctk.CTk()
    gui = MessageSpammer(master=app)
    app.mainloop()
