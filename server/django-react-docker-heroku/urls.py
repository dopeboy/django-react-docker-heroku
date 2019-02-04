from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from .views import FrontendAppView, GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=settings.GRAPHQL_DEBUG))),
    path('gql', csrf_exempt(GraphQLView.as_view())),
    re_path(r'.*', FrontendAppView.as_view()),
]
