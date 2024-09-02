import matplotlib.pyplot as plt
from index import weather

city = input("Digite uma cidade: ")

temps, dates = weather(city)

def handleGraphic(chart_type, **kwargs):
    fig, ax = plt.subplots()

    method = getattr(ax, chart_type)
    method(dates, temps, **kwargs)

    ax.set(xlabel='Dias da semana', ylabel='Temperatura (°C)', title=f"Clima para {city}")
    plt.show()
   
while True: 
  chart_type = input("Selecione o tipo de gráfico: \n 01-Gráfico de Linha \n 02-Gráfico de Barra \n 03-Gráfico de Haste \n 04-Sair \n Sua resposta: ")


  if chart_type == "01":
       handleGraphic('plot', marker = 'o')
  elif chart_type == "02":
      handleGraphic('bar', width=1, edgecolor="white", linewidth=0.7)
  elif chart_type == "03":
      handleGraphic('stem')
  elif chart_type == "04":
       print("Saindo...")
       break
  else:
       print("Opção inválida, tente novamente.")