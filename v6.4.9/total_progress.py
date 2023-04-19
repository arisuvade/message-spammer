import customtkinter as ctk


class TotalProgressLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="Total",
            font=("Jetbrains Mono", 12),
            **kwargs,
        )


class TotalProgressCount(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="0",
            font=("Jetbrains Mono", 12),
            **kwargs,
        )
