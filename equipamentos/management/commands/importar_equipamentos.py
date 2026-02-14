import csv
from django.core.management.base import BaseCommand
from equipamentos.models import Equipamento

class Command(BaseCommand):
    help = 'Importa equipamentos via CSV'

    def add_arguments(self, parser):
        parser.add_argument('arquivo')

    def handle(self, *args, **kwargs):
        with open(kwargs['arquivo'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Equipamento.objects.get_or_create(
                    nome=row['nome'],
                    tipo=row['tipo'],
                    status=row['status']
                )
        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
