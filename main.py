import requests
import json
from bs4 import BeautifulSoup

LOG_IN = "https://trading.portfoliopersonal.com/LogIn"
BONOS_URL = "https://api.portfoliopersonal.com/api/Cotizaciones/WatchList/RentaFija?cotizacionSimplificada=true&esLetra=false&idTipoPlazoLiquidacion=3&watchListId=12967"
BONOS_DEFAULT_URL = "https://api.portfoliopersonal.com/api/Cotizaciones/WatchList/RentaFija?cotizacionSimplificada=true&esLetra=false&idTipoPlazoLiquidacion=3&watchListId=29005"
CORPORATIVOS_URL = "https://api.portfoliopersonal.com/api/Cotizaciones/WatchList/RentaFija?cotizacionSimplificada=true&esLetra=false&idTipoPlazoLiquidacion=3&watchListId=12941"
CEDEARS_USD_URL = "https://api.portfoliopersonal.com/api/Cotizaciones/WatchList/21115?busquedaCompleta=false&cotizacionSimplificada=true&plazoId=3"
CEDEARS_ARS_URL = "https://api.portfoliopersonal.com/api/Cotizaciones/WatchList/21114?busquedaCompleta=false&cotizacionSimplificada=true&plazoId=3"

def logInAndGetHeaders():
    credentials = {
        "TxtUsername": "",
        "TxtPassword": "",
        "BtnLogin": "Ingresar"
    }

    session = requests.Session()
    login = session.get(LOG_IN)
    soup = BeautifulSoup(login.content)
    viewState = soup.find('input', { "name": "__VIEWSTATE" })['value']
    eventValidation = soup.find('input', { "name": "__EVENTVALIDATION" })['value']

    credentials["__VIEWSTATE"] = viewState
    credentials["__EVENTVALIDATION"] = eventValidation

    response = session.post(LOG_IN, data=credentials)
    cookie = json.loads(session.cookies['PPTA'])
    bearer = cookie['pptk']

    headers = {
        "Authorization": f"Bearer {bearer}",
        "clientKey": "pp123456",
        "authorizedClient": "191202"
    }

    return headers

def main():
    headers = logInAndGetHeaders()

    response = session.get(BONOS, headers=headers)
    print(response.content)

if __name__ == '__main__':
    main()