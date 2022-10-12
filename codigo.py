import os

bolsonaro = 0
lula = 0
ciro = 0
tebet = 0
soraya = 0
monark = 0



while True:
    print("*" *20)
    print(f"Votos Bolsonaro: {bolsonaro}")
    print(f"Votos Lula: {lula}")
    print(f"Votos Ciro: {ciro}")
    print(f"Votos Tebet: {tebet}")
    print(f"Votos Soraya: {soraya}")


    try:
        voto = int(input(f"Vote em um candidato: | {os.linesep} 22-Bolsonaro {os.linesep} 13-Lula {os.linesep} 12-Ciro {os.linesep} 15-Tebet {os.linesep} 44-Soraya {os.linesep} Seu Voto: "))
        if voto == 22:
            bolsonaro += 1
        elif voto == 13:
            lula += 1
        elif voto == 12:
            ciro += 1
        elif voto == 15:
            tebet += 1
        elif voto == 44:
            soraya += 1
        else:
            pass
    except:
        print("Digite o numero do candidato")
    os.system('cls')