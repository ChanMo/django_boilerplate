"""
Fabric with django-docker
"""
from fabric import task


@task
def deploy(c):
    with c.cd("/path/to/code/"):
        c.run("git pull origin master")
        c.run("docker-compose -f docker-compose-deploy.yml exec web python manage.py makemigrations")
        c.run("docker-compose -f docker-compose-deploy.yml exec web python manage.py migrate --noinput")
        c.run("docker-compose -f docker-compose-deploy.yml exec web python manage.py collectstatic --noinput")
        c.run("docker-compose -f docker-compose-deploy.yml restart")
