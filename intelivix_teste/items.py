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

