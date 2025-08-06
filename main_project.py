from convert import celsius_to_fahrenheit, fahrenheit_to_celsius

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose a conversion (1 or 2): ")

if choice == "1":
    try:
        celcius = float(input("Enter temperature in Celsius: "))

        fahrenheit = celsius_to_fahrenheit(celcius)

        print(f"{celcius}°C is equal to {fahrenheit}°F")

    except ValueError:
        print("Invalid input. Please enter a number.")

elif choice == "2":
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        celsius = fahrenheit_to_celsius(fahrenheit)

        print(f"{fahrenheit}°F is equal to {celsius}°C")

    except ValueError:
        print("Invalid input. Please enter a number.")  

else:
    print("Invalid choice. Please select 1 or 2.")





