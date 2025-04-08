# gui/header.py

import customtkinter as ctk
from style import DARK_MODE_PALETTE

class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=80, fg_color=DARK_MODE_PALETTE["header_bg"])
        self.grid_columnconfigure(0, weight=1)
        # Área centralizada apenas para o título
        self.header_content = ctk.CTkFrame(self, fg_color="transparent")
        self.header_content.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        # Título centralizado
        self.title = ctk.CTkLabel(
            self.header_content, 
            text="VideoForge", 
            font=("Arial", 28, "bold"), 
            text_color=DARK_MODE_PALETTE["text"]
        )
        self.title.grid(row=0, column=0)
