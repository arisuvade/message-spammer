import customtkinter as ctk


def set_appearance_mode(mode):
    ctk.set_appearance_mode(mode)


class ThemeSwitch:
    def __init__(self, master):
        self.switch = ctk.CTkSwitch(
            master,
            text="Dark Mode",
            command=self.theme,
        )
        self.switch.place(relx=0.5, rely=0.8, anchor="center")

    def theme(self):
        if self.switch.get() == 1:
            set_appearance_mode("dark")
        else:
            set_appearance_mode("light")
