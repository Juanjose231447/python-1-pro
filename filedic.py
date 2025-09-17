None
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            "NTP": "no te preocupes",
            "BNO": "bueno"
                }
for i in range(8):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print (meme_dict[word])
    else:
        print ("esa palabra no la tengo bro si quieres busca otra en el diccionario te pasas de rozca")
