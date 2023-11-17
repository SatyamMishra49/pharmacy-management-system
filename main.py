import tkinter as tk
from tkinter import messagebox


def create_medicine():
    medicine_id = entry_id.get()
    medicine_name = entry_name.get()
    medicine_quantity = entry_weight.get()
    #medicine_description=entry_description.get()
    medicine_company = entry_company.get()
    medicine_contact = entry_emergency.get()


    with open('medicines.txt', 'a') as file:
        file.write(f"{medicine_id},{medicine_name},{medicine_quantity},"f",{medicine_company},{medicine_contact}\n")

    messagebox.showinfo("Success", "medicine created successfully!")


def display_medicines():
    medicine_text.delete('1.0', tk.END)
    with open('medicines.txt', 'r') as file:
        medicines = file.readlines()

    for medicine in medicines:
        medicine_data = medicine.strip().split(',')
        medicine_text.insert(tk.END, f"ID: {medicine_data[0]}\n"
                                     f"Name: {medicine_data[1]}\n"
                                     f"Quantity: {medicine_data[2]}\n"
        
                                     #f"Description: {medicine_data[3]}\n"
        
                                     f"Company: {medicine_data[4]}\n"
                                     f"Contact: {medicine_data[5]}\n")



def search_medicine():
    medicine_id = entry_search_id.get()

    with open('medicines.txt', 'r') as file:
        medicines = file.readlines()

    for medicine in medicines:
        medicine_data = medicine.strip().split(',')
        if medicine_data[0] == medicine_id:
            messagebox.showinfo("Medicine Found",
                                f"ID: {medicine_data[0]}\n"
                                f"Name: {medicine_data[1]}\n"
                                f"Quantity: {medicine_data[2]}\n"
                                #f"Description: {medicine_data[3]}\n"
                                f"Company: {medicine_data[4]}\n"
                                f"Emergency Contact: {medicine_data[5]}\n")

            return

    messagebox.showinfo("Medicine Not Found", "Medicine not found!")


def delete_medicine():
    medicine_id = entry_search_id.get()

    with open('medicines.txt', 'r') as file:
        medicines = file.readlines()

    with open('medicines.txt', 'w') as file:
        deleted = False
        for medicine in medicines:
            medicine_data = medicine.strip().split(',')
            if medicine_data[0] != medicine_id:
                file.write(medicine)
            else:
                deleted = True
                if deleted: messagebox.showinfo("Success", f"medicine with ID {medicine_id} has been deleted!")
        else:
            messagebox.showinfo("Not Found", f"No medicine found with ID {medicine_id}")


def update_medicine():
    medicine_id = entry_update_id.get()
    field_name = entry_update_field.get()
    new_value = entry_update_value.get()

    field_index = get_field_index(field_name)

    if field_index is None:
        messagebox.showerror("Error", "Invalid field name!")
        return

    with open('medicines.txt', 'r') as file:
        medicines = file.readlines()

    with open('medicines.txt', 'w') as file:
        for medicine in medicines:
            medicine_data = medicine.strip().split(',')
            if medicine_data[0] == medicine_id:
                if field_index == 0:
                    messagebox.showerror("Error", "Cannot update Medicine ID!")
                    file.write(medicine)
                else:
                    medicine_data[field_index] = new_value
                    file.write(','.join(medicine_data) + '\n')
            else:
                file.write(medicine)

    messagebox.showinfo("Success", "Medicine updated successfully!")


def get_field_index(field_name):
    fields = ['ID', 'Name', 'Quantity', 'Description','Company','Contact']
    try:
        return fields.index(field_name)
    except ValueError:
        return None


def create_distributor():
    distributor_id = entry_distributor_id.get()
    distributor_name = entry_distributor_name.get()


    with open('distributors.txt', 'a') as file:
        file.write(f"{distributor_id},{distributor_name}\n")

    messagebox.showinfo("Success", "Distributor created successfully!")


def display_distributors():
    distributor_text.delete('1.0', tk.END)
    with open('distributors.txt', 'r') as file:
        distributors = file.readlines()

    for distributor in distributors:
        distributor_data = distributor.strip().split(',')
        distributor_text.insert(tk.END, f"ID: {distributor_data[0]}\n"
                                        f"Name: {distributor_data[1]}\n")


