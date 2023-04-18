import customtkinter as ctk


class SendButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            width=100,
            height=30,
            border_width=0,
            corner_radius=8,
            text="Send",
            hover_color="red",
            **kwargs,
        )
