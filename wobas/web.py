from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import SharedDataMiddleware
import zuice

from . import paths, templating


PathArguments = zuice.key("PathArguments")


class WebApp(object):
    def __init__(self, bindings, url_map):
        self._bindings = bindings
        self._url_map = url_map
    
    def respond(self, request, urls):
        controller_cls, args = urls.match()
        
        bindings = self._bindings.copy()
        bindings.bind(PathArguments).to_instance(args)
        
        injector = zuice.Injector(bindings)
        
        controller = injector.get(controller_cls)
        
        kwargs = dict(
            (key, injector.get(dependency))
            for key, dependency in controller.request.iteritems()
        )
        
        return controller.respond(**kwargs)

    def wsgi_app(self):
        def handle(environ, start_response):
            request = Request(environ)
            urls = self._url_map.bind_to_environ(environ)
            response = self.respond(request, urls)
            return response(environ, start_response)
            
        return SharedDataMiddleware(handle, {
            "/static": paths.local_project_path("static"),
        })


class Responder(zuice.Base):
    _templates = zuice.dependency(templating.Templates)
    
    def html(self, name, context):
        return Response(
            self._templates.template(name + ".html", context=context),
            mimetype="text/html",
        )
