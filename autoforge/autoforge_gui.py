# autoforge/autoforge_gui.py
import customtkinter as ctk
from style import DARK_MODE_PALETTE

class AutoForgeGUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=DARK_MODE_PALETTE["bg"])
        self.label = ctk.CTkLabel(
            self,
            text="AutoForge GUI",
            font=("Arial", 24, "bold"),
            text_color=DARK_MODE_PALETTE["text"]
        )
        self.label.pack(pady=20)
        # Adicione outros widgets conforme necessário
