import customtkinter as ctk


class ErrorLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text="",
            font=("Jetbrains Mono", 12, "bold"),
            text_color="red",
            **kwargs,
        )
