from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class AuthService:
    @staticmethod
    def authenticate_user(request, username, password):
        """
        Validates username and password and returns User object if valid, else None.
        """
        return authenticate(request, username=username, password=password)

    @staticmethod
    def login_user(request, user, remember_me=False):
        """
        Logs in the user and handles session cookie age logic based on remember_me flag.
        """
        login(request, user)
        if remember_me:
            # 14 days session age: 14 * 24 * 60 * 60 = 1,209,600 seconds
            request.session.set_expiry(1209600)
        else:
            # Browser close session expiry
            request.session.set_expiry(0)

    @staticmethod
    def logout_user(request):
        """
        Logs out the user and invalidates the session.
        """
        logout(request)

    @staticmethod
    def register_user(form):
        """
        Saves the registration form and returns the newly created active User.
        """
        user = form.save(commit=False)
        # Force username lowercase for standard database uniqueness checking
        user.username = user.username.lower()
        user.save()
        return user
