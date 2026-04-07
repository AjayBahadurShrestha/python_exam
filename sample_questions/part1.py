# Defining the data
age = 2              # int
number = "8000"      # str
weight = 56.0        # float
decision = True      # bool
repeat = "False"     # str
name = 45            # int (stored as number)

def save_customer_data():
    # We use 'w' to create/overwrite the file
    with open("customers.txt", "w") as f:
        # We must use str() for age, weight, and decision 
        # because you can only write strings to a text file.
        
        f.write(f"Name Code: {str(name)}\n")
        f.write(f"Age: {str(age)}\n")
        f.write(f"ID Number: {number}\n") # Already a string
        f.write(f"Weight: {str(weight)}\n")
        f.write(f"Decision Made: {str(decision)}\n")
        f.write(f"Repeat Customer: {repeat}\n") # Already a string

    print("Data saved successfully to customers.txt")

# Run the function
save_customer_data()