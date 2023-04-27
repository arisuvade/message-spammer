import customtkinter as ctk


def set_appearance_mode(mode):
    ctk.set_appearance_mode(mode)


class ThemeSwitch(ctk.CTkSwitch):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="Dark Mode",
            command=self.theme,
            **kwargs,
        )

    def theme(self):
        if self.get() == 1:
            set_appearance_mode("dark")
            self.configure(text="Light Mode")
        else:
            set_appearance_mode("light")
            self.configure(text="Dark Mode")
