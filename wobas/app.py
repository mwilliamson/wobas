from werkzeug.routing import Map, Rule, NotFound, RequestRedirect
from .web import WebApp
from . import injection
from . import controllers


_url_map = Map([
    Rule("/buckets/<bucket_slug>", endpoint=controllers.ViewBucketController),
])

app = WebApp(injection.create_bindings(), _url_map).wsgi_app()
