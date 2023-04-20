import customtkinter as ctk


class DelayOption(ctk.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        self.delay = ctk.StringVar(value="0.5 second")
        super().__init__(
            master,
            values=["0.5 second", "1 second", "2 seconds", "Random"],
            variable=self.delay,
            font=("Jetbrains Mono", 14),
            **kwargs,
        )
        self.set("0.5 second")
