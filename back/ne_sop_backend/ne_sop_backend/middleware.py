from django.conf import settings
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.backends import RemoteUserBackend

class RemoteSitnMiddleware(RemoteUserMiddleware):
    """
    Custom middleware to mimic a SSPI Auth when we dev in local
    It will set a Remote-User header with the DEBUG_USER in settings
    """
    def process_request(self, request):
        if settings.DEBUG and getattr(settings, "DEBUG_USER", None):
            request.META[self.header] = settings.DEBUG_USER
        super().process_request(request)


class RemoteSitnUserBackend(RemoteUserBackend):
    create_unknown_user = False
