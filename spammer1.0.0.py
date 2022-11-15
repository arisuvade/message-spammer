import tkinter as tk
import pyautogui as pg

root = tk.Tk()
root.title("Spammer")
root.configure(background="#2C3639")


def send():
    text = e.get()
    pg.click(644, 650)  # Move to the right location. Use position function.
    pos = pg.position()
    while pos == pg.position():  # Will end if mouse change position
        pg.typewrite(text)
        pg.press("Enter")


e = tk.Entry(
    root,
    width=25,
    borderwidth=5,
    bg="#A5C9CA",
    font=(7),
    relief="flat",
)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

c = tk.Button(
    root,
    text="Send",
    bg="#A27B5C",
    font=("monospace", 10, "bold"),
    padx=40,
    borderwidth=5,
    command=send,
)
c.grid(column=0, row=1, columnspan=4)

root.mainloop()
