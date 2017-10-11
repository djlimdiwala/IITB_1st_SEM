from django.contrib.auth.models import User


user=User.objects.create_user('naimish', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()


user=User.objects.create_user('dhaval', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()


user=User.objects.create_user('anisha', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()


user=User.objects.create_user('anisha1', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()


user=User.objects.create_user('anisha2', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()


user=User.objects.create_user('anisha3', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()

user=User.objects.create_user('anisha4', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()

user=User.objects.create_user('anisha5', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()

user=User.objects.create_user('anisha6', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()

user=User.objects.create_user('anisha7', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()

user=User.objects.create_user('anisha8', password='limdiwala')
user.is_superuser=True
user.is_staff=True
user.save()
