
#ElasticSearchENV = "development"
ElasticSearchENV = "local"

ElasticSearchConfig = {
    'local': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': '2019-icd-10-cm',
        'TYPE': '_doc',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 3600
    },
    'development': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': '2019-icd-10-cm',
        'TYPE': '_doc',
        'SCHEME': 'http',
        'HOST': 'http://159.89.198.132',
        'PORT': 9200,
        'TIMEOUT': 3600
    },
    'production': {
        'USERNAME': 'elastic',
        'PASSWORD': 'elastic',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'http://165.22.110.167',
        'PORT': 9200,
        'TIMEOUT': 360
    }
}





