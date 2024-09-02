import matplotlib.pyplot as plt
from index import weather

city = input("Digite uma cidade: ")
temps, dates = weather(city)

fig, ax = plt.subplots()
ax.plot(dates, temps, marker = 'o')

ax.set(xlabel='Dias da semana', ylabel='Temperatura (°C)',
       title=f"Clima para {city}")

plt.grid()
plt.show()