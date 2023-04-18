import customtkinter as ctk


class TotalProgress(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="0",
            font=("Jetbrains Mono", 12),
            **kwargs,
        )
