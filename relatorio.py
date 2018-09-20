# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# Uma ferramenta geradora de relatório

import psycopg2
import time


DBNAME = "news"


# consultado: https://stackoverflow.com/a/26005077
def artigos_mais_populares():
    """Mostra os três artigos mais populares de todos os tempos."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from artigos_mais_populares")
    artigos = c.fetchall()
    db.close()

    texto = "Os três artigos mais populares de todos os tempos:\n"
    for i in artigos:
        texto += "%-35s -- %-10s visualizações\n" % (i[0], i[1])
    texto += "\n\n"
    return texto


def autores_mais_populares():
    """Mostra os autores de artigos mais populares de todos os tempos."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from autores_mais_populares")
    autores = c.fetchall()
    db.close()

    texto = "Os autores de artigos mais populares de todos os tempos:\n"
    for i in autores:
        texto += "%-35s -- %-10s visualizações\n" % (i[0], i[1])
    texto += "\n\n"
    return texto


def dias_com_mais_de_1_por_cento_de_erros():
    """Mostra quais dias têm mais de 1% das requisições resultaram em erros."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from dias_com_mais_de_1_por_cento_de_erros")
    dias = c.fetchall()
    db.close()

    texto = "Quais dias têm mais de 1% das requisições com erros:\n"
    for i in dias:
        texto += "%-35s -- %-10.3s erros\n" % (i[0], i[1])
    texto += "\n\n"
    return texto


def main():
    """Escreve no arquivo de texto o relatório."""
    print("Escrevendo relatório...\n")
    relatorio = open("relatorio.txt", "w")

    relatorio.write("Relatório de Análise de Log - Escrito: " +
                    time.ctime() + "\n\n")
    relatorio.write(artigos_mais_populares())
    relatorio.write(autores_mais_populares())
    relatorio.write(dias_com_mais_de_1_por_cento_de_erros())

    relatorio.close()
    print("O relatório está pronto! Veja o arquivo relatorio.txt")


if __name__ == "__main__":
    main()
