# Scraping Kabum site

#### Projeto feito para processo seletivo da Intelivix

Site escolhido: www.kabum.com.br/

------------------------------------------------------

#### Links para instruções do projeto
* [Requerimentos do Projeto](https://github.com/DavidPierre21/kabum_scrapy#requerimentos-para-o-projeto)
* [Configuração do MongoDB](https://github.com/DavidPierre21/kabum_scrapy#configurando-mongodb)
* [Execução do projeto](https://github.com/DavidPierre21/kabum_scrapy#instru%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-projeto)
* [Tempo despendido](https://github.com/DavidPierre21/kabum_scrapy#tempo-gasto)

------------------------------------------------------

#### Requerimentos para o projeto
1. [Python 3](https://www.python.org/)
2. [Mongodb](https://www.mongodb.com/)
3. [Pymongo](https://api.mongodb.com/python/current/)
4. [Scrapy](https://scrapy.org/)

------------------------------------------------------

#### Configurando MongoDB
O projeto usa um database chamado "kabum" e uma collections chamado "produtos"
O servidor do database esta configurado para o localhost e na porta 27017

Antes de tudo, o serviço do MongoDB deve estar rodando, no Linux, utilize:
```
sudo service start mongod
```

Caso queira verificar o status do serviço
```
sudo service status mongod
```

--------------------------------------------------------
Para abrir o shell do Mongo, podemos utilizar:

```
mongo
```

ou, para o modo "silencioso"
```
mongo --quiet
```

Para selecionar o database a ser utilizado
```
use kabum;
```

Crie a collection produtos:
```
db.createCollection("produtos");
```

#### [Depois de executar a spider, para visualizar o dataset, utilize o comando:](https://github.com/DavidPierre21/kabum_scrapy#instru%C3%A7%C3%B5es-para-execu%C3%A7%C3%A3o-do-projeto)
```
db.produtos.find();
```

e caso queira exportar para json, fora do shell do Mongodb, utilize:
```
mongoexport --db kabum --collection produtos --out produtos.json 
```

--------------------------------------------------------

#### Instruções para execução do projeto

1. Clone o repositório
```
git clone https://github.com/DavidPierre21/kabum_scrapy.git
```

2. Navegue até o diretório do projeto
```
cd intelivix_teste
```

3. Para executar o crawler é preciso navegar até o diretório mais interior do projeto, então, novamente:
```
cd intelivix_teste
```
4. Finalmente, execute:
```
scrapy crawl kabum
```

--------------------------------------------------------

#### Tempo gasto
| Atividade | Tempo Gasto |
| --------- | ----------- |
| Escolhendo site | 2h |
| Configuração do ambiente | 1h |
| Estudos para projeto | 2h |
| Desenvolvimento do Crawler | 6h |
| Configuração de banco de dados | 1h |
| Criação de pipeline e configuração do Scrapy | 1h |
| Revisão de código e ajustes finais | 2h |
| **Total** | **15h** |
