from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'residents', views.ResidentView, 'resident')
router.register(r'complexes', views.ComplexView, 'complex')
router.register(r'units', views.UnitView, 'unit')
router.register(r'leases', views.LeaseView, 'lease')
router.register(r'units-by-complex', views.UnitsByComplexView, 'units_by_complex')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/units-by-complex/', views.UnitsByComplexView.as_view(), name='get_units_by_complex'),

]