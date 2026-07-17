c_temps = [10, 25, 0, 38, -5, 17]
fahrenheit_temps = [c_temp * 1.8 + 32 for c_temp in c_temps if c_temp * 1.8 + 32 < 50]
print(fahrenheit_temps)