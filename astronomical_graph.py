import matplotlib.pyplot as plt

# data([공전 주기(년), 평균 거리(AU)])
planet_data = {
    "Mercury": [0.24, 0.39],
    "Venus": [0.62, 0.72],
    "Earth": [1.0, 1.0],
    "Mars": [1.88, 1.52],
    "Jupiter": [11.86, 5.20],
    "Saturn": [29.46, 9.58],
    "Uranus": [84.01, 19.18],
    "Neptune": [164.8, 30.07]
}

periods = []
distances = []
for planet, data in planet_data.items():
    period, distance = data
    periods.append(period)
    distances.append(distance)

plt.scatter(periods, distances, label='Planets')

for i in range(len(periods) - 1):
    plt.plot([periods[i], periods[i+1]], [distances[i], distances[i+1]], 'b-')

plt.xlabel('revolution period (unit: Year)')
plt.ylabel('distances from the sun to the planet (단위:AU)')
plt.title("The graph of each planet of solar system's the revolution period which is associated with its distances as the Linear function")
plt.grid(True)
plt.legend()
plt.show()
print("1AU = 149,597,870.7 km (distances from sun to the earth.), about 0.15 billion killometers.")
time = 149597870.7
for planet, data in planet_data.items():    per, dis = data
    print(f"[ {planet} ]: A cycle of revolve : {per} year(s) | distance from the sun: {dis}AU -> {round(dis * time, 2)} km")
