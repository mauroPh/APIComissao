from fastapi import FastAPI
from pydantic import BaseModel

class Pedido(BaseModel):
        vendedor : str
        mes: int
        valor: float
        qnt_vendas : int

app = FastAPI()


@app.get("/")
async def home():
    return {"Calcula comissão de vendedores"}

@app.post("/calcular", status_code=201)
async def insere_pedidos(pedido: Pedido): #Comissao adicional por atingir meta
    mes=pedido.mes
    if pedido.qnt_vendas >= 5 and mes == 1 or mes == 5:
        comissao_mes = pedido.valor * 0.03
    elif pedido.qnt_vendas >= 3 and mes == 2:
        comissao_mes = pedido.valor * 0.03
    elif pedido.qnt_vendas >= 2 and mes == 3 or mes == 4 or mes == 8 or mes == 12:
        comissao_mes = pedido.valor * 0.03
    elif pedido.qnt_vendas >= 4 and mes == 9 or mes == 10:
        comissao_mes = pedido.valor * 0.03
    elif pedido.qnt_vendas >= 60 and mes == 6:
        comissao_mes = pedido.valor * 0.03
    elif pedido.qnt_vendas >=7 and mes == 11:
        comissao_mes = pedido.valor * 0.03
    else:
            comissao_mes = 0



    if pedido.valor <= 300.00:
        comissao_por_quantidade = pedido.valor * 0.01
        calculo_comissao = comissao_por_quantidade + comissao_mes
        return ("O valor da comissão será: R$", calculo_comissao)

    if pedido.valor > 300.00 and pedido.valor <= 1000.00:
        comissao_por_quantidade = pedido.valor * 0.03
        calculo_comissao = comissao_por_quantidade + comissao_mes
        return ("O valor da comissão será: R$", calculo_comissao)

    if pedido.valor > 1000.00:
        comissao_por_quantidade = pedido.valor * 0.05
        calculo_comissao = comissao_por_quantidade + comissao_mes
        return ("O valor da comissão será: R$", calculo_comissao)
