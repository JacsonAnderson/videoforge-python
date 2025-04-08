# gui/sidebar.py
import customtkinter as ctk
from style import DARK_MODE_PALETTE

class SidebarModal(ctk.CTkFrame):
    def __init__(self, master, on_close_callback=None, on_menu_select=None):
        super().__init__(
            master,
            fg_color=DARK_MODE_PALETTE["sidebar_bg"],
            corner_radius=10,
            border_width=2,
            border_color=DARK_MODE_PALETTE["border"]
        )
        self.on_close_callback = on_close_callback
        self.on_menu_select = on_menu_select

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)

        # Botão de fechar
        self.close_button = ctk.CTkButton(
            self,
            text="X",
            width=35,
            height=35,
            fg_color=DARK_MODE_PALETTE["button_bg"],
            hover_color=DARK_MODE_PALETTE["hover"],
            corner_radius=20,
            command=self.close
        )
        self.close_button.place(relx=1.0, x=-10, y=10, anchor="ne")

        # --- Perfil ---
        self.profile_frame = ctk.CTkFrame(self, fg_color=DARK_MODE_PALETTE["sidebar_bg"])
        self.profile_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(50,20))
        self.profile_frame.grid_columnconfigure(0, weight=1)
        
        self.profile_pic = ctk.CTkLabel(
            self.profile_frame,
            text="Foto",
            width=80,
            height=80,
            fg_color=DARK_MODE_PALETTE["button_bg"],
            corner_radius=40
        )
        self.profile_pic.grid(row=0, column=0, pady=5)
        
        self.username_label = ctk.CTkLabel(
            self.profile_frame,
            text="VideoForge",
            font=("Arial", 18, "bold"),
            text_color=DARK_MODE_PALETTE["text"]
        )
        self.username_label.grid(row=1, column=0, pady=5)
        
        # --- Menu ---
        self.menu_frame = ctk.CTkFrame(self, fg_color=DARK_MODE_PALETTE["sidebar_bg"])
        self.menu_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)
        self.menu_frame.grid_columnconfigure(0, weight=1)
        
        menu_items = [
            "Dashboard",
            "Painel de Conteúdo",
            "AutoForge",
            "Configurações",
            "Ajuda"
        ]
        
        for i, item in enumerate(menu_items):
            # Se a callback foi definida, o comando do botão chama on_menu_select passando o item
            cmd = None
            if self.on_menu_select:
                cmd = lambda item=item: self.on_menu_select(item)
            btn = ctk.CTkButton(
                self.menu_frame,
                text=item,
                fg_color=DARK_MODE_PALETTE["button_bg"],
                hover_color=DARK_MODE_PALETTE["hover"],
                height=50,
                corner_radius=8,
                font=("Arial", 14),
                command=cmd
            )
            btn.grid(row=i, column=0, sticky="ew", pady=5, padx=5)
        
        # --- Footer Interno ---
        self.footer_frame = ctk.CTkFrame(self, fg_color=DARK_MODE_PALETTE["sidebar_bg"])
        self.footer_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=(10,20))
        self.footer_frame.grid_columnconfigure(0, weight=1)
        
        self.footer_label = ctk.CTkLabel(
            self.footer_frame,
            text="Versão De Produção 0.1",
            font=("Arial", 14),
            text_color=DARK_MODE_PALETTE["text"]
        )
        self.footer_label.grid(row=0, column=0)
    
    def close(self):
        if self.on_close_callback:
            self.on_close_callback()
