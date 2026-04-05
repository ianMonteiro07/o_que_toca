import requests


API_KEY = "Rw54js0aQkIce16Vgi0Tps-ltATDjKBAxwEH"
BASE_URL = "https://api.setlist.fm/rest/1.0"

def buscar_ultimo_setlist(nome_banda):
    endpoint = f"{BASE_URL}/search/setlists"
    
    headers = {
        "x-api-key": API_KEY,
        "Accept": "application/json"
    }
    
    params = {
        "artistName": nome_banda,
        "p": 1 
    }

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        
        if response.status_code == 200:
            dados = response.json()
            if "setlist" in dados and len(dados["setlist"]) > 0:
                return dados["setlist"]
            else:
                return {"erro": "Nenhum show encontrado para esta banda."}
        elif response.status_code == 404:
            return {"erro": "Banda não encontrada no sistema."}
        else:
            return {"erro": f"Erro na API: {response.status_code}"}
            
    except Exception:
        return {"erro": "Erro de conexão. Verifique sua internet."}

if __name__ == "__main__":
    resultado = buscar_ultimo_setlist("Coldplay")
    print(resultado)