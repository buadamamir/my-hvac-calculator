
import math

def calculate_cable_thickness():
    # Define a dictionary that maps cable types to their resistivity values
    resistivity_values = {
        "copper": 1.68e-8,
        "aluminum": 2.82e-8
    }

    # Define a dictionary that maps cable types to their maximum current carrying capacities
    current_capacity_values = {
        "copper": 16,
        "aluminum": 12
    }

    # Get the cable type from the user
    cable_type = input("Enter the cable type (copper or aluminum): ")

    # Get the length of the cable from the user
    length_of_cable = float(input("Enter the length of the cable (in meters): "))

    # Get the amount of current consumed from the user
    amount_of_current_consumed = float(input("Enter the amount of current consumed (in amperes): "))

    # Get the resistivity value for the given cable type
    resistivity = resistivity_values[cable_type]

    # Get the maximum current carrying capacity for the given cable type
    current_capacity = current_capacity_values[cable_type]

    # Calculate the radius of the cable
    radius = math.sqrt((resistivity * length_of_cable * amount_of_current_consumed) / (0.5 * math.pi * current_capacity))

    # Return the radius of the cable
    return radius

# Example usage
cable_thickness = calculate_cable_thickness()

print("The thickness of the cable you should use is:", round(cable_thickness * 1000, 2), "mm")
