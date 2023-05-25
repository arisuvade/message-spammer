import customtkinter as ctk


class TitleLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="Pick a message type in options.",
            font=("Jetbrains Mono", 14, "bold"),
            **kwargs,
        )

        # Update title every 5 seconds
        self.after(5000, self.update_title_1)

    def update_title_1(self):
        # Change title
        self.configure(text="Enter a message and how many.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.update_title_2)

    def update_title_2(self):
        # Change title
        self.configure(text="Hover the mouse to end.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.reset_title)

    def reset_title(self):
        # Change title back to the original text
        self.configure(text="Pick a message type in options.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.update_title_1)
