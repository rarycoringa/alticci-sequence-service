import os

from flask import Flask
from flask_caching import Cache

app = Flask(__name__)


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


# Endpoints configuration
from alticci.sequence.views import AlticciSequenceTermView

app.add_url_rule(
    "/alticci/<int:term>",
    view_func=AlticciSequenceTermView.as_view("sequence_term_view"),
    methods=["GET"],
)
