import settings
import tkinter as tk

from tkinter import CENTER, ttk
from frames.const import *
from PIL import ImageTk, Image
from utils.example_drivers import *

class OfferRow(ttk.Frame):
    def __init__(self, parent, index):
        super().__init__(parent, width=50, height=75)
        
        """ ATTRIBUTE """
        self.parent = parent
        self.index = index
        
        self.active = False
        self.checkbox_value = tk.BooleanVar(self)
        self.checkbox_value.set(False)
        self.checkbox = ttk.Checkbutton(
            parent,
            variable=self.checkbox_value, 
            command=self.checkbox_clicked,
            style="OffersCheckButton.TCheckbutton",
        )

        self.driver_str = tk.StringVar()
        self.date_str = tk.StringVar()
        self.destination_str = tk.StringVar()
        self.number_of_seats_str = tk.StringVar()
        self.cost_MXN_str = tk.StringVar()

        self.driver_label = ttk.Label(
            parent,
            textvariable=self.driver_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.date_label = ttk.Label(
            parent,
            textvariable=self.date_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.destination_label = ttk.Label(
            parent,
            textvariable=self.destination_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.seats_label = ttk.Label(
            parent,
            textvariable=self.number_of_seats_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.cost_label = ttk.Label(
            parent,
            textvariable=self.cost_MXN_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )

        self.driver_label.config(anchor=CENTER)
        self.date_label.config(anchor=CENTER)
        self.destination_label.config(anchor=CENTER)
        self.seats_label.config(anchor=CENTER)
        self.cost_label.config(anchor=CENTER)

        
    def checkbox_clicked(self):
        self.parent.delete_driver(self.index)
        
    def clear_row(self):
        self.driver_str.set("")
        self.date_str.set("")
        self.destination_str.set("")
        self.number_of_seats_str.set("")
        self.cost_MXN_str.set("")
        self.checkbox.grid_remove()
        if(self.active):
            self.checkbox.grid_remove()
            self.active = False
            
class Offers(ttk.Frame):

    def __init__(self, parent, controller, style):
        super().__init__(parent, style=style, width=50, height=75)

        """ ATTRIBUTES """
        self.controller = controller

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
        car_img = ImageTk.PhotoImage(Image.open(self.controller.CAR_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        car_panel = ttk.Label(self, image=car_img, style="OffersLabel.TLabel")
        car_panel.image = car_img

        clock_img = ImageTk.PhotoImage(Image.open(self.controller.CLOCK_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        clock_panel = ttk.Label(self, image=clock_img,
                                style="OffersLabel.TLabel")
        clock_panel.image = clock_img

        placeholder_img = ImageTk.PhotoImage(Image.open(self.controller.PLACEHOLDER_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        placeholder_panel = ttk.Label(
            self, image=placeholder_img, style="OffersLabel.TLabel")
        placeholder_panel.image = placeholder_img

        seats_img = ImageTk.PhotoImage(Image.open(self.controller.SEATS_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        seats_panel = ttk.Label(self, image=seats_img,
                                style="OffersLabel.TLabel")
        seats_panel.image = seats_img

        money_img = ImageTk.PhotoImage(Image.open(self.controller.MONEY_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        money_panel = ttk.Label(self, image=money_img,
                                style="OffersLabel.TLabel")
        money_panel.image = money_img

        car_panel.grid(row=1, column=1, sticky="NS", pady=(5, 0))
        clock_panel.grid(row=1, column=2, sticky="NS", pady=(5, 0))
        placeholder_panel.grid(row=1, column=3, sticky="NS", pady=(5, 0))
        seats_panel.grid(row=1, column=4, sticky="NS", pady=(5, 0))
        money_panel.grid(row=1, column=5, sticky="NS", pady=(5, 0))
        """ THIRD ROW """
        selection_label = ttk.Label(
            self,
            text="Your selection",
            style="OffersNormalText.TLabel",
            padding=(5, 5, 0, 0)

        )

        driver_label = ttk.Label(
            self,
            text="Driver",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        date_time_label = ttk.Label(
            self,
            text="Date & Time",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        destination_label = ttk.Label(
            self,
            text="Destination",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        seats_number_label = ttk.Label(
            self,
            text="# of seats",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        cost_MXN_label = ttk.Label(
            self,
            text="Cost MXN",
            style="OffersTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        selection_label.config(anchor=CENTER)
        driver_label.config(anchor=CENTER)
        date_time_label.config(anchor=CENTER)
        destination_label.config(anchor=CENTER)
        seats_number_label.config(anchor=CENTER)
        cost_MXN_label.config(anchor=CENTER)

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
        self.fourth_row = OfferRow(self, index=0)

        self.fourth_row.driver_label.grid(row=4, column=1)
        self.fourth_row.date_label.grid(row=4, column=2)
        self.fourth_row.destination_label.grid(row=4, column=3)
        self.fourth_row.seats_label.grid(row=4, column=4)
        self.fourth_row.cost_label.grid(row=4, column=5)

        """ FIFTH ROW """
        self.fifth_row = OfferRow(self, index=1)
    
        self.fifth_row.driver_label.grid(row=5, column=1)
        self.fifth_row.date_label.grid(row=5, column=2)
        self.fifth_row.destination_label.grid(row=5, column=3)
        self.fifth_row.seats_label.grid(row=5, column=4)
        self.fifth_row.cost_label.grid(row=5, column=5)

        """ SIXTH ROW """
        self.sixth_row = OfferRow(self, index=2)

        self.sixth_row.driver_label.grid(row=6, column=1)
        self.sixth_row.date_label.grid(row=6, column=2)
        self.sixth_row.destination_label.grid(row=6, column=3)
        self.sixth_row.seats_label.grid(row=6, column=4)
        self.sixth_row.cost_label.grid(row=6, column=5)

        """ SEVENTH ROW """
        self.seventh_row = OfferRow(self, index=3)
 
        self.seventh_row.driver_label.grid(row=7, column=1)
        self.seventh_row.date_label.grid(row=7, column=2)
        self.seventh_row.destination_label.grid(row=7, column=3)
        self.seventh_row.seats_label.grid(row=7, column=4)
        self.seventh_row.cost_label.grid(row=7, column=5)

        """ EIGTH ROW """
        self.eigth_row = OfferRow(self, index=4)

        self.eigth_row.driver_label.grid(row=8, column=1)
        self.eigth_row.date_label.grid(row=8, column=2)
        self.eigth_row.destination_label.grid(row=8, column=3)
        self.eigth_row.seats_label.grid(row=8, column=4)
        self.eigth_row.cost_label.grid(row=8, column=5)

        """ NINTH ROW """
        self.ninth_row = OfferRow(self, index=5)

        self.ninth_row.driver_label.grid(row=9, column=1)
        self.ninth_row.date_label.grid(row=9, column=2)
        self.ninth_row.destination_label.grid(row=9, column=3)
        self.ninth_row.seats_label.grid(row=9, column=4)
        self.ninth_row.cost_label.grid(row=9, column=5)

        self.rows = [
            self.fourth_row,
            self.fifth_row,
            self.sixth_row,
            self.seventh_row,
            self.eigth_row,
            self.ninth_row,
        ]
        
        self.update_driver_offer_rows()

    def clear_rows(self):
        for row in self.rows:
            row.clear_row()

    def update_driver_offer_rows(self):

        self.clear_rows()
        if not settings.g_rideshare_offers:
            return
        
        for index, ride in enumerate(settings.g_rideshare_offers):
            if index == 0:
                self.fourth_row.driver_str.set(ride.name)
                self.fourth_row.date_str.set(ride.date)
                self.fourth_row.destination_str.set(ride.destination)
                self.fourth_row.number_of_seats_str.set(ride.number_of_seats)
                self.fourth_row.cost_MXN_str.set(ride.cost_MXN)
                self.fourth_row.active = True
                # self.fourth_row.checkbox.grid(row=4, column=0)
                current_checkbox = self.fourth_row.checkbox
                current_checkbox.grid(row=4, column=0)

            if index == 1:
                self.fifth_row.driver_str.set(ride.name)
                self.fifth_row.date_str.set(ride.date)
                self.fifth_row.destination_str.set(ride.destination)
                self.fifth_row.number_of_seats_str.set(ride.number_of_seats)
                self.fifth_row.cost_MXN_str.set(ride.cost_MXN)
                self.fifth_row.active = True
                self.fifth_row.checkbox.grid(row=5, column=0)
            if index == 2:
                self.sixth_row.driver_str.set(ride.name)
                self.sixth_row.date_str.set(ride.date)
                self.sixth_row.destination_str.set(ride.destination)
                self.sixth_row.number_of_seats_str.set(ride.number_of_seats)
                self.sixth_row.cost_MXN_str.set(ride.cost_MXN)
                self.sixth_row.active = True
                self.sixth_row.checkbox.grid(row=6, column=0)

            if index == 3:
                self.seventh_row.driver_str.set(ride.name)
                self.seventh_row.date_str.set(ride.date)
                self.seventh_row.destination_str.set(ride.destination)
                self.seventh_row.number_of_seats_str.set(ride.number_of_seats)
                self.seventh_row.cost_MXN_str.set(ride.cost_MXN)
                self.seventh_row.active = True
                self.seventh_row.checkbox.grid(row=7, column=0)
            if index == 4:
                self.eigth_row.driver_str.set(ride.name)
                self.eigth_row.date_str.set(ride.date)
                self.eigth_row.destination_str.set(ride.destination)
                self.eigth_row.number_of_seats_str.set(ride.number_of_seats)
                self.eigth_row.cost_MXN_str.set(ride.cost_MXN)
                self.eigth_row.active = True
                self.eigth_row.checkbox.grid(row=8, column=0)
            if index == 5:
                self.ninth_row.driver_str.set(ride.name)
                self.ninth_row.date_str.set(ride.date)
                self.ninth_row.destination_str.set(ride.destination)
                self.ninth_row.number_of_seats_str.set(ride.number_of_seats)
                self.ninth_row.cost_MXN_str.set(ride.cost_MXN)
                self.ninth_row.active = True
                self.ninth_row.checkbox.grid(row=9, column=0)

    def delete_driver(self, deleted_driver_index):
        self.clear_rows()
        if not settings.g_rideshare_offers:
            return
        
        selected_driver = settings.g_rideshare_offers.pop(deleted_driver_index)
        settings.g_rideshare_future_travels.append(selected_driver)
        self.controller.future_travels_frame.update_rideshare_future_travels_rows()
        
        for index, ride in enumerate(settings.g_rideshare_offers):
            if index == 0:
                self.fourth_row.driver_str.set(ride.name)
                self.fourth_row.date_str.set(ride.date)
                self.fourth_row.destination_str.set(ride.destination)
                self.fourth_row.number_of_seats_str.set(ride.number_of_seats)
                self.fourth_row.cost_MXN_str.set(ride.cost_MXN)
                self.fourth_row.active = True
                self.fourth_row.checkbox.grid(row=4, column=0)
            if index == 1:
                self.fifth_row.driver_str.set(ride.name)
                self.fifth_row.date_str.set(ride.date)
                self.fifth_row.destination_str.set(ride.destination)
                self.fifth_row.number_of_seats_str.set(ride.number_of_seats)
                self.fifth_row.cost_MXN_str.set(ride.cost_MXN)
                self.fifth_row.active = True
                self.fifth_row.checkbox.grid(row=5, column=0)
            if index == 2:
                self.sixth_row.driver_str.set(ride.name)
                self.sixth_row.date_str.set(ride.date)
                self.sixth_row.destination_str.set(ride.destination)
                self.sixth_row.number_of_seats_str.set(ride.number_of_seats)
                self.sixth_row.cost_MXN_str.set(ride.cost_MXN)
                self.sixth_row.active = True
                self.sixth_row.checkbox.grid(row=6, column=0)

            if index == 3:
                self.seventh_row.driver_str.set(ride.name)
                self.seventh_row.date_str.set(ride.date)
                self.seventh_row.destination_str.set(ride.destination)
                self.seventh_row.number_of_seats_str.set(ride.number_of_seats)
                self.seventh_row.cost_MXN_str.set(ride.cost_MXN)
                self.seventh_row.active = True
                self.seventh_row.checkbox.grid(row=7, column=0)
            if index == 4:
                self.eigth_row.driver_str.set(ride.name)
                self.eigth_row.date_str.set(ride.date)
                self.eigth_row.destination_str.set(ride.destination)
                self.eigth_row.number_of_seats_str.set(ride.number_of_seats)
                self.eigth_row.cost_MXN_str.set(ride.cost_MXN)
                self.eigth_row.active = True
                self.eigth_row.checkbox.grid(row=8, column=0)
            if index == 5:
                self.ninth_row.driver_str.set(ride.name)
                self.ninth_row.date_str.set(ride.date)
                self.ninth_row.destination_str.set(ride.destination)
                self.ninth_row.number_of_seats_str.set(ride.number_of_seats)
                self.ninth_row.cost_MXN_str.set(ride.cost_MXN)
                self.ninth_row.active = True
                self.ninth_row.checkbox.grid(row=9, column=0)