import settings
import tkinter as tk
import os

from tkinter import CENTER, ttk, Menu

from frames import Offers, Profile, FutureTravels
from frames.const import *
from web3 import Web3


class RideSharing(tk.Tk):

    WIDTH, HEIGHT = 1030,700
    
    COLUMN_1_WIDTH = 500
    COLUMN_2_WIDTH = WIDTH - COLUMN_1_WIDTH
    
    ROW_1_HEIGHT = 300
    ROW_2_HEIGHT = HEIGHT - ROW_1_HEIGHT
    
    README_PATH = 'README.md'
    CAR_PNG_PATH = "imgs/car.png"
    CLOCK_PNG_PATH = "imgs/clock.png"
    MONEY_PNG_PATH = "imgs/money.png"
    PLACEHOLDER_PNG_PATH = "imgs/placeholder.png"
    SEATS_PNG_PATH = "imgs/seats.png"
    
    ICON_ICO_PATH = "imgs/R.ico"

    GANACHE_URL = "http://127.0.0.1:7545"

    PNG_WIDTH, PNG_HEIGHT = 512, 512
    PNG_RESIZE_FACTOR = 26
    

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """ Styles """
        style = ttk.Style(self)
        style.theme_use("clam")

        """ Rideshare App  Styles """

        style.configure(
            "TextTitle.TLabel",
            background=COLOR_APP_BACKGROUND,
            foreground=COLOR_TITLE_1_TEXT,
            font=("Segoe UI", 28, "italic")
        )
        
        style.configure("AppFrame.TFrame",
                        background=COLOR_APP_BACKGROUND)
        style.configure("ProfileFrame.TFrame",
                        background=COLOR_PROFILE_BACKGROUND)
        style.configure("OfferFrame.TFrame",
                        background=COLOR_OFFERS_BACKGROUND)
        style.configure("NewOfferFrame.TFrame",
                        background=COLOR_NEW_OFFER_BACKGROUND)
        style.configure("OfferSelectionFrame.TFrame",
                        background=COLOR_OFFER_SELECTION_BACKGROUND)

        """ Rideshare Offers Frame Styles """
        style.configure(
            "OffersTitle2.TLabel",
            background=COLOR_OFFERS_TITLE_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 14)
        )
        style.configure(
            "OffersTitle3.TLabel",
            background=COLOR_OFFERS_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 10)
        )
        style.configure(
            "OffersNormalText.TLabel",
            background=COLOR_OFFERS_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            font=("Segoe UI", 8)
        )
        style.configure(
            "OffersCheckButton.TCheckbutton",
            background=COLOR_OFFERS_BACKGROUND,
        )
        style.configure("OffersLabel.TLabel",
                        background=COLOR_OFFERS_BACKGROUND)
        style.configure("OffersFrame.TFrame",
                        background=COLOR_OFFERS_BACKGROUND)

        """ Future Travels Frame Styles """
        style.configure(
            "TravelsTitle2.TLabel",
            background=COLOR_FUTURE_TRAVELS_TITLE_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 14)
        )
        style.configure(
            "TravelsTitle3.TLabel",
            background=COLOR_FUTURE_TRAVELS_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 10)
        )
        style.configure(
            "TravelsNormalText.TLabel",
            background=COLOR_FUTURE_TRAVELS_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            font=("Segoe UI", 8)
        )
        style.configure(
            "TravelsCheckButton.TCheckbutton",
            background=COLOR_FUTURE_TRAVELS_BACKGROUND,
        )
        style.configure("TravelsLabel.TLabel",
                        background=COLOR_FUTURE_TRAVELS_BACKGROUND)
        style.configure("TravelsFrame.TFrame",
                        background=COLOR_FUTURE_TRAVELS_BACKGROUND)

        """ Profile Frame Styles """
        style.configure(
            "ProfileTitle2.TLabel",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_TITLE_1_TEXT,
            font=("Segoe UI", 14)
        )
        style.configure(
            "ProfileInformation.TLabel",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 12)
        )
        style.configure("ProfileFrame.TFrame",
                        background=COLOR_PROFILE_BACKGROUND)


        style.configure(
            "ProfileInformationButton.TButton",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            relief="raised",
            font=("Segoe UI", 10),
        )

        """ New Offer Frame Styles """
        style.configure(
            "NewOfferTitle2.TLabel",
            background=COLOR_NEW_OFFER_TITLE_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 16)
        )
        style.configure(
            "NewOfferTitle3.TLabel",
            background=COLOR_NEW_OFFER_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 12, 'bold')
        )

        style.configure(
            "NewOfferText.TLabel",
            background=COLOR_NEW_OFFER_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            font=("Segoe UI", 12)
        )
        
        style.configure(
            "NewOfferButton.TButton",
            background=COLOR_NEW_OFFER_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            relief="raised",
            font=("Segoe UI", 10),
        )

        """ Offer Selection Frame Styles """
        style.configure(
            "OfferSelectionTitle2.TLabel",
            background=COLOR_OFFER_SELECTION_BACKGROUND,
            foreground=OFFER_SELECTION_COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 16, 'bold')
        )
        style.configure(
            "OfferSelectionTitle3.TLabel",
            background=COLOR_OFFER_SELECTION_BACKGROUND,
            foreground=OFFER_SELECTION_COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 12, 'bold')
        )

        style.configure(
            "OfferSelectionText.TLabel",
            background=COLOR_OFFER_SELECTION_BACKGROUND,
            foreground=OFFER_SELECTION_COLOR_NORMAL_TEXT,
            font=("Segoe UI", 12)
        )
        
        style.configure(
            "OfferSelectionButton.TButton",
            background=COLOR_OFFER_SELECTION_BUTTON_BACKGROUND,
            foreground=OFFER_SELECTION_COLOR_NORMAL_TEXT,
            relief="raised",
            font=("Segoe UI", 10),
        )

        
        
        """ Attributes  """

        self.title("Ridesharing App")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self["background"] = COLOR_APP_BACKGROUND
        self.iconbitmap(self.ICON_ICO_PATH)
        
        
        """ Ganache """
        self.web3 = Web3(Web3.HTTPProvider(self.GANACHE_URL))
        self.web3.eth.defaultAccount=self.web3.eth.accounts[0]
        
        
        """ LAYOUT CONFIGURATION """
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self, style="AppFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        container.columnconfigure(0, minsize=self.COLUMN_1_WIDTH, weight=1)
        container.columnconfigure(1, minsize=self.COLUMN_2_WIDTH, weight=1)

        container.rowconfigure(1, minsize=self.ROW_1_HEIGHT, weight=1)
        container.rowconfigure(2, minsize=self.ROW_2_HEIGHT, weight=1)
        ridesharing_title_label = ttk.Label(
            container,
            text="Ridesharing",
            style="TextTitle.TLabel",
        )

        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        
        file = Menu(menu_bar, tearoff=0)
        file.add_command(label='Exit', command=self.quit)
        
        help = Menu(menu_bar, tearoff=0)
        help.add_command(label='README', command=self.open_readme)
    
        menu_bar.add_cascade(label="File", menu=file)
        menu_bar.add_cascade(label="Help", menu=help)

        self.rideshare_offer_frame = Offers(
            container, self, style="OffersFrame.TFrame")

        self.future_travels_frame = FutureTravels(
            container, self, style="TravelsFrame.TFrame"
        )

        self.profile_frame = Profile(
            container, self, style="ProfileFrame.TFrame"
        )

        ridesharing_title_label.grid(row=0, column=0, sticky="EW",
                                     padx=(175, 0))
        self.rideshare_offer_frame.grid(
            row=1, column=0, sticky="NESW")
        self.future_travels_frame.grid(
            row=2, column=0, sticky="NESW")
        self.profile_frame.grid(
            row=0, column=1, rowspan=3, sticky="NESW"
        )

    def open_readme(self):
        os.startfile(self.README_PATH)
app = RideSharing()
app.mainloop()
