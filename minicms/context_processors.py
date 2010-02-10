from django.conf import settings

def cms(request):
    base_url = 'http%s://%s' % ('s' if request.is_secure() else '',
                                request.get_host())

    return {
        'site_name': settings.SITE_NAME,
        'site_description': settings.SITE_DESCRIPTION,
        'site_copyright': settings.SITE_COPYRIGHT,
        'site_base_url': base_url,
        'twitter_username': getattr(settings, 'TWITTER_USERNAME', None),
        'google_analytics_id': getattr(settings, 'GOOGLE_ANALYTICS_ID', None),
        'google_custom_search_id': getattr(settings, 'GOOGLE_CUSTOM_SEARCH_ID',
                                           None),
    }
