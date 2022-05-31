import settings
import tkinter as tk

from tkinter import CENTER, ttk

from frames import Offers, Profile, FutureTravels
from frames.const import *


class RideSharing(tk.Tk):

    WIDTH, HEIGHT = 700,640
    
    CAR_PNG_PATH = "imgs/car.png"
    CLOCK_PNG_PATH = "imgs/clock.png"
    MONEY_PNG_PATH = "imgs/money.png"
    PLACEHOLDER_PNG_PATH = "imgs/placeholder.png"
    SEATS_PNG_PATH = "imgs/seats.png"
    ICON_ICO_PATH = "imgs/R.ico"

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
            background=COLOR_PROFILE_TITLE_BACKGROUND,
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

        """ Attributes  """

        self.title("Ridesharing App")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self["background"] = COLOR_APP_BACKGROUND
        self.iconbitmap(self.ICON_ICO_PATH)
        """ LAYOUT CONFIGURATION """
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self, style="AppFrame.TFrame")
        container.grid(row=0, column=0, sticky="NSEW")
        container.columnconfigure(0, minsize=550, weight=1)
        container.columnconfigure(1, minsize=200, weight=1)

        container.rowconfigure(1, minsize=300, weight=1)
        container.rowconfigure(2, minsize=300, weight=1)
        ridesharing_title_label = ttk.Label(
            container,
            text="Ridesharing",
            style="TextTitle.TLabel",
        )

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


app = RideSharing()
app.mainloop()
