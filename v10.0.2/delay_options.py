import customtkinter as ctk


class DelayOptions(ctk.CTkOptionMenu):
    def __init__(self, parent, **kwargs):
        self.time_delay = ctk.StringVar(value="Instant")
        super().__init__(
            parent,
            values=["Instant", "0.5 second", "1 second", "2 seconds", "Random"],
            variable=self.time_delay,
            font=("Jetbrains Mono", 14),
            **kwargs,
        )
        self.set("Instant")
