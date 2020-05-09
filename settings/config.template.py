import sys 

CouchbaseENV = "development"

CouchbaseConfig = {
    'local': {
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'dev': {
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'uat': {
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TIMEOUT': 7200
    },
    'prod': {
        'BUCKET': '',
        'USERNAME': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TIMEOUT': 7200
    }
}

ElasticSearchENV = 'local'

ElasticSearchConfig = {
    'dev': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
    'local': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    },
    'prod': {
        'USERNAME': '',
        'PASSWORD': '',
        'INDEX': 'philippines',
        'TYPE': 'patients',
        'SCHEME': 'HTTP',
        'HOST': 'localhost',
        'PORT': 9200,
        'TIMEOUT': 7200
    }
}