import customtkinter as ctk


class MessageOptions(ctk.CTkOptionMenu):
    def __init__(self, parent, message_entry, **kwargs):
        self.message_option = ctk.StringVar(value="Normal message")
        self.message_entry = message_entry

        super().__init__(
            parent,
            values=[
                "Normal message",
                "With numbers",
                "Random number",
                "Random word",
                "Random animal",
                "Random pokemon",
            ],
            variable=self.message_option,
            font=("Jetbrains Mono", 14),
            **kwargs,
        )
        self.set("Normal message")
        self.message_option.trace_add("write", self.callback)

    def callback(self, *args):
        self.message_entry.configure(state="normal")
        self.message_entry.configure(placeholder_text="")
        option = self.message_option.get()

        if option in ("Normal message", "With numbers"):
            self.message_entry.delete(0, "end")
            self.message_entry.configure(state="normal")
            match (option):
                case "Normal message":
                    self.message_entry.configure(placeholder_text="Message")
                case "With numbers":
                    self.message_entry.configure(placeholder_text="1. Message")

        else:
            self.message_entry.delete(0, "end")
            match (option):
                case "Random number":
                    self.message_entry.configure(
                        placeholder_text="Random numbers between 0-99"
                    )
                case "Random word":
                    self.message_entry.configure(placeholder_text="Random english word")
                case "Random animal":
                    self.message_entry.configure(
                        placeholder_text="Random animal in english"
                    )
                case "Random pokemon":
                    self.message_entry.configure(
                        placeholder_text="Random pokemon from Gen 1-8"
                    )
            self.message_entry.configure(state="readonly")
