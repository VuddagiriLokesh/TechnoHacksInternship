def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

choice = input("Enter '1' to convert Fahrenheit to Celsius, or '2' to convert Celsius to Fahrenheit: ")

if choice == '1':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
elif choice == '2':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
else:
    print("Invalid choice. Please enter 1 or 2.")
