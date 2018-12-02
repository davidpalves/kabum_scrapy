# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KabumItem(scrapy.Item):
    url = scrapy.Field()
    nome = scrapy.Field()
    descricao = scrapy.Field()
    categoria = scrapy.Field()
    marca = scrapy.Field()
    navegacao = scrapy.Field()
    nome_vendedor = scrapy.Field()
    preco_normal = scrapy.Field()
    preco_disconto = scrapy.Field()
    imagem_principal = scrapy.Field()
    imagens_secundarias = scrapy.Field()
    caracteristicas = scrapy.Field()

