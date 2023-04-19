import customtkinter as ctk


class CountInput(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            placeholder_text="Count",
            width=250,
            height=30,
            border_width=2,
            corner_radius=10,
            font=("Jetbrains Mono", 14),
            **kwargs,
        )

    def disable(self):
        self.configure(state="disabled")

    def enable(self):
        self.configure(state="normal")
