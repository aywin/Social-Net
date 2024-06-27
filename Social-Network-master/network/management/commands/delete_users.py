from django.core.management.base import BaseCommand
from network.models import User, Stage, Poste, Mobilite

class Command(BaseCommand):
    help = 'Supprime les utilisateurs ayant un point dans leur nom d\'utilisateur ainsi que leurs stages, postes, et mobilités associés'

    def handle(self, *args, **kwargs):
        # Filtrer les utilisateurs ayant un point dans leur nom d'utilisateur
        utilisateurs_avec_point = User.objects.filter(username__contains='.')

        for utilisateur in utilisateurs_avec_point:
            # Supprimer les stages associés
            Stage.objects.filter(user=utilisateur).delete()
            # Supprimer les postes associés
            Poste.objects.filter(user=utilisateur).delete()
            # Supprimer les mobilités associées
            Mobilite.objects.filter(user=utilisateur).delete()
            # Supprimer l'utilisateur
            utilisateur.delete()
            self.stdout.write(self.style.SUCCESS(f'Utilisateur {utilisateur.username} supprimé avec succès avec ses stages, postes, et mobilités'))

        self.stdout.write(self.style.SUCCESS('Tous les utilisateurs avec un point dans leur nom d\'utilisateur et leurs données associées ont été supprimés avec succès'))
