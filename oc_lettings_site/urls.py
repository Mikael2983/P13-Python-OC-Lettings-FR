from django.contrib import admin
from django.urls import path, include

from . import views

# error 500 verification function
def trigger_error(request):
    division_by_zero = 1 / 0

# -------------------------------------------------------------------
# Custom error handlers
# -------------------------------------------------------------------

# These handlers are automatically used by Django when a 404 or 500 error occurs
handler404 = "oc_lettings_site.views.custom_error_404"
handler500 = "oc_lettings_site.views.custom_error_500"

# -------------------------------------------------------------------
# URL patterns
# -------------------------------------------------------------------

urlpatterns = [
    path('test/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
