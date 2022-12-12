from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        employee = self.employee
        if employee:
            return f'{self.username} ({employee.name})'
        return f'{self.username}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


