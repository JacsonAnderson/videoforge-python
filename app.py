import customtkinter as ctk
import platform
from style import DARK_MODE_PALETTE
from gui.header import Header
from gui.footer import Footer
from gui.sidebar import SidebarModal
from gui.main_content import MainContent
from autoforge.autoforge_gui import AutoForgeGUI

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VideoForge")
        self.configure(fg_color=DARK_MODE_PALETTE["bg"])
        self.geometry("1200x800")

        # Configuração do grid principal: header, body e footer
        self.grid_rowconfigure(0, weight=0)   # Header
        self.grid_rowconfigure(1, weight=1)   # Corpo
        self.grid_rowconfigure(2, weight=0)   # Footer
        self.grid_columnconfigure(0, weight=1)

        # Header
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky="ew")

        # Corpo
        self.body = ctk.CTkFrame(self, fg_color=DARK_MODE_PALETTE["bg"])
        self.body.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.body.grid_columnconfigure(0, weight=1)
        self.body.grid_rowconfigure(0, weight=1)

        # Conteúdo principal inicial (Dashboard padrão)
        self.main_content = MainContent(self.body)
        self.main_content.grid(row=0, column=0, sticky="nsew")

        # Footer
        self.footer = Footer(self)
        self.footer.grid(row=2, column=0, sticky="ew")

        # Botão fixo para abrir a Sidebar Modal
        self.sidebar_toggle_button = ctk.CTkButton(
            self,
            text="☰",
            width=35,
            height=35,
            fg_color=DARK_MODE_PALETTE["button_bg"],
            hover_color=DARK_MODE_PALETTE["hover"],
            corner_radius=0,
            border_width=0,
            font=("Arial", 16, "bold"),
            command=self.open_sidebar
        )
        self.sidebar_toggle_button.place(x=10, y=10)

        self.sidebar_modal = None

        self.after(10, self.maximize_window)

    def open_sidebar(self):
        if not self.sidebar_modal:
            self.sidebar_modal = SidebarModal(
                self,
                on_close_callback=self.close_sidebar,
                on_menu_select=self.on_menu_select
            )
            self.sidebar_modal.place(x=0, y=0, relwidth=0.18, relheight=1)
        else:
            self.close_sidebar()

    def close_sidebar(self):
        if self.sidebar_modal:
            self.sidebar_modal.place_forget()
            self.sidebar_modal = None

    def on_menu_select(self, item):
        if item == "AutoForge":
            self.open_autoforge()
        elif item == "Dashboard":
            self.open_dashboard()
        # Trate outros itens conforme necessário...
        self.close_sidebar()

    def open_autoforge(self):
        self.main_content.destroy()
        self.main_content = AutoForgeGUI(self.body)
        self.main_content.grid(row=0, column=0, sticky="nsew")

    def open_dashboard(self):
        self.main_content.destroy()
        from gui.main_content import MainContent
        self.main_content = MainContent(self.body)
        self.main_content.grid(row=0, column=0, sticky="nsew")

    def maximize_window(self):
        if platform.system() == "Windows":
            self.state("zoomed")
        else:
            sw = self.winfo_screenwidth()
            sh = self.winfo_screenheight()
            self.geometry(f"{sw}x{sh}+0+0")

if __name__ == "__main__":
    app = App()
    app.mainloop()
