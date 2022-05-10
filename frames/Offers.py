import tkinter as tk


from tkinter import CENTER, ttk
from frames.const import *
from PIL import ImageTk, Image
from utils.example_drivers import *


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
        self.fourth_row_checkbox_value = tk.BooleanVar(self)
        self.fourth_row_checkbox_value.set(False)
        self.fourth_row_checkbox = ttk.Checkbutton(
            self, variable=self.fourth_row_checkbox_value, command=self.fourth_row_checkbox_clicked,
            style="OffersCheckButton.TCheckbutton")

        self.fourth_row_driver_str = tk.StringVar()
        self.fourth_row_date_str = tk.StringVar()
        self.fourth_row_destination_str = tk.StringVar()
        self.fourth_row_number_of_seats_str = tk.StringVar()
        self.fourth_row_cost_MXN_str = tk.StringVar()

        self.fourth_row_driver_str.set(f'{EXAMPLE_DRIVER_1.name}')
        self.fourth_row_date_str.set(f'{EXAMPLE_DRIVER_1.date}')
        self.fourth_row_destination_str.set(
            f'{EXAMPLE_DRIVER_1.destination}')
        self.fourth_row_number_of_seats_str.set(
            f'{EXAMPLE_DRIVER_1.number_of_seats}')
        self.fourth_row_cost_MXN_str.set(f'{EXAMPLE_DRIVER_1.cost_MXN}')

        self.fourth_row_driver_label = ttk.Label(
            self,
            textvariable=self.fourth_row_driver_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_date_label = ttk.Label(
            self,
            textvariable=self.fourth_row_date_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_destination_label = ttk.Label(
            self,
            textvariable=self.fourth_row_destination_str,

            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_seats_label = ttk.Label(
            self,
            textvariable=self.fourth_row_number_of_seats_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fourth_row_cost_label = ttk.Label(
            self,
            textvariable=self.fourth_row_cost_MXN_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )

        self.fourth_row_driver_label.config(anchor=CENTER)
        self.fourth_row_date_label.config(anchor=CENTER)
        self.fourth_row_destination_label.config(anchor=CENTER)
        self.fourth_row_seats_label.config(anchor=CENTER)
        self.fourth_row_cost_label.config(anchor=CENTER)

        self.fourth_row_checkbox.grid(row=4, column=0)
        self.fourth_row_driver_label.grid(row=4, column=1)
        self.fourth_row_date_label.grid(row=4, column=2)
        self.fourth_row_destination_label.grid(row=4, column=3)
        self.fourth_row_seats_label.grid(row=4, column=4)
        self.fourth_row_cost_label.grid(row=4, column=5)

        """ FIFTH ROW """
        self.fifth_row_driver_str = tk.StringVar()
        self.fifth_row_date_str = tk.StringVar()
        self.fifth_row_destination_str = tk.StringVar()
        self.fifth_row_number_of_seats_str = tk.StringVar()
        self.fifth_row_cost_MXN_str = tk.StringVar()

        self.fifth_row_driver_str.set(f'{EXAMPLE_DRIVER_2.name}')
        self.fifth_row_date_str.set(f'{EXAMPLE_DRIVER_2.date}')
        self.fifth_row_destination_str.set(
            f'{EXAMPLE_DRIVER_2.destination}')
        self.fifth_row_number_of_seats_str.set(
            f'{EXAMPLE_DRIVER_2.number_of_seats}')
        self.fifth_row_cost_MXN_str.set(f'{EXAMPLE_DRIVER_2.cost_MXN}')

        self.fifth_row_checkbox_value = tk.BooleanVar(self)
        self.fifth_row_checkbox_value.set(False)
        self.fifth_row_checkbox = ttk.Checkbutton(
            self, variable=self.fifth_row_checkbox_value, command=self.fifth_row_checkbox_clicked,
            style="OffersCheckButton.TCheckbutton")

        self.fifth_row_driver_label = ttk.Label(
            self,
            textvariable=self.fifth_row_driver_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_date_label = ttk.Label(
            self,
            textvariable=self.fifth_row_date_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_destination_label = ttk.Label(
            self,
            textvariable=self.fifth_row_destination_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_seats_label = ttk.Label(
            self,
            textvariable=self.fifth_row_number_of_seats_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)

        )
        self.fifth_row_cost_label = ttk.Label(
            self,
            textvariable=self.fifth_row_cost_MXN_str,
            style="OffersNormalText.TLabel",
            padding=(0, 0, 5, 0)
        )

        self.fifth_row_driver_label.config(anchor=CENTER)
        self.fifth_row_date_label.config(anchor=CENTER)
        self.fifth_row_destination_label.config(anchor=CENTER)
        self.fifth_row_seats_label.config(anchor=CENTER)
        self.fifth_row_cost_label.config(anchor=CENTER)

        self.fifth_row_checkbox.grid(row=5, column=0)
        self.fifth_row_driver_label.grid(row=5, column=1)
        self.fifth_row_date_label.grid(row=5, column=2)
        self.fifth_row_destination_label.grid(row=5, column=3)
        self.fifth_row_seats_label.grid(row=5, column=4)
        self.fifth_row_cost_label.grid(row=5, column=5)

    def upper_row_shift(self):
        self.fourth_row_driver_str.set(EXAMPLE_DRIVER_2.name)
        self.fourth_row_date_str.set(EXAMPLE_DRIVER_2.date)
        self.fourth_row_destination_str.set(EXAMPLE_DRIVER_2.destination)
        self.fourth_row_number_of_seats_str.set(
            EXAMPLE_DRIVER_2.number_of_seats)
        self.fourth_row_cost_MXN_str.set(EXAMPLE_DRIVER_2.cost_MXN)

        empty_space = ""
        self.fifth_row_driver_str.set(empty_space)
        self.fifth_row_date_str.set(empty_space)
        self.fifth_row_destination_str.set(empty_space)
        self.fifth_row_number_of_seats_str.set(empty_space)
        self.fifth_row_cost_MXN_str.set(empty_space)

        self.fifth_row_checkbox.grid_remove()

    def fourth_row_checkbox_clicked(self):
        self.upper_row_shift()

    def fifth_row_checkbox_clicked(self):
        pass
