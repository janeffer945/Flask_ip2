from flask import Config
# import os

class config:
    API_KEY='7a66c9e2fdae4141820d7f2881365086'
    BASE_URL='https://newsapi.org/v2/everything?apiKey={}'
    SOURCES_URL='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    SPECIFIC_SOURCE_ARTICLES_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    class ProdConfig(Config):
     DEBUG=False

class DevConfig(Config):
    DEBUG=True

config_options={
    'produnction':ProdConfig,
    'development':DevConfig
}