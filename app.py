from fastapi import FastAPI
import datetime
import tkinter as tk
import customtkinter as ctk
import sys
import os

path = os.path.abspath("db")
sys.path.append(path)
from residentsDAO import ResidentsDAO
from leasingDAO import LeasingDAO
from apartmentsDAO import ApartmentsDAO

# declaring classes to be used for queries to database
res_query = ResidentsDAO()
lease_query = LeasingDAO()
apt_query = ApartmentsDAO()

def main():

    # Root object for tkinter GUI
    root = ctk.CTk()
    root.geometry('800x500')

    # String variable for text entry boxes
    res_id = tk.StringVar()
    first_name = tk.StringVar()
    last_name = tk.StringVar()
    email = tk.StringVar()
    phone = tk.StringVar()
    birthdate = tk.StringVar()
    gender = tk.StringVar()
    start_date = tk.StringVar()
    end_date = tk.StringVar()

    # All the leases in the database
    leases = lease_query.get_leases()
    row_num = 0

    # Iterate through the leases and create button interactions for each
    for lease in leases:

        # Create the labels and entry boxes that will be used when viewing a profile
        lbl_name = ctk.CTkLabel(root, text="")
        lbl_email = ctk.CTkLabel(root, text="")
        lbl_phone = ctk.CTkLabel(root, text="")
        lbl_birth = ctk.CTkLabel(root, text="")
        lbl_dates = ctk.CTkLabel(root, text="")
        lbl_complex = ctk.CTkLabel(root, text="")
        lbl_addr = ctk.CTkLabel(root, text="")
        lbl_apt = ctk.CTkLabel(root, text="")
        lbl_room = ctk.CTkLabel(root, text="")
        lbl_rent = ctk.CTkLabel(root, text="")
        ent_first_name = ctk.CTkEntry(root, textvariable=first_name)
        ent_last_name = ctk.CTkEntry(root, textvariable=last_name)
        ent_email = ctk.CTkEntry(root, textvariable=email)
        ent_phone = ctk.CTkEntry(root, textvariable=phone)
        ent_dob = ctk.CTkEntry(root, textvariable=birthdate)
        btn_save = ctk.CTkButton(root, text='Save', fg_color='light green', text_color='gray', hover_color='light blue')

        def save():
            """ Update the resident profile and disable all entry boxes again. """

            # Resident data to be sent in db query
            resident = {'first_name': first_name.get(),
                        'last_name': last_name.get(),
                        'email': email.get(),
                        'phone': phone.get(),
                        'birthdate': birthdate.get(),
                        'gender': gender.get()}
            
            # Send query
            res_query.update_resident(res_id.get(), resident)

            # Disable all entry boxes and the save button
            ent_first_name.configure(state="disabled", fg_color='light gray')
            ent_last_name.configure(state="disabled", fg_color='light gray')
            ent_email.configure(state="disabled", fg_color='light gray')
            ent_phone.configure(state="disabled", fg_color='light gray')
            ent_dob.configure(state="disabled", fg_color='light gray')
            btn_save.configure(state="disabled")

        btn_save.configure(command=save)

        def edit():
            """ Enable entry boxes and save button. """

            ent_first_name.configure(state='normal', fg_color='white')
            ent_last_name.configure(state='normal', fg_color='white')
            ent_email.configure(state='normal', fg_color='white')
            ent_phone.configure(state='normal', fg_color='white')
            ent_dob.configure(state='normal', fg_color='white')

            btn_save.configure(state="normal")
            btn_save.grid(column=7, row=8)

            
        def display_lease(lease=lease):
            """ Based on selected lease display the details and ability to edit. """

            # Query for the resident, their unit, and their complex data based on corresponding lease
            resident = res_query.get_resident_by_id(lease['resident_id'])
            unit = apt_query.get_unit_by_id(lease['unit_id'])
            cmplx = apt_query.get_complex_by_id(unit['complex_id'])

            # Configure the labels and entry boxes to now contain data
            lbl_name.configure(text='Name: ')
            lbl_email.configure(text='Email: ')
            lbl_phone.configure(text='Phone Number: ')
            lbl_birth.configure(text='Date of Birth: ')
            lbl_dates.configure(text='Lease Dates: ' + lease['lease_start'] + ' to ' + lease['lease_end'])
            lbl_complex.configure(text=cmplx['name'])
            lbl_addr.configure(text=cmplx['addr'])
            lbl_apt.configure(text='#' + unit['apt_num'])
            lbl_room.configure(text='Room ' + unit['room'] + ' Bed ' + unit['bed'])
            lbl_rent.configure(text='Rent: $' + str(unit['rent']))

            # Default that the entry boxes will be disabled until the edit button is pressed.
            ent_first_name.configure(state="disabled", fg_color='light gray')
            ent_last_name.configure(state="disabled", fg_color='light gray')
            ent_email.configure(state="disabled", fg_color='light gray')
            ent_phone.configure(state="disabled", fg_color='light gray')
            ent_dob.configure(state="disabled", fg_color='light gray')

            res_id.set(lease['resident_id'])
            first_name.set(resident['first_name'])
            last_name.set(resident['last_name'])
            email.set(resident['email'])
            phone.set(resident['phone'])
            birthdate.set(resident['birthdate'])
            gender.set(resident['gender'])
            
            btn_edit = ctk.CTkButton(root, text="Edit", fg_color='green', command=edit)
            btn_edit.grid(row=7, column=7)

            # Add the entry boxes only once a lease has been pressed to keep interface clean.
            ent_first_name.grid(column=6, row=2)
            ent_last_name.grid(column=6, row=3)
            ent_email.grid(column=6, row=4)
            ent_phone.grid(column=6, row=5)
            ent_dob.grid(column=6, row=6)

        # Get the resident name from the database
        name = res_query.get_resident_by_id(lease['resident_id'])['first_name']

        # Create button that will allow user to view details to specific lease/profile
        lbl_lease = ctk.CTkButton(root, text="View " + name + "'s Profile", command=display_lease)
        lbl_lease.grid(column=2, columnspan=2, row=row_num, padx=30)
        row_num += 1
        
        # Arrange widgets
        lbl_name.grid(column=5, row=2, padx=30)
        lbl_email.grid(column=5, row=4)
        lbl_phone.grid(column=5, row=5)
        lbl_birth.grid(column=5, row=6)
        lbl_rent.grid(column=5, row=7)
        lbl_dates.grid(column=7, row=2)
        lbl_complex.grid(column=7, row=3)
        lbl_addr.grid(column=7, row=4)
        lbl_apt.grid(column=7, row=5)
        lbl_room.grid(column=7, row=6)

    def get_rent_roll():
        """ Get the rent roll using db query and dates from entry boxes. """

        # Dates from entry boxes
        start = start_date.get()
        end = end_date.get()

        # Open new dialog window
        dialog = None
        if (start != "" and end != ""):

            # Get the rent roll data from the database. 
            rent_roll = lease_query.get_rent_roll(start, end)

            if dialog is None or not dialog.winfo_exists():
                dialog = ctk.CTkToplevel()
            dialog.focus()

            # Add title labels
            lbl_cplx_name = ctk.CTkLabel(dialog, text='Complex Name')
            lbl_apt_num = ctk.CTkLabel(dialog, text='Apartment Number')
            lbl_res_name = ctk.CTkLabel(dialog, text='Resident Name')
            lbl_rent_owe = ctk.CTkLabel(dialog, text="Rent Owed")

            # Display rent roll data to the new window
            row_num = 1
            for i in rent_roll:
                lbl_c = ctk.CTkLabel(dialog, text=i['complex_name'])
                lbl_a = ctk.CTkLabel(dialog, text=i['apartment'])
                lbl_n = ctk.CTkLabel(dialog, text=i['resident_name'])
                lbl_r = ctk.CTkLabel(dialog, text=i['rent_price'])

                lbl_c.grid(column=1, row=row_num)
                lbl_a.grid(column=2, row=row_num)
                lbl_n.grid(column=3, row=row_num)
                lbl_r.grid(column=4, row=row_num)

                row_num += 1

            # Arrange title widgets. 
            lbl_cplx_name.grid(column=1, row=0, padx=30)
            lbl_apt_num.grid(column=2, row=0, padx=30)
            lbl_res_name.grid(column=3, row=0, padx=30)
            lbl_rent_owe.grid(column=4, row=0, padx=30)

    def get_rent():
        """ Get the calculated total rent over a period of time. """

        # Get the dates from the entry boxes. 
        start = start_date.get()
        end = end_date.get()
        rent = 0

        # As long as the dates are not empty query the database
        if (start != "" and end != ""):
            rent = lease_query.get_total_rent(start, end)
        else:
            rent = 0

        # Display the rent to the main window
        lbl_total_rent = ctk.CTkLabel(root, text='$' + str(rent))
        lbl_total_rent.grid(column=8, row=11)

    def get_capacity():
        """ Get the capacity percentage and display to the main window. """

        # Get the dates from the entry boxes. 
        start = start_date.get()
        end = end_date.get()

        # Get the capacity from the database and put to the screen as long as the dates are not empty. 
        if (start != "" and end != ""):
            capacity = lease_query.get_capacity(start, end)
            lbl_capacity = ctk.CTkLabel(root, text=capacity['cap_percent'])
            lbl_capacity.grid(column=8, row=12)

    # Create the widgets for the date entry and data retrieval for different reports. 
    lbl_start = ctk.CTkLabel(root, text='Start Date: ')
    lbl_end = ctk.CTkLabel(root, text='End Date: ')
    lbl_format = ctk.CTkLabel(root, text='yyyy-mm-dd', text_color='gray')
    ent_start = ctk.CTkEntry(root, textvariable=start_date)
    ent_end = ctk.CTkEntry(root, textvariable=end_date)
    btn_rent_roll = ctk.CTkButton(root, text='Rent Roll Report', command=get_rent_roll)
    btn_rent = ctk.CTkButton(root, text='Rent Due', command=get_rent)
    btn_capacity = ctk.CTkButton(root, text='Capacity Details', command=get_capacity)

    # Arrange widgets. 
    lbl_start.grid(column=5, row=10)
    lbl_end.grid(column=5, row=11)
    lbl_format.grid(column=6, row=12)
    ent_start.grid(column=6, row=10)
    ent_end.grid(column=6, row=11)
    btn_rent_roll.grid(column=7, row=10)
    btn_rent.grid(column=7, row=11)
    btn_capacity.grid(column=7, row=12)

    root.mainloop()

# app = FastAPI()

# @app.get('/')
# async def root():
#     return {'example': 'This is an example', 
#             'data': 0}

if __name__=='__main__':
    main()