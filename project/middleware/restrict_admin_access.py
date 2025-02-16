from django.http import HttpResponseForbidden
from django.urls import resolve
from django.conf import settings

class RestrictAdminAccessMiddleware:
    # A list of paths related to the admin panel that you want to restrict
    RESTRICTED_PATHS = [
        'admin', 'admin:index', 'admin:login', 
        'admin:logout', 'admin:password_change', 'admin:password_change_done',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

        # Load allowed IPs from settings
        self.allowed_ips = getattr(settings, 'ALLOWED_ADMIN_IPS', [])
        print(f"Allowed IPs loaded: {self.allowed_ips}")  # Debugging: Ensure allowed IPs are loaded

    def __call__(self, request):
        # Debugging: Log the requested path
        request_path = request.path_info
        print(f"Request path: {request_path}")

        # Resolve the URL to check if it's an admin panel-related path
        resolved_url = self.resolve_url(request)

        # If the path is in the restricted list, check the IP
        if resolved_url in self.RESTRICTED_PATHS or self.is_admin_path(request_path):
            ip_address = self.get_ip_address(request)

            # Check if the IP address is allowed
            if ip_address not in self.allowed_ips:
                print(f"Access Denied: IP {ip_address} is not allowed.")  # Debugging: IP not allowed
                return HttpResponseForbidden("You are not authorized to access the admin panel.")

        # Proceed with the request
        return self.get_response(request)

    def resolve_url(self, request):
        """
        Resolves the URL name from the request path.
        """
        try:
            resolved_url = resolve(request.path_info).url_name
            print(f"Resolved URL: {resolved_url}")  # Debugging: Show resolved URL
            return resolved_url
        except Exception as e:
            print(f"Error resolving URL: {e}")
            return None

    def is_admin_path(self, path):
        """
        Checks if the path is part of the restricted admin paths.
        """
        return any(restricted_path in path for restricted_path in self.RESTRICTED_PATHS)

    def get_ip_address(self, request):
        """
        Extracts the IP address from the request, considering the 'X-Forwarded-For' header.
        """
        ip = request.META.get('HTTP_X_FORWARDED_FOR')

        if ip:
            ip = ip.split(',')[0]  # Get the first IP address if there are multiple
        else:
            ip = request.META.get('REMOTE_ADDR')  # Use the direct IP address

        print(f"Extracted IP address: {ip}")  # Debugging: Show extracted IP
        return ip
