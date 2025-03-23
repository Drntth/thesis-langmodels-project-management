import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from project_management.models import Project, ProjectStatus
from django.contrib.auth.models import User
import datetime
from pathlib import Path
from django.conf import settings
from utils.clean_filename import clean_filename


class Command(BaseCommand):
    help = "Seed the database with projects"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        users = list(User.objects.all())
        statuses = list(ProjectStatus.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR("No users found! Run seed_users first."))
            return

        if not statuses:
            self.stdout.write(
                self.style.ERROR("No statuses found! Run seed_project_statuses first.")
            )
            return

        num_projects = 5
        seeder.add_entity(
            Project,
            num_projects,
            {
                "name": lambda x: seeder.faker.company(),
                "description": lambda x: seeder.faker.text(max_nb_chars=200),
                "deadline": lambda x: self.generate_future_date(),
                "owner": lambda x: random.choice(users),
                "status": lambda x: random.choice(statuses),
            },
        )

        inserted_pks = seeder.execute()
        total_created = sum(len(pk_list) for pk_list in inserted_pks.values())
        created_projects = Project.objects.filter(
            id__in=[pk for pk_list in inserted_pks.values() for pk in pk_list]
        )

        self.stdout.write(self.style.SUCCESS(f"Seeded {total_created} projects:"))
        for project in created_projects:
            self.create_project_folder(project)
            self.stdout.write(f" - {project.name} (Folder Created)")

    def generate_future_date(self):
        today = datetime.date.today()
        future_days = random.randint(1, 365)
        return today + datetime.timedelta(days=future_days)

    def create_project_folder(self, project):
        project_folder_name = clean_filename(f"{project.owner.username}_{project.name}")
        project_folder_path = (
            Path(settings.MEDIA_ROOT) / "projects" / project_folder_name
        )

        if not project_folder_path.exists():
            project_folder_path.mkdir(parents=True, exist_ok=True)
            self.stdout.write(
                self.style.SUCCESS(f"Created folder: {project_folder_path}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Folder already exists: {project_folder_path}")
            )
