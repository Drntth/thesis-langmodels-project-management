import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from project_management.models import Project, ProjectStatus, ProjectRole, ProjectMember
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with projects"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        users = list(User.objects.all())
        statuses = list(ProjectStatus.objects.all())

        if not users or not statuses:
            self.stdout.write(self.style.ERROR("No users or statuses found! Run seed_users first."))
            return

        num_projects = 5
        seeder.add_entity(Project, num_projects, {
            'name': lambda x: seeder.faker.company(),
            'owner': lambda x: random.choice(users),
            'status': lambda x: random.choice(statuses),
        })

        inserted_pks = seeder.execute()
        total_created = sum(len(pk_list) for pk_list in inserted_pks.values())
        created_projects = Project.objects.filter(id__in=[pk for pk_list in inserted_pks.values() for pk in pk_list])

        self.stdout.write(self.style.SUCCESS(f"Seeded {total_created} projects:"))
        for project in created_projects:
            self.stdout.write(f" - {project.name}")
