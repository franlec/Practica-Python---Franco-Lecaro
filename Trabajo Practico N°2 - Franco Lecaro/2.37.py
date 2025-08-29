hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def hashtagsMasUsados (tendencias,cantidad):
    hashtags_mas = []
    for hashtag, vecesUtilizado in tendencias:
        if vecesUtilizado >= cantidad:
            hashtags_mas.append(hashtag)
    if not hashtags_mas:
        return print("Ningun hastag fue utilizado mas de ", cantidad, "veces")
    return hashtags_mas

print(hashtagsMasUsados(tendencias,190))


