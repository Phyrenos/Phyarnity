import tkinter as tk
from tkinter import ttk
import json
import os


class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Phyarnity")

        self.scroll_frame = ttk.Frame(self.master)
        self.scroll_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scroll_frame, width=1000, height=400)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.y_scrollbar = ttk.Scrollbar(self.scroll_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.x_scrollbar = ttk.Scrollbar(self.scroll_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas.configure(yscrollcommand=self.y_scrollbar.set, xscrollcommand=self.x_scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas, bg="lightgray")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")  # Anchor to top-left corner

        self.row_count = 0
        self.col_count = 0

        def box_clicked(text: str):
            print(text)

        def GetJson():
            appdata_path = os.path.expanduser(os.getenv('APPDATA'))
            file_path = os.path.join(appdata_path, "Phyarnity/")

            with open(file_path + "db.json", "r") as e:
                return json.load(e)

        def create_box(text):
            box = tk.Button(self.inner_frame, text=text, width=25, height=20, command=lambda: box_clicked("wow"))
            box.grid(row=self.row_count, column=self.col_count, padx=5, pady=5)
            self.col_count += 1
            if self.col_count == 4:
                self.col_count = 0
                self.row_count += 1

        for item in GetJson():
            create_box(item["Name"])

        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))


def start():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
