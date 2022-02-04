#!/usr/bin/env python
# coding: utf-8
import pandas as pd


def Peliculas_JSON(file_1):
    """
    input: ubicacion del archivo txt
    Convierte el archivo txt a json
    """
    df = pd.read_table(file_1, sep="|")
    df.head()
    df.to_json("peliculas.json",orient="records")


Peliculas_JSON("peliculas.txt")






