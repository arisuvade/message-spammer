import customtkinter as ctk


class TitleLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="Type your message and how many.",
            font=("Jetbrains Mono", 14, "bold"),
            **kwargs,
        )

    def update_title(self):
        # Change title
        self.configure(text="Hover the mouse to end.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.reset_title)

    def reset_title(self):
        # Change title back to the original text
        self.configure(text="Type your message and how many.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.update_title)
