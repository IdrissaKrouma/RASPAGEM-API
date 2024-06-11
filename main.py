import os 
import json
import shutil
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
import schedule
import time

# def job() :
#         chemin_actuel = os.getcwd()
#         nouveau_chemin = os.path.abspath(os.path.join(chemin_actuel, os.pardir))
#         nouveau_chemin_script = os.path.join(nouveau_chemin, "Scrapy_Brvm")
#         os.chdir(nouveau_chemin_script)
#         chemin_script_shell = './scrapy.sh'
#         try:
#             subprocess.run(['sh',chemin_script_shell], check=True)
#             print("Script shell exécuté avec succès.")
#         except subprocess.CalledProcessError as e:
#             print("Erreur lors de l'exécution du script shell:", e)

#         chemin_actuel = os.getcwd()
#         nouveau_chemin = os.path.abspath(os.path.join(chemin_actuel, os.pardir))
#         nouveau_chemin_script = os.path.join(nouveau_chemin, "app")
#         os.chdir(nouveau_chemin_script)

def job():
    chemin_actuel = os.getcwd()
    print(f"Répertoire actuel: {chemin_actuel}")

    nouveau_chemin_script = os.path.join(chemin_actuel, "scrapy_app")

    if not os.path.isdir(nouveau_chemin_script):
        raise FileNotFoundError(f"Le répertoire spécifié est introuvable : {nouveau_chemin_script}")

    os.chdir(nouveau_chemin_script)
    print(f"Changé de répertoire pour : {nouveau_chemin_script}")

    chemin_script_shell = './scrapy.sh'

    if not os.path.isfile(chemin_script_shell):
        raise FileNotFoundError(f"Le fichier spécifié est introuvable : {chemin_script_shell}")
    
    with open(chemin_script_shell, 'r') as file:
        lignes_script_shell = file.readlines()

    try:
        for ligne in lignes_script_shell:
            subprocess.run(ligne.strip(), shell=True, check=True)
        # subprocess.run(chemin_script_shell, shell=True, check=True)
        print("Script shell exécuté avec succès.")
    except subprocess.CalledProcessError as e:
        print("Erreur lors de l'exécution du script shell:", e)

    chemin_actuel = os.getcwd()
    nouveau_chemin = os.path.abspath(os.path.join(chemin_actuel, os.pardir))

    print(f"Changé de répertoire pour : {nouveau_chemin}")



schedule.every(10).minutes.do(job)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return {'hello world is me the inventor !'}

@app.get("/actions")
async def read_item():
    try:
        job()
        with open("../scrapy_app/top5_data.json", "r") as file:
            data = json.load(file)
        if not data:
            raise HTTPException(status_code=400, detail="JSON data is empty")
        top5_json = data[0].get("top5")
        if top5_json is None:
            raise HTTPException(status_code=400, detail="Expected key 'top5' not found")
        return {"top5": top5_json}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format")
    except KeyError:
        raise HTTPException(status_code=400, detail="Expected key not found in JSON")

@app.get("/actions/{action_id}")
async def read_item(action_id:int):
    try:
        job()
        with open("../scrapy_app/top5_data.json", "r") as file:
            data = json.load(file)
        if not data:
            raise HTTPException(status_code=400, detail="JSON data is empty")
        top5_json = data[0].get("top5")
        if top5_json is None:
            raise HTTPException(status_code=400, detail="Expected key 'top5' not found")
        return {"action": top5_json[action_id-1]}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format")
    except KeyError:
        raise HTTPException(status_code=400, detail="Expected key not found in JSON")

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)