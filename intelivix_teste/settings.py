BOT_NAME = 'intelivix_teste'

SPIDER_MODULES = ['intelivix_teste.spiders']
NEWSPIDER_MODULE = 'intelivix_teste.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'intelivix_teste.pipelines.MongoDBPipeline': 300}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "kabum"
MONGODB_COLLECTION = "produtos"