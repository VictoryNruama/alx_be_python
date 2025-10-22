# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
try:
    temp_input = input("Enter the temperature value: ").strip()
    temperature = float(temp_input)  # validate numeric input
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if unit == "c":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted:.2f}°F.")
    elif unit == "f":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted:.2f}°C.")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
