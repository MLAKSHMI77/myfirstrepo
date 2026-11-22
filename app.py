def analyze_temperatures(temps_celsius):
    """Converts a list of Celsius temperatures to Fahrenheit and checks for warm days."""
    warm_days = []
    
    for temp in temps_celsius:
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is {fahrenheit:.1f}°F")
        
        if temp >= 25:
            warm_days.append(temp)
            
    return warm_days

# Sample data
weekly_temps = [21, 24, 27, 29, 22, 19, 26]

# Run the function
hot_days = analyze_temperatures(weekly_temps)
print(f"\nNumber of warm days (25°C or above): {len(hot_days)}")
