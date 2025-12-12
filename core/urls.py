from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Simple homepage view
def home(request):
    return HttpResponse("Welcome to the HR System!")

urlpatterns = [
    path('admin/', admin.site.urls),        # Admin panel
    path('', home, name='home'),            # Homepage URL
    # You can add API or app URLs here, e.g.:
    # path('api/performance/', include('performance.urls')),
    # path('api/leave/', include('leave.urls')),
]

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
