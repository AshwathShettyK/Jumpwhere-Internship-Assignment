from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, NoReverseMatch

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self._exempt_urls = None

    def get_exempt_urls(self):
        """
        Lazy load exempt URL paths to prevent AppRegistryNotReady / NoReverseMatch
        exceptions during Django initialization.
        """
        if self._exempt_urls is None:
            exempt = []
            # Add named authentication routes if resolvable
            for name in ['accounts:login', 'accounts:logout', 'accounts:register']:
                try:
                    exempt.append(reverse(name))
                except NoReverseMatch:
                    pass
            
            # Add hardcoded admin paths
            exempt.extend(['/admin/login/', '/admin/'])
            
            # Add asset directories
            if getattr(settings, 'STATIC_URL', None):
                exempt.append(settings.STATIC_URL)
            if getattr(settings, 'MEDIA_URL', None):
                exempt.append(settings.MEDIA_URL)
                
            self._exempt_urls = exempt
        return self._exempt_urls

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            exempt_urls = self.get_exempt_urls()
            
            # Check if current path matches or starts with any exempt URL patterns
            is_exempt = any(path.startswith(url) for url in exempt_urls)
            if not is_exempt:
                # Include next query parameter for post-login redirect
                login_url = reverse('accounts:login')
                return redirect(f"{login_url}?next={path}")
                
        return self.get_response(request)
