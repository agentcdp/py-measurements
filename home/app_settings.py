from django.conf import settings

MASTER_TEMPLATE = settings.MASTER_TEMPLATE if hasattr(settings, 'MASTER_TEMPLATE') else 'master.html'