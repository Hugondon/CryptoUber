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
            text="Rideshare Offers",
            style="OffersTitle2.TLabel"
        )

        offers_label.grid(row=0, column=0, columnspan=6, sticky="EW",
                          padx=(200, 200), pady=(5, 0))

        """ SECOND ROW """
        # imgs
        """ THIRD ROW """
        selection_label = ttk.Label(
            self,
            text="Your selection",
            style="OffersNormalText.TLabel",
            padding=(5, 10, 0, 0)

        )

        driver_label = ttk.Label(
            self,
            text="Driver",
            style="OffersTitle3.TLabel",
            padding=(10, 10, 5, 0)
        )
        date_time_label = ttk.Label(
            self,
            text="Date & Time",
            style="OffersTitle3.TLabel",
            padding=(10, 10, 5, 0)
        )
        destination_label = ttk.Label(
            self,
            text="Destination",
            style="OffersTitle3.TLabel",
            padding=(10, 10, 5, 0)
        )
        seats_number_label = ttk.Label(
            self,
            text="# of seats",
            style="OffersTitle3.TLabel",
            padding=(10, 10, 5, 0)
        )
        cost_MXN_label = ttk.Label(
            self,
            text="Cost MXN",
            style="OffersTitle3.TLabel",
            padding=(10, 10, 5, 0)
        )

        table_separator = ttk.Separator(self)

        selection_label.grid(row=2, column=0, sticky="EW",
                             padx=(10, 0))
        driver_label.grid(row=2, column=1, sticky="EW")
        date_time_label.grid(row=2, column=2, sticky="EW")
        destination_label.grid(row=2, column=3, sticky="EW")
        seats_number_label.grid(row=2, column=4, sticky="EW")
        cost_MXN_label.grid(row=2, column=5, sticky="EW")
        table_separator.grid(row=3, columnspan=6, padx=(10, 5), sticky="EW")

        """ FOURTH ROW """
