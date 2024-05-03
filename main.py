import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("nacimiento.xlsx")

@app.router("/")
def Principal():
  return "Esta es una Api que muestra informacion personal"


@app.router("/Por_Nombre/<Nombre>")
def PorNombre(Nombre):
  base[base["Nombre"]==Nombre]
  respuesta=f"Se llama {Nombre} es {fila.loc[:,´Nombre]}"
  return respuesta

@app.router("/Por_Edad/<Edad>")
def PorEdad(Edad):
  resultados=base[base[Edad]==Edad ]
  resultado=str(resultados)
  return resultados


@app.router("/Por_Genero/<Edad>")
def PorGenero(Genero):
  resultados=base[base[Genero]==Genero ]
  resultado=str(resultados)
  return resultados


if __name__=="__main__":
  app.run()

