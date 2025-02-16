from django.http import HttpResponseForbidden
from django.urls import resolve
from django.conf import settings

class RestrictIPMiddleware:
    RESTRICTED_PATHS = ['special-path','add-ip']  # A list of paths you want to restrict

    def __init__(self, get_response):
        self.get_response = get_response

        # Initialize the allowed IPs list (you can also get this from settings)
        self.allowed_ips = getattr(settings, 'ALLOWED_IPS', [])

    def __call__(self, request):
        # Get the current path
        current_path = resolve(request.path_info).url_name

        # Check if the current path is in the restricted paths list
        if current_path in self.RESTRICTED_PATHS:
            ip_address = self.get_ip_address(request)  # Get the IP address from the request

            # Debugging: Print the retrieved IP address
            print(f"Request IP Address: {ip_address}")

            # Debugging: Print allowed IPs to verify
            print(f"Allowed IPs: {self.allowed_ips}")

            if ip_address not in self.allowed_ips:
                return HttpResponseForbidden("You are not authorized to access this page.")

        response = self.get_response(request)
        return response

    def get_ip_address(self, request):
        # Try to get the IP address from the 'X-Forwarded-For' header if present
        ip = request.META.get('HTTP_X_FORWARDED_FOR')

        if ip:
            ip = ip.split(',')[0]  # Use the first IP address in the list
        else:
            ip = request.META.get('REMOTE_ADDR')  # Get the direct IP address

        return ip

    def add_allowed_ip(self, new_ip):
        """Method to add a new IP to the allowed IPs list."""
        if new_ip not in self.allowed_ips:
            self.allowed_ips.append(new_ip)
            print(f"IP {new_ip} added to allowed IPs list.")
