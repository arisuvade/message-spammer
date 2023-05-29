import customtkinter as ctk


class TitleLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="Pick a message type in options",
            font=("Jetbrains Mono", 14, "bold"),
            **kwargs,
        )

        self.after(5000, self.update_title_1)

    def update_title_1(self):
        self.configure(text="Enter a message and how many")
        self.master.after(5000, self.update_title_2)

    def update_title_2(self):
        self.configure(text="Hover the mouse to end")
        self.master.after(5000, self.reset_title)

    def reset_title(self):
        self.configure(text="Pick a message type in options")
        self.master.after(5000, self.update_title_1)
