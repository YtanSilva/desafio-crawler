from dataclasses import dataclass


#Criando estrutura do objeto
@dataclass
class Movie:
    title: str
    year: str
    duration: str
    pg: str
    rating: str
    url: str