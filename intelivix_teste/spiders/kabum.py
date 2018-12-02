# -*- coding: utf-8 -*-
import scrapy
from intelivix_teste.items import KabumItem

produto = str(input("Digite o produto a ser buscado: "))

class KabumSpider(scrapy.Spider):
    name = 'kabum'
    url = str('https://www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?ordem=5&limite=100&pagina=1&string='+produto)
    # allowed_domains = [url]
    start_urls = [url]

    def parse(self, response):
        pages = response.xpath('//div[@class="listagem-box"]/div[@class="listagem-titulo_descr"]/span[@class="H-titulo"]/a')

        for page in pages:
            yield response.follow(page, callback=self.parse_item)

        next_page_container = response.xpath('//div[@class="listagem-paginacao"]/form/table/tr/td/a[contains(text(),"Proxima")]')
        if len(next_page_container) > 0:
            yield response.follow(next_page_container[0], callback=self.parse)




    def parse_item(self, response):
        item = KabumItem()

        item['url'] = response.url
            
        item['nome'] = response.xpath('//div[@id="titulo_det"]/h1[@class="titulo_det"]/text()').extract_first()

        item['descricao'] = response.xpath('//p[contains(@itemprop,"description")]/text()').extract_first()

        item['categoria'] = response.xpath('//h2[@class="h2titcategoria"]/text()').extract_first()

        try:
            item['marca'] = response.xpath('//p[contains(text(),"Marca:")]/text()').extract_first().split(':')[1].strip()
        except AttributeError:
            self.logger.debug('Falha ao extrair marca em %s', response.url)
            pass

        item['navegacao'] = [li.split('>')[0].strip() for li in response.xpath('//ol[contains(@itemtype,"http://schema.org/BreadcrumbList")]/li/a/text()').extract()]

        item['nome_vendedor'] = 'Kabum eletronicos'

        precos = {
            'preco_normal': response.xpath('//div[@class="preco_normal"]/text()').re(r'\d*\.*\d+\,\d+'),
            'preco_disconto': response.xpath('//span[@class="preco_desconto"]/span/span/strong/text()').re(r'\d*\.*\d+\,\d+')
        }

        for key in precos.keys():
            if len(precos[key]) > 0:
                item[key] = float(precos[key][0].replace('.','').replace(',','.'))
            else:
                self.logger.debug('{} not found on %s'.format(key), 
                    response.url)  

        imagens = response.xpath('//ul[@id="imagens-carrossel"]/li/img/@src')
        item['imagem_principal'] = imagens.extract_first()
        item['imagens_secundarias'] = imagens.extract()[1:]

        caracteristicas = []
        for carac in response.xpath('//div[@class="content_tab"]/p/text()').re(r'\w+\:[\s\S]*'):
            nome = carac.split(':')[0].strip()
            valor = carac.split(':')[1].strip()
            caracteristicas.append({'nome':nome, 'valor':valor})
        
        item['caracteristicas'] = caracteristicas

        yield item
