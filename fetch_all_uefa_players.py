import json
import os
import re
import urllib.request

# Le 55 Nazionali UEFA
UEFA_TEAMS = {
    "ALB": "Albania", "AND": "Andorra", "ARM": "Armenia", "AUT": "Austria",
    "AZE": "Azerbaigian", "BEL": "Belgio", "BLR": "Bielorussia", "BIH": "Bosnia ed Erzegovina",
    "BUL": "Bulgaria", "CYP": "Cipro", "CRO": "Croazia", "DEN": "Danimarca",
    "EST": "Estonia", "FIN": "Finlandia", "FRA": "Francia", "WAL": "Galles",
    "GEO": "Georgia", "GER": "Germania", "GIB": "Gibilterra", "GRE": "Grecia",
    "ENG": "Inghilterra", "IRL": "Irlanda", "NIR": "Irlanda del Nord", "ISL": "Islanda",
    "FRO": "Isole Fær Øer", "ISR": "Israele", "ITA": "Italia", "KAZ": "Kazakistan",
    "KOS": "Kosovo", "LVA": "Lettonia", "LIE": "Liechtenstein", "LTA": "Lituania",
    "LUX": "Lussemburgo", "MKD": "Macedonia del Nord", "MLT": "Malta", "MDA": "Moldavia",
    "MNE": "Montenegro", "NOR": "Norvegia", "NED": "Paesi Bassi", "POL": "Polonia",
    "POR": "Portogallo", "CZE": "Repubblica Ceca", "ROU": "Romania", "RUS": "Russia",
    "SMR": "San Marino", "SCO": "Scozia", "SRB": "Serbia", "SVK": "Slovacchia",
    "SVN": "Slovenia", "ESP": "Spagna", "SWE": "Svezia", "SUI": "Svizzera",
    "TUR": "Turchia", "UKR": "Ucraina", "HUN": "Ungheria"
}

def pulisci_nome(testo):
    testo = testo.lower()
    testo = re.sub(r'[àáâãäå]', 'a', testo)
    testo = re.sub(r'[èéêë]', 'e', testo)
    testo = re.sub(r'[ìíîï]', 'i', testo)
    testo = re.sub(r'[òóôõö]', 'o', testo)
    testo = re.sub(r'[ùúûü]', 'u', testo)
    testo = re.sub(r'[cç]', 'c', testo)
    testo = re.sub(r'[ñ]', 'n', testo)
    testo = re.sub(r'[^\w\s]', '', testo)
    testo = re.sub(r'\s+', '_', testo)
    return testo

def genera_dati():
    print("⏳ Generazione rose per tutte le 55 nazionali UEFA in corso...")
    
    players_db = {}
    rosters_db = {code: [] for code in UEFA_TEAMS.keys()}
    
    for code, country_name in UEFA_TEAMS.items():
        # Genera una rosa da 23 giocatori per ogni nazione
        squadra = []
        for i in range(1, 24):
            if i <= 3:
                ruolo = "POR"
                nome = f"Portiere {i}"
            elif i <= 10:
                ruolo = "DIF"
                nome = f"Difensore {i-3}"
            elif i <= 18:
                ruolo = "CEN"
                nome = f"Centrocampista {i-10}"
            else:
                ruolo = "ATT"
                nome = f"Attaccante {i-18}"
            squadra.append({"name": f"{nome} ({country_name})", "pos": ruolo})

        for p in squadra:
            p_id = f"{puli_nome(p['name'])}_{code.lower()}"
            rosters_db[code].append(p_id)
            players_db[p_id] = {
                "name": p["name"],
                "pos": p["pos"],
                "nat": country_name
            }

    os.makedirs("data", exist_ok=True)
    
    with open("data/players.json", "w", encoding="utf-8") as f:
        json.dump(players_db, f, ensure_ascii=False, indent=2)
        
    with open("data/rosters.json", "w", encoding="utf-8") as f:
        json.dump(rosters_db, f, ensure_ascii=False, indent=2)

    print(f"✅ Completato! Creati {len(players_db)} giocatori su 55 Nazionali.")

def puli_nome(t):
    return pulisci_nome(t)

if __name__ == "__main__":
    genera_dati()