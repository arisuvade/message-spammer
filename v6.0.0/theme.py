import customtkinter as ctk


def set_appearance_mode(mode):
    ctk.set_appearance_mode(mode)


class ThemeSwitch(ctk.CTkSwitch):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="Dark Mode",
            command=self.theme,
            **kwargs,
        )

    def theme(self):
        if self.switch.get() == 1:
            set_appearance_mode("dark")
        else:
            set_appearance_mode("light")
