import numpy as np

participantes = [
    {
        "nome": "Cassandra",

        "localizacao": "Brasil",

        "sonho": "Ser atriz.",

        "interesses": ["Teatro", "Relações Internacionais"]
    },

    {
        "nome": "José",

        "localizacao": "Brasil",

        "sonho": "Salvar os corais marinhos.",

        "interesses": ["Biologia", "Oceania"]
    },

    {
        "nome": "Charlie",

        "localizacao": "Inglaterra",

        "sonho": "Conhecer o mundo.",

        "interesses": ["Relações internacionais", "Gastronomia"]
    },

    {
        "nome": "Alberta",

        "localizacao": "Alemanha",

        "sonho": "ser professora.",

        "interesses": ["Letras Frânces", "Música"]
    },

    {
        "nome": "Rowan",

        "localizacao": "Noruegua",

        "sonho": "Salvar vidas.",

        "interesses": ["Medicina", "Enfermagem"]
    },

    {
        "nome": "Sr. Branco",

        "localizacao": "Camarões",

        "sonho": "Não morrer.",

        "interesses": ["Química", "Direito"]
    },

    {
        "nome": "Fátima Lacraia",

        "localizacao": "Brasil",

        "sonho": "Não ser comida.",

        "interesses": ["Engenharia de alimentos", "Gastronomia"]
    },

    {
        "nome": "Jefferson",

        "localizacao": "Uruguai",

        "sonho": "Ser famoso.",

        "interesses": ["Relações internacionais", "Gastronomia"]
    },

    {
        "nome": "Carlota",

        "localizacao": "Suiça",

        "sonho": "Ser mestre queijeira.",

        "interesses": ["Medicina veterinária", "Gastronomia"]
    } 
]

regioes = set(participante["localizacao"] for participante in participantes)

sonhos = {}

for participante in participantes:

    sonho = participante["sonho"]

    if sonho not in sonhos:

        sonhos[sonho] = []

    sonhos[sonho].append(participante["nome"])

areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])

interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)

area_mais_popular = interesses_unicos[np.argmax(contagem)]

print("Regiões dos participantes:\n", '\n'.join(regioes))

print("Sonhos dos participantes:")

for sonho, nomes in sonhos.items():

    print(f"{' '.join(nomes)}: {(sonho)}")

print("Área de interesse mais popular:", area_mais_popular)