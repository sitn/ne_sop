from django.urls import path, include

# from rest_framework.urlpatterns import format_suffix_patterns
from ne_sop_api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"item", views.ItemViewSet, basename="item")
router.register(r"item-summary", views.ItemSummaryViewSet, basename="item-summary")
router.register(r"item-type", views.ItemTypeViewSet, basename="item-type")
router.register(r"item-status", views.ItemStatusViewSet, basename="item-status")
router.register(r"entity", views.EntityViewSet, basename="entity")
# router.register(r"service", views.ServiceViewSet, basename="service")
router.register(r"entity-type", views.EntityTypeViewSet, basename="entity-type")
# router.register(r"parliamentary-type", views.ParliamentaryTypeViewSet, basename="parliamentary-type")
router.register(r"event", views.EventViewSet, basename="event")
router.register(r"event-type", views.EventTypeViewSet, basename="event-type")
router.register(r"template", views.TemplateViewSet, basename="template")
router.register(r"template-types", views.TemplateTypeViewSet, basename="template-types")
router.register(r"document", views.DocumentViewSet, basename="document")
router.register(r"item-type-statistics", views.ItemTypeStatisticsViewSet, basename="item-type-statistics")
router.register(r"user", views.UserViewSet, basename="user")
router.register(r"current-user", views.CurrentUserViewSet, basename="current-user")
router.register(r"send-late-email", views.LateItemsViewSet, basename="send-late-email")

urlpatterns = [
    path("api/", include(router.urls)),
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
