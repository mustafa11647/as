from tkinter import *

def calculate_interest():
  """
  Calculates and displays simple and compound interest
  """
  try:
    principal = float(principal_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get()) / 100  # Convert percentage to decimal

    # Calculate Simple Interest
    simple_interest = principal * rate * time

    # Calculate Compound Interest (assuming annual compounding)
    amount = principal * (1 + rate) ** time
    compound_interest = amount - principal

    # Display results
    simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")

  except ValueError:
    # Handle invalid inputs
    message = "Please enter valid numbers for Principal, Time, and Rate."
    error_label.config(text=message, foreground="red")

# Create the main window
window = Tk()
window.title("Interest Calculator")

# Create labels and entry fields for user input
principal_label = Label(window, text="Principal Amount:")
principal_label.grid(row=0, column=0, pady=5)

principal_entry = Entry(window)
principal_entry.grid(row=0, column=1, pady=5)

time_label = Label(window, text="Time Period (Years):")
time_label.grid(row=1, column=0, pady=5)

time_entry = Entry(window)
time_entry.grid(row=1, column=1, pady=5)

rate_label = Label(window, text="Rate of Interest (%):")
rate_label.grid(row=2, column=0, pady=5)

rate_entry = Entry(window)
rate_entry.grid(row=2, column=1, pady=5)

# Create a button to trigger calculation
calculate_button = Button(window, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, columnspan=2, pady=10)

# Create labels to display results
simple_interest_label = Label(window, text="")
simple_interest_label.grid(row=4, columnspan=2)

compound_interest_label = Label(window, text="")
compound_interest_label.grid(row=5, columnspan=2)

# Create an error label for invalid inputs
error_label = Label(window, text="")
error_label.grid(row=6, columnspan=2)

# Run the main event loop
window.mainloop()
