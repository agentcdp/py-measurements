from django.conf import settings

# Master template
MASTER_TEMPLATE = settings.MASTER_TEMPLATE if hasattr(settings, 'MASTER_TEMPLATE') else 'master.html'
