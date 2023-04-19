import customtkinter as ctk


class CurrentProgressLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="Current",
            font=("Jetbrains Mono", 12),
            **kwargs,
        )


class CurrentProgressCount(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            text="0",
            font=("Jetbrains Mono", 16),
            **kwargs,
        )
