import random
from django.core.management.base import BaseCommand
from project_management.models import Project, ProjectMember, ProjectRole
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with project members"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        projects = list(Project.objects.all())
        roles = list(ProjectRole.objects.all())

        if not users or not projects or not roles:
            self.stdout.write(self.style.ERROR("No users, projects, or roles found! Run seed_users, seed_projects, and seed_roles first."))
            return

        created_members = []

        for project in projects:
            assigned_users = set() 
            num_members = min(len(users), random.randint(1, 3))

            while len(assigned_users) < num_members:
                user = random.choice(users)
                role = random.choice(roles)

                if user.id in assigned_users:
                    continue

                member, created = ProjectMember.objects.get_or_create(user=user, project=project, role=role)
                if created:
                    assigned_users.add(user.id)
                    created_members.append(f"{user.username} -> {project.name} ({role.name})")

        if created_members:
            self.stdout.write(self.style.SUCCESS(f"Seeded {num_members} project members:"))
            for member in created_members:
                self.stdout.write(f" - {member}")
        else:
            self.stdout.write(self.style.WARNING("No new project members added (all users are already assigned)."))
