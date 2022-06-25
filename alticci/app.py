import os

from flask import Flask
from flask_restful import Api
from flask_caching import Cache
from flasgger import Swagger

# Flask API configuration
app = Flask(__name__)

api = Api(app)

app.config['JSON_SORT_KEYS'] = False
app.config["SWAGGER"] = {
    "title": "Alticci Sequence Service",
    "uiversion": 3,
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "openapi",
            "route": "/openapi.json",
        },
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/",
}
swagger = Swagger(app, config=swagger_config)


# Cache configuration
use_redis_env_var = os.environ.get("USE_REDIS", "false")
use_redis = True if use_redis_env_var.lower() == "true" else False

if use_redis:
    config = {
        "CACHE_TYPE": "RedisCache",
        "CACHE_DEFAULT_TIMEOUT": os.environ.get("CACHE_DEFAULT_TIMEOUT", 300),
        "CACHE_REDIS_HOST": os.environ.get("CACHE_REDIS_HOST", "0.0.0.0"),
        "CACHE_REDIS_PORT": os.environ.get("CACHE_REDIS_PORT", "6379"),
    }
else:
    config = {
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": os.environ.get("CACHE_DEFAULT_TIMEOUT", 60),
    }

cache = Cache(config=config)
cache.init_app(app)


# Resources configuration
from alticci.sequence.views import (
    AlticciSequenceTermView,
    AlticciSequenceTermListView
)

api.add_resource(
    AlticciSequenceTermView,
    "/alticci/<int:term>",
    endpoint="sequence",
)
api.add_resource(
    AlticciSequenceTermListView,
    "/alticci/<int:first_term>/<int:last_term>",
    endpoint="sequence_list",
)
