from home import app_settings

# home app context
def home_context(request):
    context = {
        'get_master_template': app_settings.MASTER_TEMPLATE
    }
    return context
