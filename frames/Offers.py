import tkinter as tk


from tkinter import ttk
from frames.const import *


class Offers(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style, width=50, height=75)

        self.controller = controller

        """ ATTRIBUTES """

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        offers_label = ttk.Label(
            self,
            text="Rideshare offers",
            style="TextOffersSubtitle.TLabel"
        )

        offers_label.grid(row=0, column=0, sticky="EW",
                          padx=(200, 0), pady=(5, 20))

        """ SECOND ROW """
        # imgs
        """ THIRD ROW """
        selection_label = ttk.Label(
            self,
            text="Your selection",
            style="NormalOffersText.TLabel"
        )

        driver_label = ttk.Label(
            self,
            text="Driver",
            style="TextOffersSubtitle.TLabel"
        )
        date_time_label = ttk.Label(
            self,
            text="Date & Time",
            style="TextOffersSubtitle.TLabel"
        )

        selection_label.grid(row=2, column=0, sticky="EW",
                             padx=(10, 0))
        driver_label.grid(row=2, column=1, sticky="EW")

        """ FOURTH ROW """
