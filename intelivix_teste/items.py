# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KabumItem(scrapy.Item):
    url = scrapy.Field() 				# Url do produto sendo extraído
    name = scrapy.Field() 				# Nome do produto
    description = scrapy.Field()			# Texto contendo a descrição do produto
    category = scrapy.Field()			# Categoria em que o produto se enquadra
    brand = scrapy.Field()				# Marca do produto
    navigation = scrapy.Field() 			# (string list) Lista de categorias e subcategorias de navegação, indo do mais geral para mais específico
    current_price = scrapy.Field() 				# (float) Valor atual do produto
    old_price = scrapy.Field() 		# (float) Valor do produto sem desconto, se houver
    discount_price = scrapy.Field() 		# (float) Valor do produto sem desconto, se houver
    main_image = scrapy.Field() 	# (string) URL da imagem do produto
    secondary_images = scrapy.Field()# (string list) Lista de URL das imagens secundárias
    features = scrapy.Field() 	# (list dict) Lista de dicionários contendo as caracteristicas do produto Ex.: [{'name': 'Cor', 'value': 'Preto'}]

