import tkinter as tk


from tkinter import ttk
from frames.const import *


class Profile(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style)

        self.controller = controller

        """ ATTRIBUTES """

        """ LAYOUT CONFIGURATION """

        """ FIRST ROW """
        offers_label = ttk.Label(
            self,
            text="Details",
            style="ProfileTitle2.TLabel"
        )

        offers_label.grid(row=0, column=0, sticky="EW",
                          padx=(40, 0), pady=(5, 10))

        """ SECOND ROW """
        # imgs

        """ THIRD ROW """
        name_label = ttk.Label(
            self,
            text="Name: Juan",
            style="ProfileInformation.TLabel"
        )
        id_label = ttk.Label(
            self,
            text="Identifier: 531441",
            style="ProfileInformation.TLabel"
        )

        name_label.grid(row=2, column=0, sticky="EW",
                        padx=(10, 0))
        id_label.grid(row=3, column=0, sticky="EW",
                      padx=(10, 0))

        """ FOURTH ROW """
