import tkinter as tk

from tkinter import CENTER, ttk

from frames import Offers, Profile, FutureTravels
from frames.const import *


class RideSharing(tk.Tk):

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
        style.configure("TravelsFrame.TFrame",
                        background=COLOR_FUTURE_TRAVELS_BACKGROUND)

        """ Profile Frame Styles """
        style.configure(
            "ProfileTitle2.TLabel",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_TITLE_1_TEXT,
            font=("Segoe UI", 14, 'bold')
        )
        style.configure(
            "ProfileInformation.TLabel",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_TITLE_2_TEXT,
            font=("Segoe UI", 12)
        )
        style.configure("ProfileFrame.TFrame",
                        background=COLOR_PROFILE_BACKGROUND)

        """ Attributes  """

        self.title("Ridesharing App")
        self.geometry("700x640")
        self["background"] = COLOR_APP_BACKGROUND

        """ LAYOUT CONFIGURATION """
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self, style="AppFrame.TFrame")
        container.grid(row=0, column=0, sticky="NW")
        container.columnconfigure(0, minsize=550, weight=1)
        container.columnconfigure(1, minsize=200, weight=1)

        container.rowconfigure(1, minsize=300, weight=1)
        container.rowconfigure(2, minsize=300, weight=1)
        ridesharing_title_label = ttk.Label(
            container,
            text="Ridesharing",
            style="TextTitle.TLabel",
        )

        rideshare_offer_frame = Offers(
            container, self, style="OffersFrame.TFrame")

        future_travels_frame = FutureTravels(
            container, self, style="TravelsFrame.TFrame"
        )

        profile_frame = Profile(
            container, self, style="ProfileFrame.TFrame"
        )

        ridesharing_title_label.grid(row=0, column=0, sticky="EW",
                                     padx=(175, 0))
        rideshare_offer_frame.grid(
            row=1, column=0, sticky="NESW")
        future_travels_frame.grid(
            row=2, column=0, sticky="NESW")
        profile_frame.grid(
            row=0, column=1, rowspan=3, sticky="NESW"
        )


app = RideSharing()
app.mainloop()
