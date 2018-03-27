from django.urls import path
from . import views
from ffs.views import product_list_view
from ffs.views import user_view
from ffs.views import search_view
from ffs.views import flagged_view
from ffs.views import landing_view
from ffs.views import upload_view

urlpatterns = [
	path('products/', product_list_view),
	path('user/', user_view),
	path('search/', search_view),
	path('flagged/', flagged_view),
	path('upload/', upload_view),
	path('', landing_view),
]
