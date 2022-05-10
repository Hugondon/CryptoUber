import tkinter as tk


from tkinter import ttk
from frames.const import *


class FutureTravels(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style)

        self.controller = controller

        """ ATTRIBUTES """

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        future_travels_label = ttk.Label(
            self,
            text="My Future Travels",
            style="TextTravelsSubtitle.TLabel"
        )

        future_travels_label.grid(row=0, column=0, sticky="EW",
                                  padx=(200, 0), pady=(5, 20))

        """ SECOND ROW """
        # imgs

        """ THIRD ROW """

        """ FOURTH ROW """
