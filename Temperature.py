import matplotlib.pyplot as plt

# Task 1
temperatures  = [2,5,6,8,9,10,12,16,18,14,7,8,9.5,11,17,12.5,5.5,]
comfortable_temp = []
mid_temp = []
cold_temp = []


for temp in temperatures:
    if temp < 10:
        cold_temp.append(temp)
    elif 10 <= temp < 15:
        mid_temp.append(temp)
    elif 15 <= temp < 20:
        comfortable_temp.append(temp)

print("Cold Temoerature",cold_temp)
print("Mid Temperature : ",mid_temp)
print("Comfortable Temp :" ,comfortable_temp)

# Task 2
print("Cold temperatures count:", len(cold_temp))
print("Mild temperatures count:", len(mid_temp))
print("Comfortable temperatures count:", len(comfortable_temp))

# Task 3
temperatures_fahrenheit =[]
for Celsius in temperatures:
    Fahrenheit = (Celsius *(9/5)) + 32
    temperatures_fahrenheit.append(Fahrenheit)
print("Fahrenheit values :" , temperatures_fahrenheit)



# Task 4
night_temperatures = []  # 00-08
evening_temperatures = []  # 08-16
day_temperatures = []  # 16-24

for i, temp in enumerate(temperatures):
    if i < 8:  # Night (positions 0-7)
        night_temperatures.append(temp)
    elif i < 16:  # Evening (positions 8-15)
        evening_temperatures.append(temp)
    else:  # Day (positions 16-24)
        day_temperatures.append(temp)

print("Night Temperatures:", night_temperatures)
print("Evening Temperatures:", evening_temperatures)
print("Day Temperatures:", day_temperatures)

if day_temperatures:  # Avoid division by zero
    avg_day_temp = sum(day_temperatures) / len(day_temperatures)
    print("Average Day Temperature:", avg_day_temp)

time_labels = ['Night'] * len(night_temperatures) + ['Evening'] * len(evening_temperatures) + ['Day'] * len(day_temperatures)
all_temps = night_temperatures + evening_temperatures + day_temperatures

plt.figure(figsize=(8, 5))
plt.plot(time_labels, all_temps, marker='o', linestyle='-', color='b')
plt.title("Day vs. Temperature")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()
