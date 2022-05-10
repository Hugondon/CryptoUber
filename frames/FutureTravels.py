import settings
import tkinter as tk


from tkinter import CENTER, ttk
from frames.const import *
from PIL import ImageTk, Image
from utils.example_drivers import *


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
            style="TravelsTitle2.TLabel"
        )

        future_travels_label.grid(row=0, column=0, columnspan=6, sticky="EW",
                                  padx=(200, 200), pady=(5, 0))

        """ SECOND ROW """
        car_img = ImageTk.PhotoImage(Image.open(self.controller.CAR_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        car_panel = ttk.Label(self, image=car_img, style="TravelsLabel.TLabel")
        car_panel.image = car_img

        clock_img = ImageTk.PhotoImage(Image.open(self.controller.CLOCK_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        clock_panel = ttk.Label(self, image=clock_img,
                                style="TravelsLabel.TLabel")
        clock_panel.image = clock_img

        placeholder_img = ImageTk.PhotoImage(Image.open(self.controller.PLACEHOLDER_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        placeholder_panel = ttk.Label(
            self, image=placeholder_img, style="TravelsLabel.TLabel")
        placeholder_panel.image = placeholder_img

        seats_img = ImageTk.PhotoImage(Image.open(self.controller.SEATS_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        seats_panel = ttk.Label(self, image=seats_img,
                                style="TravelsLabel.TLabel")
        seats_panel.image = seats_img

        money_img = ImageTk.PhotoImage(Image.open(self.controller.MONEY_PNG_PATH).resize(
            (self.controller.PNG_WIDTH//self.controller.PNG_RESIZE_FACTOR, self.controller.PNG_HEIGHT//self.controller.PNG_RESIZE_FACTOR)))
        money_panel = ttk.Label(self, image=money_img,
                                style="TravelsLabel.TLabel")
        money_panel.image = money_img

        car_panel.grid(row=1, column=1, sticky="NS", pady=(5, 0))
        clock_panel.grid(row=1, column=2, sticky="NS", pady=(5, 0))
        placeholder_panel.grid(row=1, column=3, sticky="NS", pady=(5, 0))
        seats_panel.grid(row=1, column=4, sticky="NS", pady=(5, 0))
        money_panel.grid(row=1, column=5, sticky="NS", pady=(5, 0))
        """ THIRD ROW """
        selection_label = ttk.Label(
            self,
            text="Accepted",
            style="TravelsNormalText.TLabel",
            padding=(5, 5, 5, 0)

        )

        driver_label = ttk.Label(
            self,
            text="Driver",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        date_time_label = ttk.Label(
            self,
            text="Date & Time",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        destination_label = ttk.Label(
            self,
            text="Destination",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        seats_number_label = ttk.Label(
            self,
            text="# of seats",
            style="TravelsTitle3.TLabel",
            padding=(10, 5, 5, 0)
        )
        cost_MXN_label = ttk.Label(
            self,
            text="Cost MXN",
            style="TravelsTitle3.TLabel",
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
        table_separator.grid(row=3, columnspan=6, padx=(10, 10), sticky="EW")

        """ FOURTH ROW """

        self.fourth_row_accepted_str = tk.StringVar()
        self.fourth_row_driver_str = tk.StringVar()
        self.fourth_row_date_str = tk.StringVar()
        self.fourth_row_destination_str = tk.StringVar()
        self.fourth_row_number_of_seats_str = tk.StringVar()
        self.fourth_row_cost_MXN_str = tk.StringVar()

        self.fourth_row_accepted_label = ttk.Label(
            self,
            textvariable=self.fourth_row_accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.fourth_row_driver_label = ttk.Label(
            self,
            textvariable=self.fourth_row_driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.fourth_row_date_label = ttk.Label(
            self,
            textvariable=self.fourth_row_date_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_destination_label = ttk.Label(
            self,
            textvariable=self.fourth_row_destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_seats_label = ttk.Label(
            self,
            textvariable=self.fourth_row_number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_cost_label = ttk.Label(
            self,
            textvariable=self.fourth_row_cost_MXN_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )

        self.fourth_row_accepted_label.config(anchor=CENTER)
        self.fourth_row_driver_label.config(anchor=CENTER)
        self.fourth_row_date_label.config(anchor=CENTER)
        self.fourth_row_destination_label.config(anchor=CENTER)
        self.fourth_row_seats_label.config(anchor=CENTER)
        self.fourth_row_cost_label.config(anchor=CENTER)

        self.fourth_row_accepted_label.grid(row=4, column=0)
        self.fourth_row_driver_label.grid(row=4, column=1)
        self.fourth_row_date_label.grid(row=4, column=2)
        self.fourth_row_destination_label.grid(row=4, column=3)
        self.fourth_row_seats_label.grid(row=4, column=4)
        self.fourth_row_cost_label.grid(row=4, column=5)

        """ FIFTH ROW """

        self.fifth_row_accepted_str = tk.StringVar()
        self.fifth_row_driver_str = tk.StringVar()
        self.fifth_row_date_str = tk.StringVar()
        self.fifth_row_destination_str = tk.StringVar()
        self.fifth_row_number_of_seats_str = tk.StringVar()
        self.fifth_row_cost_MXN_str = tk.StringVar()

        self.fifth_row_accepted_label = ttk.Label(
            self,
            textvariable=self.fifth_row_accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.fifth_row_driver_label = ttk.Label(
            self,
            textvariable=self.fifth_row_driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.fifth_row_date_label = ttk.Label(
            self,
            textvariable=self.fifth_row_date_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_destination_label = ttk.Label(
            self,
            textvariable=self.fifth_row_destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_seats_label = ttk.Label(
            self,
            textvariable=self.fifth_row_number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_cost_label = ttk.Label(
            self,
            textvariable=self.fifth_row_cost_MXN_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )

        self.fifth_row_accepted_label.config(anchor=CENTER)
        self.fifth_row_driver_label.config(anchor=CENTER)
        self.fifth_row_date_label.config(anchor=CENTER)
        self.fifth_row_destination_label.config(anchor=CENTER)
        self.fifth_row_seats_label.config(anchor=CENTER)
        self.fifth_row_cost_label.config(anchor=CENTER)

        self.fifth_row_accepted_label.grid(row=5, column=0)
        self.fifth_row_driver_label.grid(row=5, column=1)
        self.fifth_row_date_label.grid(row=5, column=2)
        self.fifth_row_destination_label.grid(row=5, column=3)
        self.fifth_row_seats_label.grid(row=5, column=4)
        self.fifth_row_cost_label.grid(row=5, column=5)

        """ SIXTH ROW """

        self.sixth_row_accepted_str = tk.StringVar()
        self.sixth_row_driver_str = tk.StringVar()
        self.sixth_row_date_str = tk.StringVar()
        self.sixth_row_destination_str = tk.StringVar()
        self.sixth_row_number_of_seats_str = tk.StringVar()
        self.sixth_row_cost_MXN_str = tk.StringVar()

        self.sixth_row_accepted_label = ttk.Label(
            self,
            textvariable=self.sixth_row_accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.sixth_row_driver_label = ttk.Label(
            self,
            textvariable=self.sixth_row_driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.sixth_row_date_label = ttk.Label(
            self,
            textvariable=self.sixth_row_date_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.sixth_row_destination_label = ttk.Label(
            self,
            textvariable=self.sixth_row_destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.sixth_row_seats_label = ttk.Label(
            self,
            textvariable=self.sixth_row_number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.sixth_row_cost_label = ttk.Label(
            self,
            textvariable=self.sixth_row_cost_MXN_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )

        self.sixth_row_accepted_label.config(anchor=CENTER)
        self.sixth_row_driver_label.config(anchor=CENTER)
        self.sixth_row_date_label.config(anchor=CENTER)
        self.sixth_row_destination_label.config(anchor=CENTER)
        self.sixth_row_seats_label.config(anchor=CENTER)
        self.sixth_row_cost_label.config(anchor=CENTER)

        self.sixth_row_accepted_label.grid(row=6, column=0)
        self.sixth_row_driver_label.grid(row=6, column=1)
        self.sixth_row_date_label.grid(row=6, column=2)
        self.sixth_row_destination_label.grid(row=6, column=3)
        self.sixth_row_seats_label.grid(row=6, column=4)
        self.sixth_row_cost_label.grid(row=6, column=5)

        """ SEVENTH ROW """

        self.seventh_row_accepted_str = tk.StringVar()
        self.seventh_row_driver_str = tk.StringVar()
        self.seventh_row_date_str = tk.StringVar()
        self.seventh_row_destination_str = tk.StringVar()
        self.seventh_row_number_of_seats_str = tk.StringVar()
        self.seventh_row_cost_MXN_str = tk.StringVar()

        self.seventh_row_accepted_label = ttk.Label(
            self,
            textvariable=self.seventh_row_accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.seventh_row_driver_label = ttk.Label(
            self,
            textvariable=self.seventh_row_driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.seventh_row_date_label = ttk.Label(
            self,
            textvariable=self.seventh_row_date_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.seventh_row_destination_label = ttk.Label(
            self,
            textvariable=self.seventh_row_destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.seventh_row_seats_label = ttk.Label(
            self,
            textvariable=self.seventh_row_number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.seventh_row_cost_label = ttk.Label(
            self,
            textvariable=self.seventh_row_cost_MXN_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )

        self.seventh_row_accepted_label.config(anchor=CENTER)
        self.seventh_row_driver_label.config(anchor=CENTER)
        self.seventh_row_date_label.config(anchor=CENTER)
        self.seventh_row_destination_label.config(anchor=CENTER)
        self.seventh_row_seats_label.config(anchor=CENTER)
        self.seventh_row_cost_label.config(anchor=CENTER)

        self.seventh_row_accepted_label.grid(row=7, column=0)
        self.seventh_row_driver_label.grid(row=7, column=1)
        self.seventh_row_date_label.grid(row=7, column=2)
        self.seventh_row_destination_label.grid(row=7, column=3)
        self.seventh_row_seats_label.grid(row=7, column=4)
        self.seventh_row_cost_label.grid(row=7, column=5)

        """ EIGTH ROW """

        self.eigth_row_accepted_str = tk.StringVar()
        self.eigth_row_driver_str = tk.StringVar()
        self.eigth_row_date_str = tk.StringVar()
        self.eigth_row_destination_str = tk.StringVar()
        self.eigth_row_number_of_seats_str = tk.StringVar()
        self.eigth_row_cost_MXN_str = tk.StringVar()

        self.eigth_row_accepted_label = ttk.Label(
            self,
            textvariable=self.eigth_row_accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.eigth_row_driver_label = ttk.Label(
            self,
            textvariable=self.eigth_row_driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.eigth_row_date_label = ttk.Label(
            self,
            textvariable=self.eigth_row_date_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.eigth_row_destination_label = ttk.Label(
            self,
            textvariable=self.eigth_row_destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.eigth_row_seats_label = ttk.Label(
            self,
            textvariable=self.eigth_row_number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.eigth_row_cost_label = ttk.Label(
            self,
            textvariable=self.eigth_row_cost_MXN_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )

        self.eigth_row_accepted_label.config(anchor=CENTER)
        self.eigth_row_driver_label.config(anchor=CENTER)
        self.eigth_row_date_label.config(anchor=CENTER)
        self.eigth_row_destination_label.config(anchor=CENTER)
        self.eigth_row_seats_label.config(anchor=CENTER)
        self.eigth_row_cost_label.config(anchor=CENTER)

        self.eigth_row_accepted_label.grid(row=8, column=0)
        self.eigth_row_driver_label.grid(row=8, column=1)
        self.eigth_row_date_label.grid(row=8, column=2)
        self.eigth_row_destination_label.grid(row=8, column=3)
        self.eigth_row_seats_label.grid(row=8, column=4)
        self.eigth_row_cost_label.grid(row=8, column=5)

        """ NINTH ROW """

        self.ninth_row_accepted_str = tk.StringVar()
        self.ninth_row_driver_str = tk.StringVar()
        self.ninth_row_date_str = tk.StringVar()
        self.ninth_row_destination_str = tk.StringVar()
        self.ninth_row_number_of_seats_str = tk.StringVar()
        self.ninth_row_cost_MXN_str = tk.StringVar()

        self.ninth_row_accepted_label = ttk.Label(
            self,
            textvariable=self.ninth_row_accepted_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.ninth_row_driver_label = ttk.Label(
            self,
            textvariable=self.ninth_row_driver_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )
        self.ninth_row_date_label = ttk.Label(
            self,
            textvariable=self.ninth_row_date_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.ninth_row_destination_label = ttk.Label(
            self,
            textvariable=self.ninth_row_destination_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.ninth_row_seats_label = ttk.Label(
            self,
            textvariable=self.ninth_row_number_of_seats_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.ninth_row_cost_label = ttk.Label(
            self,
            textvariable=self.ninth_row_cost_MXN_str,
            style="TravelsNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )

        self.ninth_row_accepted_label.config(anchor=CENTER)
        self.ninth_row_driver_label.config(anchor=CENTER)
        self.ninth_row_date_label.config(anchor=CENTER)
        self.ninth_row_destination_label.config(anchor=CENTER)
        self.ninth_row_seats_label.config(anchor=CENTER)
        self.ninth_row_cost_label.config(anchor=CENTER)

        self.ninth_row_accepted_label.grid(row=9, column=0)
        self.ninth_row_driver_label.grid(row=9, column=1)
        self.ninth_row_date_label.grid(row=9, column=2)
        self.ninth_row_destination_label.grid(row=9, column=3)
        self.ninth_row_seats_label.grid(row=9, column=4)
        self.ninth_row_cost_label.grid(row=9, column=5)

        self.update_rideshare_future_travels_rows()

    def clear_rows(self):
        self.fourth_row_accepted_str.set("")
        self.fourth_row_driver_str.set("")
        self.fourth_row_date_str.set("")
        self.fourth_row_destination_str.set("")
        self.fourth_row_number_of_seats_str.set("")
        self.fourth_row_cost_MXN_str.set("")

        self.fifth_row_accepted_str.set("")
        self.fifth_row_driver_str.set("")
        self.fifth_row_date_str.set("")
        self.fifth_row_destination_str.set("")
        self.fifth_row_number_of_seats_str.set("")
        self.fifth_row_cost_MXN_str.set("")

        self.sixth_row_accepted_str.set("")
        self.sixth_row_driver_str.set("")
        self.sixth_row_date_str.set("")
        self.sixth_row_destination_str.set("")
        self.sixth_row_number_of_seats_str.set("")
        self.sixth_row_cost_MXN_str.set("")

        self.seventh_row_accepted_str.set("")
        self.seventh_row_driver_str.set("")
        self.seventh_row_date_str.set("")
        self.seventh_row_destination_str.set("")
        self.seventh_row_number_of_seats_str.set("")
        self.seventh_row_cost_MXN_str.set("")

        self.eigth_row_accepted_str.set("")
        self.eigth_row_driver_str.set("")
        self.eigth_row_date_str.set("")
        self.eigth_row_destination_str.set("")
        self.eigth_row_number_of_seats_str.set("")
        self.eigth_row_cost_MXN_str.set("")

        self.ninth_row_accepted_str.set("")
        self.ninth_row_driver_str.set("")
        self.ninth_row_date_str.set("")
        self.ninth_row_destination_str.set("")
        self.ninth_row_number_of_seats_str.set("")
        self.ninth_row_cost_MXN_str.set("")

    def update_rideshare_future_travels_rows(self):
        self.clear_rows()
        # Esto se puede hacer más eficientemente, estoy seguro.
        for index, ride in enumerate(settings.g_rideshare_future_travels):
            if index == 0:
                self.fourth_row_accepted_str.set("✓")
                self.fourth_row_driver_str.set(ride.name)
                self.fourth_row_date_str.set(ride.date)
                self.fourth_row_destination_str.set(ride.destination)
                self.fourth_row_number_of_seats_str.set(ride.number_of_seats)
                self.fourth_row_cost_MXN_str.set(ride.cost_MXN)
            if index == 1:
                self.fifth_row_accepted_str.set("✓")
                self.fifth_row_driver_str.set(ride.name)
                self.fifth_row_date_str.set(ride.date)
                self.fifth_row_destination_str.set(ride.destination)
                self.fifth_row_number_of_seats_str.set(ride.number_of_seats)
                self.fifth_row_cost_MXN_str.set(ride.cost_MXN)
            if index == 2:
                self.sixth_row_accepted_str.set("✓")
                self.sixth_row_driver_str.set(ride.name)
                self.sixth_row_date_str.set(ride.date)
                self.sixth_row_destination_str.set(ride.destination)
                self.sixth_row_number_of_seats_str.set(ride.number_of_seats)
                self.sixth_row_cost_MXN_str.set(ride.cost_MXN)
            if index == 3:
                self.seventh_row_accepted_str.set("✓")
                self.seventh_row_driver_str.set(ride.name)
                self.seventh_row_date_str.set(ride.date)
                self.seventh_row_destination_str.set(ride.destination)
                self.seventh_row_number_of_seats_str.set(ride.number_of_seats)
                self.seventh_row_cost_MXN_str.set(ride.cost_MXN)
            if index == 4:
                self.eigth_row_accepted_str.set("✓")
                self.eigth_row_driver_str.set(ride.name)
                self.eigth_row_date_str.set(ride.date)
                self.eigth_row_destination_str.set(ride.destination)
                self.eigth_row_number_of_seats_str.set(ride.number_of_seats)
                self.eigth_row_cost_MXN_str.set(ride.cost_MXN)
            if index == 5:
                self.ninth_row_accepted_str.set("✓")
                self.ninth_row_driver_str.set(ride.name)
                self.ninth_row_date_str.set(ride.date)
                self.ninth_row_destination_str.set(ride.destination)
                self.ninth_row_number_of_seats_str.set(ride.number_of_seats)
                self.ninth_row_cost_MXN_str.set(ride.cost_MXN)
