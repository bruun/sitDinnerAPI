from src.dinner.models import Cafeteria, Dinner
from src.dinner.views import fetch_and_create
from datetime import date,datetime
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        start = datetime.now()
        cafeterias = Cafeteria.objects.all()
        for cafeteria in cafeterias:
            #Dinner.objects.create(cafeteria=cafeteria, date=date(2011,5,30), description='trololol', price=42)
            fetch_and_create(cafeteria, date.today())
        print datetime.now() - start