from fastapi import FastAPI, Request

app = FastAPI()

planta = [
    {
        'umidade': 60,
        'temperatura': 30,
        'vazao': 40,
    }
]

resultado = [
    {
        'duracao': 0
    }
]


@app.get("/planta")
async def get():
    return {'planta': planta}


@app.put("/plantanova")
async def put(info: Request):
    req_info = await info.json()
    print(req_info)
    novo = req_info
    planta[0] = novo
    return {'Alterado': planta}

@app.get("/resultado")
async def get():
    return {'resultado': resultado}


@app.put("/resultadonovo")
async def put(info: Request):
    req_info = await info.json()
    print(req_info)
    novo = req_info
    resultado[0] = novo
    return {'Alterado': resultado}