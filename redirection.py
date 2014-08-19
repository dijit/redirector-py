#!/usr/bin/env python
from urlparse import urlparse
import rivr
from rivr.http import ResponsePermanentRedirect
from rivr.wsgi import WSGIHandler
import redis
from admin import Admin

r = redis.StrictRedis(host='redis1.e3.drk.sc', db=1)

router=rivr.Router((r'^admin/?$', Admin.as_view(connection=r)))

@router.register(r'^')
def handler(request):
    hostname = request.environ['HTTP_HOST']
    if ":" in hostname:
        hostname, port = hostname.split(":", 1)

    URL = r.get(hostname)
    if URL:
        return ResponsePermanentRedirect(URL + request.path)

    raise rivr.Http404('Hostname not found in DB')

app = rivr.MiddlewareController.wrap(router,
        rivr.TemplateMiddleware(template_dirs = ['./'])
        )


wsgi = WSGIHandler(app)

if __name__ == '__main__':
    rivr.serve(app)

