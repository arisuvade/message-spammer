import customtkinter as ctk


class MessageEntry(ctk.CTkEntry):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            placeholder_text="Message",
            width=250,
            height=30,
            border_width=2,
            corner_radius=10,
            font=("Jetbrains Mono", 14, "bold"),
            **kwargs,
        )
