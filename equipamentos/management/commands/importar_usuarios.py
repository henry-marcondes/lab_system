import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Importa usuários via CSV'

    def add_arguments(self, parser):
        parser.add_argument('arquivo')

    def handle(self, *args, **kwargs):
        with open(kwargs['arquivo'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                username = row.get('username', '').strip()

                if not username:
                    continue

                if not User.objects.filter(username=username).exists():

                    user = User.objects.create_user(
                        username=username,
                        email=row.get('email', '').strip(),
                        password=row.get('password', '').strip(),
                        first_name=row.get('first_name', '').strip(),
                        last_name=row.get('last_name', '').strip()
                    )

                    # ATIVAR USUÁRIO
                    user.is_active = True

                    # STAFF (se vier "true", "1", "sim", etc)
                    if row.get('is_staff', '').strip().lower() in ['true', '1', 'sim', 'yes']:
                        user.is_staff = True

                    user.save()

        self.stdout.write(self.style.SUCCESS('Usuários importados com sucesso!'))
   

