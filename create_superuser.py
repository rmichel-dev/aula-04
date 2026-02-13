from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@email.com"
password = "12345678"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superusuário criado com sucesso.")
else:
    print("Superusuário já existe.")