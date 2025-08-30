from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, email, password=None):
        user = self.create_user(name, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


