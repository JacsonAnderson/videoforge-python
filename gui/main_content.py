# gui/main_content.py

import customtkinter as ctk
from style import DARK_MODE_PALETTE

class MainContent(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=DARK_MODE_PALETTE["bg"])
        self.label = ctk.CTkLabel(
            self,
            text="Bem-vindo à Plataforma VideoForge",
            font=("Arial", 20, "bold"),
            text_color=DARK_MODE_PALETTE["text"]
        )
        self.label.pack(pady=20)
        # Aqui você pode adicionar mais widgets conforme necessário
