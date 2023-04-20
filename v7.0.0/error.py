import customtkinter as ctk


class ErrorLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="",
            font=("Jetbrains Mono", 12, "bold"),
            text_color="red",
            **kwargs,
        )
