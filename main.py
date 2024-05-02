import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("BasePokemon.xlsx")

@app.router("/")
def Principal():
  return "Esta es una Api que muestra pokemons"


@app.router("/Por_Numero/<Numero>")
def PorNumero(Numero):
  base[base["Numeros"]==Numero]
  respuesta=f"El pokemon {Numero} es {fila.loc[:,´Nombre]}"
  return respuesta 

@app.router("/Por_Tipo/<Tipo>")
def PorTipo(Tipo):
  resultados=base[base[Tipo]==Tipo ]
  resultado=str(resultados)
  return resultados

@app.router("/Por_Peso/<Peso1>/<Peso2>")
def PorPeso(Peso1 ,Peso2):
  resultados=base[(base["Peso"]>Peso1) & (base["Peso"]<Peso2)]
  resultados=str(resultados)
  return resultados

print(PorPeso(30))

if __name__=="__main__":
  app.run()



