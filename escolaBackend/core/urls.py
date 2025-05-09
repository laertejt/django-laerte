from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from administracao.apis import router as administracaoRouter

api = NinjaAPI()
api.add_router("/administracao/",administracaoRouter )


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home),
    path("api/", api.urls),
]

