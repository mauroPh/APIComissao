from Tools.scripts.dutree import display
from fastapi import FastAPI
import pandas as pd


app = FastAPI()

vendedor1 = 0
comissao = {
    for (Pedidos[vendedor:1]){
        vendedor1 = sum(Pedidos["valor"])
    }

}

calcula_comissao = {

}
Pedidos = {
     {"vendedor": 1, "data": "2022-03-01", "valor": 500.34},
     {"vendedor": 1, "data": "2022-03-01", "valor": 1000.22},
     { "vendedor": 1, "data": "2022-03-01", "valor": 100.35},
     {"vendedor": 1, "data": "2022-03-01", "valor": 100.35},
     {"vendedor": 1, "data": "2022-03-01", "valor": 100.35},
     {"vendedor": 1, "data": "2022-03-01", "valor": 22.34},
     {"vendedor": 1, "data": "2022-04-01", "valor": 5000.34 },
     {"vendedor": 2, "data": "2022-03-01", "valor": 2000.34 },
     {"vendedor": 2, "data": "2022-04-01", "valor": 3000.34 },
     {"vendedor": 3, "data": "2022-03-01", "valor": 500.34},
     {"vendedor": 3, "data": "2022-03-01", "valor": 1000.22},
     {"vendedor": 4, "data": "2022-03-01", "valor": 100.35 },
     {"vendedor": 4, "data": "2022-03-01", "valor": 22.34 },
     {"vendedor": 3, "data": "2022-04-01", "valor": 5000.34 },
     {"vendedor": 2, "data": "2022-03-01", "valor": 2000.34 },
     {"vendedor": 2, "data": "2022-04-01", "valor": 3000.34 },


}
pedidos_df = pd.DataFrame(Pedidos)


@app.get("/")
async def home():
    return {"Calcula comissão de vendedores"}

@app.get("/pedidos/{id_pedidos}")
async def pegar_pedidos(id_pedidos: int):
        if id_pedidos in Pedidos:
           return Pedidos[id_pedidos]
        else:
            return{ "Erro":"ID pedidos inexistente"}

@app.post("/comissoes", status_code=201)
async def insere_pedidos(pedidos: str):
         return {"pedidos"}