def search_distributor():
    distributor_id = entry_search_distributor_id.get()

    with open('distributors.txt', 'r') as file:
        distributors = file.readlines()

    for distributor in distributors:
        distributor_data = distributor.strip().split(',')
        if distributor_data[0] == distributor_id:
            messagebox.showinfo("distributor Found",
                                f"ID: {distributor_data[0]}\n"
                                f"Name: {distributor_data[1]}\n")
            return

    messagebox.showinfo("Distributor Not Found", "Distributor not found!")


def delete_distributor():
    distributor_id = entry_search_distributor_id.get()

    with open('distributors.txt', 'r') as file:
        distributors = file.readlines()

    with open('distributors.txt', 'w') as file:
        for distributor in distributors:
            distributor_data = distributor.strip().split(',')
            if distributor_data[0] != distributor_id:
                file.write(distributor)

    messagebox.showinfo("Success", "Distributor deleted successfully!")


def update_distributor():
    distributor_id = entry_update_distributor_id.get()
    field_name = entry_update_distributor_field.get()
    new_value = entry_update_distributor_value.get()

    field_index = get_distributor_field_index(field_name)

    if field_index is None:
        messagebox.showerror("Error", "Invalid field name!")
        return

    with open('distributors.txt', 'r') as file:
        distributors = file.readlines()

    with open('distributors.txt', 'w') as file:
        for distributor in distributors:
            distributor_data = distributor.strip().split(',')
            if distributor_data[0] == distributor_id:
                if field_index == 0:
                    messagebox.showerror("Error", "Cannot update distributor ID!")
                    file.write(distributor)
                else:
                    distributor_data[field_index] = new_value
                    file.write(','.join(distributor_data) + '\n')
            else:
                file.write(distributor)

    messagebox.showinfo("Success", "Distributor updated successfully!")


def get_distributor_field_index(field_name):
    fields = ['ID', 'Name', 'Gender']
    try:
        return fields.index(field_name)
    except ValueError:
        return None


# Create the main window
window = tk.Tk()
window.title("PHARMACY MANAGEMENT SYSTEM")
window.configure(bg="grey75")

# Create the medicine section
frame_medicine = tk.LabelFrame(window, text="MEDICINE SECTION:")
frame_medicine.pack(side=tk.LEFT, padx=10, pady=10)

