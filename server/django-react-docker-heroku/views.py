from django.http import HttpResponse, HttpResponseNotAllowed
from graphene_django.views import GraphQLView as BaseGraphQLView, HttpError

import logging
import os

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
)


class GraphQLView(BaseGraphQLView):
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() not in ('get', 'post', 'options'):
            raise HttpError(HttpResponseNotAllowed(
                ['GET', 'POST', 'OPTIONS'], 'GraphQL only supports GET, POST and OPTIONS requests.'))

        if request.method.lower() == 'options':
            return HttpResponse(
                status=200,
                content='',
                content_type='application/json'
            )

        return super().dispatch(request, *args, **kwargs)
