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
        style.configure(
            "TextTitle.TLabel",
            background=COLOR_APP_BACKGROUND,
            foreground=COLOR_TITLE_TEXT,
            font=("Segoe UI", 28, "italic")
        )
        style.configure(
            "TextOffersSubtitle.TLabel",
            background=COLOR_OFFERS_BACKGROUND,
            foreground=COLOR_SUBTITLE_TEXT,
            font=("Segoe UI", 14)
        )
        style.configure(
            "TextTravelsSubtitle.TLabel",
            background=COLOR_FUTURE_TRAVELS_BACKGROUND,
            foreground=COLOR_SUBTITLE_TEXT,
            font=("Segoe UI", 14)
        )
        style.configure(
            "ProfileSubtitle.TLabel",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_TITLE_TEXT,
            font=("Segoe UI", 14)
        )
        style.configure(
            "ProfileInformation.TLabel",
            background=COLOR_PROFILE_BACKGROUND,
            foreground=COLOR_SUBTITLE_TEXT,
            font=("Segoe UI", 12)
        )
        style.configure(
            "NormalOffersText.TLabel",
            background=COLOR_OFFERS_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            font=("Segoe UI", 8)
        )
        style.configure(
            "NormalTravelsText.TLabel",
            background=COLOR_FUTURE_TRAVELS_BACKGROUND,
            foreground=COLOR_NORMAL_TEXT,
            font=("Segoe UI", 8)
        )

        style.configure("AppFrame.TFrame",
                        background=COLOR_APP_BACKGROUND)
        style.configure("OffersFrame.TFrame",
                        bordercolor="red",
                        background=COLOR_OFFERS_BACKGROUND)
        style.configure("TravelsFrame.TFrame",
                        background=COLOR_FUTURE_TRAVELS_BACKGROUND)
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
        container.columnconfigure(0, minsize=500, weight=1)
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
