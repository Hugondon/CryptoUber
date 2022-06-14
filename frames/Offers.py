from tkinter.font import NORMAL
import settings
import tkinter as tk

from tkinter import CENTER, DISABLED, ttk, Toplevel, messagebox
from frames.const import *
from PIL import ImageTk, Image
from utils.example_drivers import *

class OfferRow(ttk.Frame):
    def __init__(self, parent, index):
        super().__init__(parent, width=50, height=75)
        
        """ ATTRIBUTE """
        self.parent = parent
        self.index = index
        
        self.active = False
        self.checkbox_value = tk.BooleanVar(self)
        self.checkbox_value.set(False)
        self.checkbox = ttk.Checkbutton(
            parent,
            variable=self.checkbox_value, 
            command=self.checkbox_clicked,
            style="OffersCheckButton.TCheckbutton",
        )

        self.driver_str = tk.StringVar()
        self.start_travel_time_str = tk.StringVar()
        self.destination_str = tk.StringVar()
        self.number_of_seats_str = tk.StringVar()
        self.cost_eth_str = tk.StringVar()
        self.cost_eth = 0;
        self.expiration_time_s = tk.IntVar()
        
        self.account_str = ""
        
        self.driver_label = ttk.Label(
            parent,
            textvariable=self.driver_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.start_travel_time_label = ttk.Label(
            parent,
            textvariable=self.start_travel_time_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.destination_label = ttk.Label(
            parent,
            textvariable=self.destination_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.seats_label = ttk.Label(
            parent,
            textvariable=self.number_of_seats_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.cost_label = ttk.Label(
            parent,
            textvariable=self.cost_eth_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        

        self.driver_label.config(anchor=CENTER)
        self.start_travel_time_label.config(anchor=CENTER)
        self.destination_label.config(anchor=CENTER)
        self.seats_label.config(anchor=CENTER)
        self.cost_label.config(anchor=CENTER)
        
    def checkbox_clicked(self):
        
        def callback_accept_offer():
            self.checkbox_value.set(False)
            self.parent.enable_checkbuttons()            
            
            if(self.parent.controller.current_user.withdraw_from_account(amount=self.cost_eth)):
                greeter_contract = self.parent.controller.web3.eth.contract(abi=self.smart_contract_abi, bytecode=self.smart_contract_bytecode)
                tx_hash = greeter_contract.constructor().transact()
                transaction_receipt = self.parent.controller.web3.eth.wait_for_transaction_receipt(tx_hash)
                print(f"Hash: {self.parent.controller.web3.toHex(tx_hash)}")
                print(f"Contact Address: {transaction_receipt.contractAddress}")

                self.parent.delete_offer(self.index, offer_was_accepted=True, transaction_receipt=transaction_receipt)
                offer_window.destroy()  
            else:    
                messagebox.showerror(
                    message=f"Insufficient Funds!",
                    title="Error"
                )
            
        def callback_cancel_offer():
            self.checkbox_value.set(False)
            self.parent.enable_checkbuttons()
            offer_window.destroy()
            
        def callback_dismiss_offer():
            self.checkbox_value.set(False)
            self.parent.enable_checkbuttons()
            self.parent.delete_offer(self.index, offer_was_accepted=False)
            offer_window.destroy()
            
        def update_timer():
            if(self.expiration_time_s.get() == 0):
                self.checkbox_value.set(False)
                self.parent.enable_checkbuttons()
                self.parent.delete_offer(self.index, offer_was_accepted=False)
                offer_window.destroy()
            else:
                self.expiration_time_s.set(self.expiration_time_s.get() - 1)
                time_label.after(1000, update_timer)

        WIDTH, HEIGHT = 460,260
        offer_window= Toplevel(self, bg=COLOR_OFFER_SELECTION_BACKGROUND)
        
        offer_window.title("New Offer Selected")
        offer_window.geometry(f"{WIDTH}x{HEIGHT}")
        offer_window.iconbitmap(self.parent.controller.ICON_ICO_PATH)
        
        container = ttk.Frame(offer_window, style="OfferSelectionFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")

        self.parent.disable_checkbuttons(self.index)
        
        """ LAYOUT """
        title_frame = ttk.Frame(
            container,
            style="OfferSelectionFrame.TFrame"
        )
        
        information_frame = ttk.Frame(
            container,
            style="OfferSelectionFrame.TFrame"
        )
        
        timer_frame = ttk.Frame(
            container,
            style="OfferSelectionFrame.TFrame"
        )
                
        buttons_frame = ttk.Frame(
            container,
            style="OfferSelectionFrame.TFrame"
        )

        title_label = ttk.Label(title_frame,
                            text= "New Offer Selected",
                            style="OfferSelectionTitle2.TLabel",
                            )
        title_label.grid(column=0, row=0, sticky="W") 

        driver_name_label = ttk.Label(information_frame,
                            text= "Driver: ",
                            style="OfferSelectionText.TLabel",
                            )

        account_label = ttk.Label(information_frame,
                            text= "Account: ",
                            style="OfferSelectionText.TLabel",
                            )
        driver_name_text = ttk.Label(information_frame,
                            textvariable=self.driver_str,
                            style="OfferSelectionText.TLabel",
                            )
        account_text = ttk.Label(information_frame,
                            text=self.account_str,
                            style="OfferSelectionText.TLabel",
                            )
        
        driver_name_label.grid(column=0, row=0, sticky="W")
        driver_name_text.grid(column=1, row=0, sticky="W")
        
        account_label.grid(column=0, row=1, sticky="W")
        account_text.grid(column=1, row=1, sticky="W")
        
        expire_label = ttk.Label(timer_frame,
                            text= "Expires in: ",
                            style="OfferSelectionText.TLabel",
                            )

        
        time_label = ttk.Label(timer_frame,
                            textvariable=self.expiration_time_s,
                            style="OfferSelectionText.TLabel",
                            )
        time_label.after(1000, update_timer)
        units_label =  ttk.Label(timer_frame,
                            text= " seconds",
                            style="OfferSelectionText.TLabel",
                            )
        
        expire_label.grid(row=0, column=0, sticky="W")
        time_label.grid(row=0, column=1, sticky="W")
        units_label.grid(row=0, column=2, sticky="W")

        accept_button = ttk.Button(
            buttons_frame,
            text="Accept",
            command=callback_accept_offer,
            style="OfferSelectionButton.TButton",
            width=10,
            cursor="hand2"
        )
        cancel_button = ttk.Button(
            buttons_frame,
            text="Cancel",
            command=callback_cancel_offer,
            style="OfferSelectionButton.TButton",
            width=10,
            cursor="hand2"
        )
        dismiss_button = ttk.Button(
            buttons_frame,
            text="Dismiss",
            command=callback_dismiss_offer,
            style="OfferSelectionButton.TButton",
            width=10,
            cursor="hand2"
        )
        
        accept_button.grid(column=0, row=0, sticky="W", padx=(0, 20))
        cancel_button.grid(column=1, row=0, sticky="W", padx=(0, 20))
        dismiss_button.grid(column=2, row=0, sticky="W", padx=(0, 20))
        
        title_frame.grid(row=0, column=0, padx=(20, 0), pady=(20, 20))
        information_frame.grid(row=1, column=0, padx=(10,0), pady=(0, 20))
        timer_frame.grid(row=2, column=0, padx=(30,0), pady=(0, 30))
        buttons_frame.grid(row=3, column=0, padx=(40,0), pady=(0, 20))       
    
    def clear_row(self):
        self.driver_str.set("")
        self.start_travel_time_str.set("")
        self.destination_str.set("")
        self.number_of_seats_str.set("")
        self.cost_eth_str.set("")
        self.cost_eth = 0
        self.checkbox.grid_remove()
        if(self.active):
            self.checkbox.grid_remove()
            self.active = False
class Offers(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style, width=50, height=75)

        """ ATTRIBUTES """
        self.controller = controller

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        title_frame = ttk.Frame(
            self,
            style="OffersFrame.TFrame"
        )
        
        offers_label = ttk.Label(
            title_frame,
            text="Rideshare Offers",
            style="OffersTitle2.TLabel"
        )
        offers_label.grid(row=0, column=0, sticky="EW")
        
        title_frame.grid(row=0, column=0, columnspan=7, sticky="EW",
                          padx=(200, 0), pady=(5, 0))

        """ SECOND ROW """
        car_img = ImageTk.PhotoImage(Image.open(self.controller.CAR_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        car_panel = ttk.Label(self, image=car_img, style="OffersLabel.TLabel")
        car_panel.image = car_img

        clock_img = ImageTk.PhotoImage(Image.open(self.controller.CLOCK_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        clock_panel = ttk.Label(self, image=clock_img,
                                style="OffersLabel.TLabel")
        clock_panel.image = clock_img

        placeholder_img = ImageTk.PhotoImage(Image.open(self.controller.PLACEHOLDER_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        placeholder_panel = ttk.Label(
            self, image=placeholder_img, style="OffersLabel.TLabel")
        placeholder_panel.image = placeholder_img

        seats_img = ImageTk.PhotoImage(Image.open(self.controller.SEATS_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        seats_panel = ttk.Label(self, image=seats_img,
                                style="OffersLabel.TLabel")
        seats_panel.image = seats_img

        money_img = ImageTk.PhotoImage(Image.open(self.controller.MONEY_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        money_panel = ttk.Label(self, image=money_img,
                                style="OffersLabel.TLabel")
        money_panel.image = money_img
        

        car_panel.grid(row=1, column=1, sticky="NS", pady=(5, 0))
        clock_panel.grid(row=1, column=2, sticky="NS", pady=(5, 0))
        placeholder_panel.grid(row=1, column=3, sticky="NS", pady=(5, 0))
        seats_panel.grid(row=1, column=4, sticky="NS", pady=(5, 0))
        money_panel.grid(row=1, column=5, sticky="NS", pady=(5, 0))
        
        """ THIRD ROW """
        selection_label = ttk.Label(
            self,
            text="Your selection",
            style="OffersNormalText.TLabel",
            padding=(5, 5, 0, 0)

        )

        driver_label = ttk.Label(
            self,
            text="Driver",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        start_travel_time_label = ttk.Label(
            self,
            text="Time",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        destination_label = ttk.Label(
            self,
            text="Destination",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        seats_number_label = ttk.Label(
            self,
            text="# of seats",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        cost_eth_label = ttk.Label(
            self,
            text="Cost Eth",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        
        
        selection_label.config(anchor=CENTER)
        driver_label.config(anchor=CENTER)
        start_travel_time_label.config(anchor=CENTER)
        destination_label.config(anchor=CENTER)
        seats_number_label.config(anchor=CENTER)
        cost_eth_label.config(anchor=CENTER)

        table_separator = ttk.Separator(self)

        selection_label.grid(row=2, column=0, sticky="EW", padx=(10, 0))
        driver_label.grid(row=2, column=1, sticky="EW")
        start_travel_time_label.grid(row=2, column=2, sticky="EW")
        destination_label.grid(row=2, column=3, sticky="EW")
        seats_number_label.grid(row=2, column=4, sticky="EW")
        cost_eth_label.grid(row=2, column=5, sticky="EW")
        
        table_separator.grid(row=3, columnspan=7, padx=(10, 5), sticky="EW")

        """ FOURTH ROW """
        self.fourth_row = OfferRow(self, index=0)

        self.fourth_row.driver_label.grid(row=4, column=1)
        self.fourth_row.start_travel_time_label.grid(row=4, column=2)
        self.fourth_row.destination_label.grid(row=4, column=3)
        self.fourth_row.seats_label.grid(row=4, column=4)
        self.fourth_row.cost_label.grid(row=4, column=5)

        """ FIFTH ROW """
        self.fifth_row = OfferRow(self, index=1)
    
        self.fifth_row.driver_label.grid(row=5, column=1)
        self.fifth_row.start_travel_time_label.grid(row=5, column=2)
        self.fifth_row.destination_label.grid(row=5, column=3)
        self.fifth_row.seats_label.grid(row=5, column=4)
        self.fifth_row.cost_label.grid(row=5, column=5)

        """ SIXTH ROW """
        self.sixth_row = OfferRow(self, index=2)

        self.sixth_row.driver_label.grid(row=6, column=1)
        self.sixth_row.start_travel_time_label.grid(row=6, column=2)
        self.sixth_row.destination_label.grid(row=6, column=3)
        self.sixth_row.seats_label.grid(row=6, column=4)
        self.sixth_row.cost_label.grid(row=6, column=5)

        """ SEVENTH ROW """
        self.seventh_row = OfferRow(self, index=3)
 
        self.seventh_row.driver_label.grid(row=7, column=1)
        self.seventh_row.start_travel_time_label.grid(row=7, column=2)
        self.seventh_row.destination_label.grid(row=7, column=3)
        self.seventh_row.seats_label.grid(row=7, column=4)
        self.seventh_row.cost_label.grid(row=7, column=5)

        """ EIGTH ROW """
        self.eigth_row = OfferRow(self, index=4)

        self.eigth_row.driver_label.grid(row=8, column=1)
        self.eigth_row.start_travel_time_label.grid(row=8, column=2)
        self.eigth_row.destination_label.grid(row=8, column=3)
        self.eigth_row.seats_label.grid(row=8, column=4)
        self.eigth_row.cost_label.grid(row=8, column=5)

        """ NINTH ROW """
        self.ninth_row = OfferRow(self, index=5)

        self.ninth_row.driver_label.grid(row=9, column=1)
        self.ninth_row.start_travel_time_label.grid(row=9, column=2)
        self.ninth_row.destination_label.grid(row=9, column=3)
        self.ninth_row.seats_label.grid(row=9, column=4)
        self.ninth_row.cost_label.grid(row=9, column=5)

        self.rows = [
            self.fourth_row,
            self.fifth_row,
            self.sixth_row,
            self.seventh_row,
            self.eigth_row,
            self.ninth_row,
        ]
        
        self.update_offer_rows()

    def enable_checkbuttons(self):
        for row in self.rows:
            row.checkbox.config(state=NORMAL)
                
    def disable_checkbuttons(self, enabled_checkbutton_index):
        for index, row in enumerate(self.rows):
            if(enabled_checkbutton_index != index):
                row.checkbox.config(state=DISABLED)

    def clear_rows(self):
        for row in self.rows:
            row.clear_row()

    def update_offer_rows(self):

        self.clear_rows()
        if not settings.g_rideshare_offers:
            return
        
        for index, smart_contract in enumerate(settings.g_rideshare_offers):
            current_row = self.rows[index] 
            current_row.driver_str.set(smart_contract.driver)
            current_row.destination_str.set(smart_contract.destination)
            current_row.start_travel_time_str.set(smart_contract.start_travel_time)
            current_row.number_of_seats_str.set(smart_contract.number_of_seats)
            current_row.cost_eth_str.set(smart_contract.cost_eth)
            current_row.cost_eth = smart_contract.cost_eth
            current_row.expiration_time_s.set(smart_contract.expiration_time_s)
            if(settings.g_driver_dictionary.get(smart_contract.driver)):
                current_row.account_str = settings.g_driver_dictionary[smart_contract.driver].account.id
            else:
                current_row.account_str = "0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            current_row.smart_contract_bytecode = smart_contract.bytecode
            current_row.smart_contract_abi = smart_contract.abi
            current_row.active = True
            current_row.checkbox.grid(row=index + 4, column=0) # Offset por posicion inicials

    def delete_offer(self, deleted_driver_index, offer_was_accepted=True, transaction_receipt=""):
        self.clear_rows()
        if not settings.g_rideshare_offers:
            return
        
        selected_offer = settings.g_rideshare_offers.pop(deleted_driver_index)
        selected_offer.selected = True
        
        if offer_was_accepted:
            selected_offer.transaction_receipt = transaction_receipt            
            settings.g_rideshare_future_travels.append(selected_offer)
            self.controller.future_travels_frame.update_rideshare_future_travels_rows()
        

        for index, smart_contract in enumerate(settings.g_rideshare_offers):
            current_row = self.rows[index] 
            current_row.driver_str.set(smart_contract.driver)
            current_row.start_travel_time_str.set(smart_contract.start_travel_time)
            current_row.destination_str.set(smart_contract.destination)
            current_row.number_of_seats_str.set(smart_contract.number_of_seats)
            current_row.cost_eth_str.set(smart_contract.cost_eth)
            current_row.cost_eth = smart_contract.cost_eth
            current_row.expiration_time_s.set(smart_contract.expiration_time_s)
            if(settings.g_driver_dictionary.get(smart_contract.driver)):
                current_row.account_str = settings.g_driver_dictionary[smart_contract.driver].account.id
            else:
                current_row.account_str = "0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            current_row.smart_contract_bytecode = smart_contract.bytecode
            current_row.smart_contract_abi = smart_contract.abi
            current_row.active = True
            current_row.checkbox.grid(row=index + 4, column=0) # Offset por posicion inicials