# gui/footer.py

import customtkinter as ctk
from style import DARK_MODE_PALETTE

class Footer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=40, fg_color=DARK_MODE_PALETTE["header_bg"])
        self.grid_columnconfigure(0, weight=1)
        self.label = ctk.CTkLabel(
            self,
            text="© 2025 VideoForge. Todos os direitos reservados.",
            font=("Arial", 12),
            text_color=DARK_MODE_PALETTE["text"]
        )
        self.label.grid(row=0, column=0, padx=20, pady=5)
