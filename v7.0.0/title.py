import customtkinter as ctk


class TitleUpdater:
    def __init__(self, master: ctk.CTk):
        self.master = master

        self.title = ctk.CTkLabel(
            self.master,
            text="Type your message and how many.",
            font=("Jetbrains Mono", 14, "bold"),
        )
        self.title.place(relx=0.5, rely=0.09, anchor="center")

    def update_title(self):
        # Change title
        self.title.configure(text="Hover the mouse to end.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.reset_title)

    def reset_title(self):
        # Change title back to the original text
        self.title.configure(text="Type your message and how many.")

        # Call the method again after 5 seconds
        self.master.after(5000, self.update_title)
