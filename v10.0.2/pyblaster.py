import customtkinter as ctk

from title_label import TitleLabel
from message_options import MessageOptions
from message_entry import MessageEntry
from count_entry import CountEntry
from delay_options import DelayOptions
from send_button import SendButton
from theme_switch import ThemeSwitch
from error_label import ErrorLabel
from send_message import send_message


class PyBlaster(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Window
        self.wm_title("PyBlaster")
        self.geometry("300x260")
        self.resizable(False, False)

        # Title
        self.title = TitleLabel(self)
        self.title.place(relx=0.5, rely=0.05, anchor="center")

        # Message
        self.message_entry = MessageEntry(self)
        self.message_entry.place(relx=0.5, rely=0.31, anchor="center")

        # Message options
        self.message_options = MessageOptions(self, self.message_entry)
        self.message_options.place(relx=0.5, rely=0.17, anchor="center")

        # Count
        self.count_entry = CountEntry(self)
        self.count_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Delay
        self.delay_options = DelayOptions(self)
        self.delay_options.place(relx=0.5, rely=0.59, anchor="center")

        # Send
        self.send = SendButton(self, command=self.send_message)
        self.send.place(relx=0.5, rely=0.76, anchor="center")

        # Theme switch
        self.theme_switch = ThemeSwitch(self)
        self.theme_switch.place(relx=0.5, rely=0.88, anchor="center")

        # Error
        self.error_label = ErrorLabel(self)
        self.error_label.place(relx=0.5, rely=0.97, anchor="center")

    def send_message(self):
        send_message(
            self.error_label,
            self.count_entry.get(),
            self.message_options.message_option.get(),
            self.message_entry.get(),
            self.delay_options.time_delay.get(),
        )
