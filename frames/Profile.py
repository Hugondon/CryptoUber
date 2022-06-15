import tkinter as tk


from tkinter import VERTICAL, ttk, Toplevel
from frames.const import *
from PIL import ImageTk, Image
import settings
from solcx import compile_source
from utils.SmartContract import SmartContract
class Profile(ttk.Frame):

    IMAGE_JPG_PATH = "imgs/hugo.jpg"
    
    JPG_WIDTH, JPG_HEIGHT = 704, 938
    JPG_RESIZE_REFACTOR = 4
    
    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style)

        self.controller = controller

        """ ATTRIBUTES """

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        profile_frame = ttk.Frame(
            self,
            style="ProfileFrame.TFrame"
        )
        profile_label = ttk.Label(
            profile_frame,
            text="Details",
            style="ProfileTitle2.TLabel",
        )

        profile_label.grid(row=0, column=0, sticky="EW")
        profile_frame.grid(row=0,column=0, sticky="EW", padx=(150+0.35*self.JPG_WIDTH//self.JPG_RESIZE_REFACTOR, 0), pady=(5, 10))
        """ SECOND ROW """
        hugo_img = ImageTk.PhotoImage(Image.open(self.IMAGE_JPG_PATH).resize(
            (self.JPG_WIDTH//self.JPG_RESIZE_REFACTOR, self.JPG_HEIGHT//self.JPG_RESIZE_REFACTOR)))
        img_panel = ttk.Label(self, image=hugo_img, style="OffersLabel.TLabel")
        img_panel.image = hugo_img
        img_panel.grid(row=1, column=0, sticky="WN", padx=(150,0),pady=(0, 10))
        

        """ THIRD ROW """
        
        information_frame = ttk.Frame(
            self,
            style="ProfileFrame.TFrame"
        )
        
        name_label = ttk.Label(
            information_frame,
            text="Name",
            style="ProfileInformation.TLabel"
        )
        id_label = ttk.Label(
            information_frame,
            text="Account ID",
            style="ProfileInformation.TLabel"
        )
        balance_label = ttk.Label(
            information_frame,
            text="Account Balance",
            style="ProfileInformation.TLabel"
        )

        name_text = ttk.Label(
            information_frame,
            textvariable=self.controller.username,
            style="ProfileInformation.TLabel"
        )
        id_text = ttk.Label(
            information_frame,
            textvariable=self.controller.current_user.account.id,
            style="ProfileInformation.TLabel"
        )
        balance_text = ttk.Label(
            information_frame,
            textvariable=self.controller.account_balance,
            style="ProfileInformation.TLabel"
        )
        
        name_label.grid(row=0, column=0, sticky="EW")
        id_label.grid(row=1, column=0, sticky="EW")
        balance_label.grid(row=2, column=0, sticky="EW")
        
        name_text.grid(row=0, column=1, sticky="EW")
        id_text.grid(row=1, column=1, sticky="EW")
        balance_text.grid(row=2, column=1, sticky="EW")       
        
        information_frame.grid(row=2, column=0, sticky="EW", padx=(20, 0))
        
        """ FOURTH ROW """
        buttons_frame = ttk.Frame(
            self,
            style="ProfileFrame.TFrame"
        )
        
        add_offer_button = ttk.Button(
            buttons_frame,
            text="Add Offer",
            command=self.callback_add_offer,
            style="ProfileInformationButton.TButton",
            width=15,
            cursor="hand2"
        )
        edit_profile_button = ttk.Button(
            buttons_frame,
            text="Edit Profile",
            command=self.callback_edit_profile,
            style="ProfileInformationButton.TButton",
            width=15,
            cursor="hand2"
        )
        
        add_offer_button.grid(row=0, column=0, sticky="S", pady=(0,25))
        edit_profile_button.grid(row=1, column=0, sticky="S", pady=(0,25))
        
        buttons_frame.grid(row=3, column=0, sticky="EW", padx=(120+0.35*self.JPG_WIDTH//self.JPG_RESIZE_REFACTOR, 0), pady=(50, 10))  


    def callback_accept_contract(self):
  
        new_smart_contract = SmartContract(
            driver=self.driver_name.get(),
            destination=self.destination_name.get(),
            start_travel_time=f"{self.start_travel_hour.get()}:{self.start_travel_minute.get()}",
            number_of_seats=self.max_num_of_passengers.get(),
            duration=self.travel_time_value.get(),
            cost_eth=self.price_eth.get(),
            expiration_time_s=self.expiration_time_s.get()
        )
        settings.g_rideshare_offers.append(new_smart_contract)
        
        self.controller.rideshare_offer_frame.update_offer_rows()
        self.offer_window.destroy()
    
    def callback_add_offer(self):
        
        WIDTH, HEIGHT = 512,520
        self.offer_window= Toplevel(self, bg=COLOR_NEW_OFFER_BACKGROUND)
        
        self.offer_window.title("New Offer")
        self.offer_window.geometry(f"{WIDTH}x{HEIGHT}")
        self.offer_window.iconbitmap(self.controller.ICON_ICO_PATH)
        
        container = ttk.Frame(self.offer_window, style="NewOfferFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        
        
        """ ATTRIBUTES """
        self.driver_name = tk.StringVar()
        self.destination_name = tk.StringVar()
        
        self.travel_time_value = tk.IntVar(value=20)
        self.start_travel_hour = tk.IntVar(value=14)
        self.start_travel_minute = tk.IntVar(value=30)
        
        self.eta_minutes = tk.IntVar(value=6)
        
        self.max_num_of_passengers = tk.IntVar(value=2)
        
        self.price_eth = tk.DoubleVar(value=1)
        self.expiration_time_s = tk.IntVar(value=10)
        
        """ LAYOUT """
        title_frame = ttk.Frame(
            container,
            style="NewOfferFrame.TFrame"
        )

        title_label = ttk.Label(title_frame,
                            text= "New Offer!",
                            style="NewOfferTitle2.TLabel",
                            )
        title_label.grid(column=0, row=0, sticky="W") # Para evitar que color de fondo se vaya a la derecha
    
        driver_name_label = ttk.Label(container,
                            text= "Driver Name",
                            style="NewOfferTitle3.TLabel",
                            )
    

        destination_label = ttk.Label(container,
                            text= "Destination",
                            style="NewOfferTitle3.TLabel",
                            )
    

        travel_time_label = ttk.Label(container,
                            text= "Expected Travel Time [minutes]",
                            style="NewOfferTitle3.TLabel",
                            )
    
        
        start_time_label = ttk.Label(container,
                            text= "Start Travel Time [hh:mm] ",
                            style="NewOfferTitle3.TLabel",
                            )

        eta_label = ttk.Label(container,
                            text= "ETA [minutes] ",
                            style="NewOfferTitle3.TLabel",
                            )
    
    

        max_num_of_passengers_label = ttk.Label(container,
                            text= "Max # of Passengers ",
                            style="NewOfferTitle3.TLabel",
                            )
    

        price_label = ttk.Label(container,
                            text= "Price [Eth]",
                            style="NewOfferTitle3.TLabel",
                            )
        
        contract_expiration_time_label = ttk.Label(container,
                            text= "Expiration Time [s]: ",
                            style="NewOfferTitle3.TLabel",
                            )
        
        buttons_frame = ttk.Frame(
            container,
            style="NewOfferFrame.TFrame"
        )
        
        accept_button = ttk.Button(
            buttons_frame,
            text="Accept",
            command=self.callback_accept_contract,
            style="NewOfferButton.TButton",
            width=15,
            cursor="hand2"
        )

        accept_button.grid(column=0, row=0, sticky="W")
    
        title_frame.grid(row=0, column=0, columnspan=3, sticky="WE", padx=(70, 0), pady=(25, 0))
        driver_name_label.grid(row=1, column=0, sticky="WE", padx=(50, 0), pady=(25, 20))
        destination_label.grid(row=2, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        travel_time_label.grid(row=3, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        start_time_label.grid(row=4, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        eta_label.grid(row=5, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        max_num_of_passengers_label.grid(row=6, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        price_label.grid(row=7, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        contract_expiration_time_label.grid(row=8, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        buttons_frame.grid(row=9, columnspan=3, padx=(200,0),pady=(0,20), sticky="W")
        
        vertical_separator = ttk.Separator(container,orient=VERTICAL)
        
        vertical_separator.grid(column=1, row=1, rowspan=8, sticky="NSW", padx=(20,20), pady=(0, 20))
        
        driver_name_input = ttk.Combobox(
            container, width=25, textvariable=self.driver_name
        )
        driver_name_input["values"] = ("David", "Alex", "Luis", "Andy")
        
        
        destination_input = ttk.Entry(
            container, width=25, textvariable=self.destination_name
        )
        
        travel_time_spinbox = tk.Spinbox(
            container,
            width=23,
            from_=0,
            to=50,
            values=(0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50),
            textvariable=self.travel_time_value,
            wrap=True
        )
        start_travel_frame = ttk.Frame(
            container,
            style="NewOfferFrame.TFrame"
        )
        start_travel_hour_spinbox = tk.Spinbox(
            start_travel_frame,
            width=9,
            from_=0,
            to=23,
            textvariable=self.start_travel_hour,
            wrap=True
        )
        
        travel_label = ttk.Label(
            start_travel_frame,
            text=" : ",
            style="NewOfferText.TLabel"
        )
        
        start_travel_minute_spinbox = tk.Spinbox(
            start_travel_frame,
            width=9,
            from_=0,
            to=59,
            textvariable=self.start_travel_minute,
            wrap=True
        )
        start_travel_hour_spinbox.grid(column=0, row=0, sticky="W")
        travel_label.grid(column=1, row=0, sticky="EW")
        start_travel_minute_spinbox.grid(column=2, row=0, sticky="W")
        
        eta_scale = tk.Scale(
            container,
            length=150,
            tickinterval=5,
            bg=COLOR_NEW_OFFER_BACKGROUND,
            troughcolor=COLOR_NEW_OFFER_BACKGROUND,
            orient="horizontal",
            from_=0,
            to=25,
            variable=self.eta_minutes,
        )
        
        max_num_of_passengers_spinbox = tk.Spinbox(
            container,
            width=24,
            from_=0,
            to=4,
            textvariable=self.max_num_of_passengers,
            wrap=True
        )
        
        price_spinbox = tk.Spinbox(
            container,
            width=24,
            format="%.6f",
            increment=0.01,
            from_=0,
            to=10,
            textvariable=self.price_eth,
            wrap=True
        )
        
        contract_expiration_time_spinbox = tk.Spinbox(
            container,
            width=24,
            from_=0,
            to=15,
            textvariable=self.expiration_time_s,
            wrap=True
        )
        
        
        driver_name_input.grid(column=2, row=1, padx=(0, 0), pady=(25,20), sticky="NW")
        destination_input.grid(column=2, row=2, pady=(0,20), sticky="NW")
        travel_time_spinbox.grid(column=2, row=3, pady=(0,20), sticky="W")
        start_travel_frame.grid(column=2, row=4, pady=(0,20), sticky="W")
        eta_scale.grid(column=2, row=5, pady=(0,20), sticky="W")
        max_num_of_passengers_spinbox.grid(column=2, row=6, pady=(0,20), sticky="W")
        price_spinbox.grid(column=2, row=7, pady=(0,20), sticky="W")
        contract_expiration_time_spinbox.grid(column=2, row=8, pady=(0,20), sticky="W")
            
    def callback_edit_profile(self):
        
        
        def callback_accept_profile_changes():
            profile_window.destroy()
            
        WIDTH, HEIGHT = 335, 260
        
        profile_window= Toplevel(self)
        
        profile_window.title("Profile Settings")
        profile_window.geometry(f"{WIDTH}x{HEIGHT}")
        profile_window.iconbitmap(self.controller.ICON_ICO_PATH)
        
        container = ttk.Frame(profile_window, style="NewOfferFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        
        title_frame = ttk.Frame(
            container,
            style="NewOfferFrame.TFrame"
        )
        
        title_label = ttk.Label(title_frame,
                            text= "Edit Your Profile!",
                            style="NewOfferTitle2.TLabel",
                            )
        title_label.grid(column=0, row=0, sticky="W") # Para evitar que color de fondo se vaya a la derecha
        
        
        user_name_label = ttk.Label(container,
                            text= "User Name",
                            style="NewOfferTitle3.TLabel",
                            )
    

        account_id_label = ttk.Label(container,
                            text= "Account ID",
                            style="NewOfferTitle3.TLabel",
                            )
    

        balance_label = ttk.Label(container,
                            text= "New Balance",
                            style="NewOfferTitle3.TLabel",
                            )
        
        
        buttons_frame = ttk.Frame(
            container,
            style="NewOfferFrame.TFrame"
        )
        
        accept_button = ttk.Button(
            buttons_frame,
            text="Accept",
            command=callback_accept_profile_changes,
            style="NewOfferButton.TButton",
            width=15,
            cursor="hand2"
        )
        accept_button.grid(column=0, row=0, sticky="W")
        
        title_frame.grid(row=0, column=0, columnspan=3, sticky="WE", padx=(80, 0), pady=(25, 20))
        user_name_label.grid(row=1, column=0, sticky="EW", padx=(30, 0), pady=(0, 20))
        account_id_label.grid(row=2, column=0, sticky="EW", padx=(30, 0), pady=(0, 20))
        balance_label.grid(row=3, column=0, sticky="EW", padx=(30, 0), pady=(0, 20))
        buttons_frame.grid(row=4, columnspan=3, padx=(90,0),pady=(0,20), sticky="W")
        
        vertical_separator = ttk.Separator(container,orient=VERTICAL)
        
        vertical_separator.grid(column=1, row=1, rowspan=3, sticky="NSW", padx=(20,20), pady=(0, 20))
        
        username_input = ttk.Entry(
            container, width=25, textvariable=self.controller.username
        )
        account_id_input = ttk.Entry(
            container, width=25, textvariable=self.controller.account_id
        )
        balance_spinbox = tk.Spinbox(
            container,
            width=24,
            format="%.4f",
            increment=0.01,
            from_=0,
            to=10,
            textvariable=self.controller.account_balance,
            wrap=True
        )
        
        username_input.grid(column=2, row=1, pady=(0,20), sticky="NW")
        account_id_input.grid(column=2, row=2, pady=(0,20), sticky="NW")
        balance_spinbox.grid(column=2, row=3, pady=(0,20), sticky="NW")
        