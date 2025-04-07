import customtkinter as ctk
import platform
from style import DARK_MODE_PALETTE
from gui.header import Header
from gui.footer import Footer
from gui.sidebar import SidebarModal
from gui.main_content import MainContent

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VideoForge")
        self.configure(fg_color=DARK_MODE_PALETTE["bg"])
        self.geometry("1200x800")

        # Configuração do grid principal: header, body e footer
        self.grid_rowconfigure(0, weight=0)   # Header
        self.grid_rowconfigure(1, weight=1)   # Corpo (Main Content)
        self.grid_rowconfigure(2, weight=0)   # Footer
        self.grid_columnconfigure(0, weight=1)

        # Cria o Header e posiciona na parte superior
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky="ew")

        # Cria um frame para o corpo que conterá o conteúdo principal
        self.body = ctk.CTkFrame(self, fg_color=DARK_MODE_PALETTE["bg"])
        self.body.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.body.grid_columnconfigure(0, weight=1)
        self.body.grid_rowconfigure(0, weight=1)

        # Cria o MainContent dentro do body
        self.main_content = MainContent(self.body)
        self.main_content.grid(row=0, column=0, sticky="nsew")

        # Cria o Footer na parte inferior
        self.footer = Footer(self)
        self.footer.grid(row=2, column=0, sticky="ew")

        # Botão fixo para abrir a Sidebar Modal (exemplo com ícone "☰", tamanho maior e fonte personalizada)
        self.sidebar_toggle_button = ctk.CTkButton(
            self,
            text="☰",
            width=35,
            height=35,
            fg_color=DARK_MODE_PALETTE["button_bg"],
            hover_color=DARK_MODE_PALETTE["hover"],
            corner_radius=0,          # Remove o arredondamento
            border_width=0,           # Remove a borda
            font=("Arial", 16, "bold"),
            command=self.open_sidebar
        )
        self.sidebar_toggle_button.place(x=10, y=10)

        # Variável para armazenar a Sidebar Modal aberta (se existir)
        self.sidebar_modal = None

        # Maximiza a janela após iniciar (dependendo do SO)
        self.after(10, self.maximize_window)

    def open_sidebar(self):
        if not self.sidebar_modal:
            # Exibe a Sidebar Modal como overlay à esquerda, ocupando 18% da largura
            self.sidebar_modal = SidebarModal(self, on_close_callback=self.close_sidebar)
            self.sidebar_modal.place(x=0, y=0, relwidth=0.18, relheight=1)
        else:
            self.close_sidebar()

    def close_sidebar(self):
        if self.sidebar_modal:
            self.sidebar_modal.place_forget()
            self.sidebar_modal = None

    def maximize_window(self):
        if platform.system() == "Windows":
            self.state("zoomed")
        else:
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            self.geometry(f"{screen_width}x{screen_height}+0+0")

if __name__ == "__main__":
    app = App()
    app.mainloop()