label_id = tk.Label(frame_medicine, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(frame_medicine)
entry_id.grid(row=0, column=1)

label_name = tk.Label(frame_medicine, text="NAME:")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(frame_medicine)
entry_name.grid(row=1, column=1)



label_weight = tk.Label(frame_medicine, text="QUANTITY:")
label_weight.grid(row=3, column=0)
entry_weight = tk.Entry(frame_medicine)
entry_weight.grid(row=3, column=1)



#label_crime = tk.Label(frame_medicine, text="DESCRIPTION:")
#label_crime.grid(row=7, column=0)
#entry_description = tk.Entry(frame_medicine)
#entry_description.grid(row=7, column=1)



label_company = tk.Label(frame_medicine, text="COMPANY:")
label_company.grid(row=10, column=0)
entry_company = tk.Entry(frame_medicine)
entry_company.grid(row=10, column=1)

label_emergency = tk.Label(frame_medicine, text="CONTACT:")
label_emergency.grid(row=11, column=0)
entry_emergency = tk.Entry(frame_medicine)
entry_emergency.grid(row=11, column=1)

#label_cell = tk.Label(frame_medicine, text="SERIAL NUMBER:")
#label_cell.grid(row=12, column=0)
#entry_cell = tk.Entry(frame_medicine)
#entry_cell.grid(row=12, column=1)

button_create_medicine = tk.Button(frame_medicine, text="CREATE MEDICINE", command=create_medicine)
button_create_medicine.grid(row=13, column=0, columnspan=2, pady=10)

button_display_medicines = tk.Button(frame_medicine, text="DISPLAY MEDICINE", command=display_medicines)
button_display_medicines.grid(row=14, column=0, columnspan=2, pady=10)

label_search_id = tk.Label(frame_medicine, text="SEARCH BY ID:")
label_search_id.grid(row=15, column=0)
entry_search_id = tk.Entry(frame_medicine)
entry_search_id.grid(row=15, column=1)

button_search_medicine = tk.Button(frame_medicine, text="SEARCH MEDICINE", command=search_medicine)
button_search_medicine.grid(row=16, column=0, columnspan=2, pady=10)

button_delete_medicine = tk.Button(frame_medicine, text="DELETE MEDICINE", command=delete_medicine)
button_delete_medicine.grid(row=17, column=0, columnspan=2, pady=10)

label_update_id = tk.Label(frame_medicine, text="UPDATE BY ID:")
label_update_id.grid(row=18, column=0)
entry_update_id = tk.Entry(frame_medicine)
entry_update_id.grid(row=18, column=1)

label_update_field = tk.Label(frame_medicine, text="FIELD TO UPDATE:")
label_update_field.grid(row=19, column=0)
entry_update_field = tk.Entry(frame_medicine)
entry_update_field.grid(row=19, column=1)

label_update_value = tk.Label(frame_medicine, text="NEW VALUE:")
label_update_value.grid(row=20, column=0)
entry_update_value = tk.Entry(frame_medicine)
entry_update_value.grid(row=20, column=1)

button_update_medicine = tk.Button(frame_medicine, text="UPDATE MEDICINE", command=update_medicine)
button_update_medicine.grid(row=21, column=0, columnspan=2, pady=10)

# Create the distributor section
frame_distributor = tk.LabelFrame(window, text="DISTRIBUTOR SECTION")
frame_distributor.pack(side=tk.LEFT, padx=10, pady=10)

label_distributor_id = tk.Label(frame_distributor, text="ID:")
label_distributor_id.grid(row=0, column=0)
entry_distributor_id = tk.Entry(frame_distributor)
entry_distributor_id.grid(row=0, column=1)

label_distributor_name = tk.Label(frame_distributor, text="DISTRIBUTOR NAME:")
label_distributor_name.grid(row=1, column=0)
entry_distributor_name = tk.Entry(frame_distributor)
entry_distributor_name.grid(row=1, column=1)



button_create_distributor = tk.Button(frame_distributor, text="CREATE DISTRIBUTORS", command=create_distributor)
button_create_distributor.grid(row=4, column=0, columnspan=2, pady=10)

button_display_distributors = tk.Button(frame_distributor, text="DISPLAY DISTRIBUTORS", command=display_distributors)
button_display_distributors.grid(row=5, column=0, columnspan=2, pady=10)

label_search_distributor_id = tk.Label(frame_distributor, text="SEARCH BY ID:")
label_search_distributor_id.grid(row=6, column=0)
entry_search_distributor_id = tk.Entry(frame_distributor)
entry_search_distributor_id.grid(row=6, column=1)

button_search_distributor = tk.Button(frame_distributor, text="SEARCH DISTRIBUTORS", command=search_distributor)
button_search_distributor.grid(row=7, column=0, columnspan=2, pady=10)

button_delete_distributor = tk.Button(frame_distributor, text="DELETE DISTRIBUTORS", command=delete_distributor)
button_delete_distributor.grid(row=8, column=0, columnspan=2, pady=10)

label_update_distributor_id = tk.Label(frame_distributor, text="UPDATE BY ID:")
label_update_distributor_id.grid(row=9, column=0)
entry_update_distributor_id = tk.Entry(frame_distributor)
entry_update_distributor_id.grid(row=9, column=1)

label_update_distributor_field = tk.Label(frame_distributor, text="FIELD TO UPDATE:")
label_update_distributor_field.grid(row=10, column=0)
entry_update_distributor_field = tk.Entry(frame_distributor)
entry_update_distributor_field.grid(row=10, column=1)

label_update_distributor_value = tk.Label(frame_distributor, text="NEW VALUE:")
label_update_distributor_value.grid(row=11, column=0)
entry_update_distributor_value = tk.Entry(frame_distributor)
entry_update_distributor_value.grid(row=11, column=1)

button_update_distributor = tk.Button(frame_distributor, text="UPDATE DISTRIBUTORS", command=update_distributor)
button_update_distributor.grid(row=12, column=0, columnspan=2, pady=10)

# Create the display area for medicines and distributer
frame_display = tk.LabelFrame(window, text="DISPLAY AREA")
frame_display.pack(side=tk.LEFT, padx=10, pady=10)

medicine_text = tk.Text(frame_display, height=26, width=44)
medicine_text.pack(side=tk.LEFT, padx=10, pady=10)

distributor_text = tk.Text(frame_display, height=26, width=44)
distributor_text.pack(side=tk.LEFT, padx=10, pady=10)


window.mainloop()