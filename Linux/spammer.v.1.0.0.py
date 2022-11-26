import tkinter as tk
import pyautogui as pg


root = tk.Tk()
root.title("Spammer")
root.configure(background="#2C3333")


def send():
    text = textbox.get()

    # Center of the monitor.
    height, width = pg.size()
    pg.click(height / 2, width / 2)

    # Will end if you move your mouse.
    pos = pg.position()
    while pos == pg.position():
        pg.write(text)
        pg.press("Enter")


textbox = tk.Entry(
    root,
    width=25,
    borderwidth=5,
    fg="white",
    bg="#395B64",
    font=(7),
    relief="flat",
)
textbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

send_btn = tk.Button(
    root,
    text="Send",
    bg="#A5C9CA",
    font=("monospace", 10, "bold"),
    padx=40,
    borderwidth=5,
    command=send,
)
send_btn.grid(column=0, row=1, columnspan=4)

root.mainloop()
