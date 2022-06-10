import tkinter as tk


from tkinter import VERTICAL, ttk, Toplevel
from frames.const import *
from PIL import ImageTk, Image
from solcx import compile_source
from utils import CryptoAccount, User
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
        current_user_account = CryptoAccount(
            id=tk.StringVar(value="0x077c6c3ca8F3bAf37159A5b198c69e5562574042"),
            balance_eth=tk.IntVar(value=100),
            public_key=tk.StringVar(value="14baa5d10aaa0bfc836a427595c82037e74c467823fd214f0d007be2786246a5")
        )
        
        self.current_user = User(
            name=tk.StringVar(value="Juanito"),
            account=current_user_account
        )
        
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
            textvariable=self.current_user.name,
            style="ProfileInformation.TLabel"
        )
        id_text = ttk.Label(
            information_frame,
            textvariable=self.current_user.account.id,
            style="ProfileInformation.TLabel"
        )
        balance_text = ttk.Label(
            information_frame,
            textvariable=self.current_user.account.balance_eth,
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
        update_balance_button = ttk.Button(
            buttons_frame,
            text="Update Balance",
            command=self.callback_updating_balance,
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
        update_balance_button.grid(row=1, column=0, sticky="S", pady=(0, 25))
        edit_profile_button.grid(row=2, column=0, sticky="S", pady=(0,25))
        
        buttons_frame.grid(row=3, column=0, sticky="EW", padx=(120+0.35*self.JPG_WIDTH//self.JPG_RESIZE_REFACTOR, 0), pady=(50, 10))  


    def callback_accept_contract(self):
        
        # print(f"Driver name: {self.driver_name.get()}")
        # print(f"Contract #: {self.contract_number.get()}")
        # print(f"Destination Name: {self.destination_name.get()}")
        # print(f"Expected Travel Time: {self.travel_time_value.get()}")
        # print(f"Start Travel Time: {self.start_travel_hour.get()}:{self.start_travel_minute.get()}")
        # print(f"ETA: {self.eta_minutes.get()}")
        # print(f"Max Number of Passengers: {self.max_num_of_passengers.get()}")
        # print(f"Price: {self.price_eth.get()}")
        
        source_code = f'''
        pragma solidity >0.5.0;

            contract Greeter {{
                string public driver;
                string public destination;
                string public startTravelTime;
                uint public duration;


                constructor() public {{
                    driver = "{self.driver_name.get()}";
                    destination = "{self.destination_name.get()}";
                    startTravelTime = "{self.start_travel_hour.get()}:{self.start_travel_minute.get()}";
                    duration = {self.travel_time_value.get()};
                }}

                function getDriver() view public returns (string memory) {{
                    return driver;
                }}
                function getDestination() view public returns (string memory) {{
                    return destination;
                }}
                function getStartTravelTime() view public returns (string memory) {{
                    return startTravelTime;
                }}
                function getDuration() view public returns (uint) {{
                    return duration;
                }}
                
        }}
        '''

        # Solidity source code
        compiled_solidity = compile_source(
            source_code,
            output_values=['abi', 'bin']
        )

        contract_id, contract_interface = compiled_solidity.popitem()
        bytecode, abi = contract_interface['bin'], contract_interface['abi']
        
        self.offer_window.destroy()
    
    def callback_add_offer(self):
        
        WIDTH, HEIGHT = 512,520
        self.offer_window= Toplevel(self, bg=COLOR_NEW_OFFER_BACKGROUND)
        
        self.offer_window.title("New Offer")
        self.offer_window.geometry(f"{WIDTH}x{HEIGHT}")
        self.offer_window.iconbitmap(self.controller.ICON_ICO_PATH)
        
        container = ttk.Frame(self.offer_window, style="NewOfferFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        # container.columnconfigure(0, minsize=WIDTH, weight=1) 
        # container.rowconfigure(0, minsize=HEIGHT, weight=1)
        
        
        """ ATTRIBUTES """
        self.driver_name = tk.StringVar()
        self.contract_number = tk.StringVar()
        self.destination_name = tk.StringVar()
        
        self.travel_time_value = tk.IntVar(value=20)
        self.start_travel_hour = tk.IntVar(value=14)
        self.start_travel_minute = tk.IntVar(value=30)
        
        self.eta_minutes = tk.IntVar(value=6)
        
        self.max_num_of_passengers = tk.IntVar(value=2)
        
        self.price_eth = tk.DoubleVar(value=1)
        
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
    

        contract_number_label = ttk.Label(container,
                            text= "Contract #",
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
        contract_number_label.grid(row=2, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        destination_label.grid(row=3, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        travel_time_label.grid(row=4, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        start_time_label.grid(row=5, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        eta_label.grid(row=6, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        max_num_of_passengers_label.grid(row=7, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        price_label.grid(row=8, column=0, sticky="WE", padx=(50, 0), pady=(0, 20))
        buttons_frame.grid(row=9, columnspan=3, padx=(200,0),pady=(0,20), sticky="W")
        
        vertical_separator = ttk.Separator(container,orient=VERTICAL)
        
        vertical_separator.grid(column=1, row=1, rowspan=8, sticky="NSW", padx=(20,20), pady=(0, 20))
        
        driver_name_input = ttk.Entry(
            container, width=25, textvariable=self.driver_name
        )
        contract_number_input = ttk.Entry(
            container, width=25, textvariable=self.contract_number
        )
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
        
        driver_name_input.grid(column=2, row=1, padx=(0, 0), pady=(25,20), sticky="NW")
        contract_number_input.grid(column=2, row=2, padx=(0, 0), pady=(0,20), sticky="NW")
        destination_input.grid(column=2, row=3, pady=(0,20), sticky="NW")
        travel_time_spinbox.grid(column=2, row=4, pady=(0,20), sticky="W")
        start_travel_frame.grid(column=2, row=5, pady=(0,20), sticky="W")
        eta_scale.grid(column=2, row=6, pady=(0,20), sticky="W")
        max_num_of_passengers_spinbox.grid(column=2, row=7, pady=(0,20), sticky="W")
        price_spinbox.grid(column=2, row=8, pady=(0,20), sticky="W")
        
    
    
    def callback_updating_balance(self):
        if(self.current_user.withdraw_from_account(amount=100)):
            print("VALID")
        else:
            print("NOT VALID")
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