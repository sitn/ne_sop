from django.urls import path, include

# from rest_framework.urlpatterns import format_suffix_patterns
from ne_sop_api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"item", views.ItemViewSet, basename="item")
router.register(r"item-type", views.ItemTypeViewSet, basename="item-type")
router.register(r"item-status", views.ItemStatusViewSet, basename="item-status")
router.register(r"entity", views.EntityViewSet, basename="entity")
# router.register(r"entity-list", views.EntityListViewSet, basename="entity-list")
router.register(r"entity-type", views.EntityTypeViewSet, basename="entity-type")
router.register(r"event", views.EventViewSet, basename="event")
router.register(r"event-type", views.EventTypeViewSet, basename="event-type")
router.register(r"template", views.TemplateViewSet, basename="template")
router.register(r"user", views.UserViewSet, basename="user")

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("", include(router.urls)),
    path("api/", include(router.urls)),
    path(
        "api/entity/<uuid:uuid>/",
        views.EntityViewSet.as_view(actions={"get": "retrieve"}),
        name="entity-uuid",
    ),
    path(
        "api/entitylist/",
        views.EntityListViewSet.as_view(),
        name="entitylist",
    ),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/schema/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]


"""     path(
        "api/entitylist/",
        views.EntityListViewSet.as_view(),
        name="entity-list",
    ), """


# https://github.com/encode/django-rest-framework/issues/1337
# urlpatterns = format_suffix_patterns(urlpatterns)
