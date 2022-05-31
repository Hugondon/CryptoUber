import tkinter as tk


from tkinter import ttk, Toplevel
from frames.const import *


class Profile(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style)

        self.controller = controller

        """ ATTRIBUTES """

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        offers_label = ttk.Label(
            self,
            text="Details",
            style="ProfileTitle2.TLabel"
        )

        offers_label.grid(row=0, column=0, sticky="EW",
                          padx=(45, 0), pady=(5, 10))

        """ SECOND ROW """
        # imgs

        """ THIRD ROW """
        name_label = ttk.Label(
            self,
            text="Name: Juan",
            style="ProfileInformation.TLabel"
        )
        id_label = ttk.Label(
            self,
            text="Account: 0x531441",
            style="ProfileInformation.TLabel"
        )
        balance_label = ttk.Label(
            self,
            text="Balance: 0.12 ETH",
            style="ProfileInformation.TLabel"
        )

        name_label.grid(row=2, column=0, sticky="EW",
                        padx=(10, 0))
        id_label.grid(row=3, column=0, sticky="EW",
                      padx=(10, 0))
        balance_label.grid(row=4, column=0, sticky="EW",
                      padx=(10, 0))

        """ FOURTH ROW """
        add_offer_button = ttk.Button(
            self,
            text="Add Offer",
            command=self.callback_add_offer,
            style="ProfileInformationButton.TButton",
            width=15,
            cursor="hand2"
        )
        update_balance_button = ttk.Button(
            self,
            text="Update Balance",
            command=self.callback_updating_balance,
            style="ProfileInformationButton.TButton",
            width=15,
            cursor="hand2"
        )
        edit_profile_button = ttk.Button(
            self,
            text="Edit Profile",
            command=self.callback_edit_profile,
            style="ProfileInformationButton.TButton",
            width=15,
            cursor="hand2"
        )
        
        add_offer_button.grid(row=5, column=0, sticky="S", padx=(10,5), pady=(390,10))
        update_balance_button.grid(row=6, column=0, sticky="S", padx=(10,5), pady=(0, 10))
        edit_profile_button.grid(row=7, column=0, sticky="S", padx=(10,5), pady=(0,10))
                
        """
        Transferencias
        SmartContract
        
        """
    
    def callback_add_offer(self):
        
        WIDTH, HEIGHT = 700,250
        offer_window= Toplevel(self)
        
        offer_window.title("New Offer")
        offer_window.geometry(f"{WIDTH}x{HEIGHT}")
        offer_window.iconbitmap(self.controller.ICON_ICO_PATH)
        
        container = ttk.Frame(offer_window, style="ProfileFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        container.columnconfigure(0, minsize=WIDTH, weight=1) 
        container.rowconfigure(0, minsize=HEIGHT, weight=1)
        
        title_label = ttk.Label(container,
                            text= "New Offer!",
                            style="TextTitle.TLabel",
                            )

        title_label.grid(row=0, column=0, sticky="WE")
    
    def callback_updating_balance(self):
        print("Updating Balance")
        # GET BALANCE
        
        # send_transaction Transaccion falsa :D
        
        # IMPRIMIR DE ALGUNA FORMA EL RECIBO :)
    
    def callback_edit_profile(self):
        WIDTH, HEIGHT = 700,250
        
        profile_window= Toplevel(self)
        
        profile_window.title("Profile Settings")
        profile_window.geometry(f"{WIDTH}x{HEIGHT}")
        profile_window.iconbitmap(self.controller.ICON_ICO_PATH)
        
        container = ttk.Frame(profile_window, style="AppFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        container.columnconfigure(0, minsize=WIDTH, weight=1) 
        container.rowconfigure(0, minsize=HEIGHT, weight=1)
        
        title_label = ttk.Label(container,
                            text= "Edit Your Profile!",
                            style="TextTitle.TLabel",
                            )

        title_label.grid(row=0, column=0, sticky="WE", padx=(10,0))