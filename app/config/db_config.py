from app.config import Config

TORTOISE_ORM = {
    'connections': {
        'default': Config.DATABASE_URL,
    },
    'apps': {
        'models': {
            'models': ['app.models', 'aerich.models'],  
            'default_connection': 'default',
        },
    },
}
