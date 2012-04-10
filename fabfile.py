from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'webfaction'
DEST_PATH = '/home/jfilipe/webapps/filipe_blog'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
BUILD_PATH = os.path.join(ROOT_PATH, 'build')


def clean():
    local('rm -rf %s' % BUILD_PATH)


def compile_scss():
    with lcd('%s/static/scss' % ROOT_PATH):
        local('compass compile --output-style compressed --force')


def freeze():
    clean()
    compile_scss()
    local('python %s/site.py freeze' % ROOT_PATH)


def serve():
    compile_scss()
    local('python %s/site.py' % ROOT_PATH)


def smush():
    local('smusher %s/static/img' % ROOT_PATH)


@hosts(PROD)
def deploy():
    freeze()
    project.rsync_project(
        remote_dir=DEST_PATH,
        local_dir=BUILD_PATH.rstrip('/') + '/',
        exclude=['.DS_Store', 'static/scss'],
        delete=True)
