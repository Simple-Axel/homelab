import jinja2
import json
from os import environ, system


def render(file):
    source = "kluster/templates/" + file + ".j2"
    t = jinja2.Template(source)
    new_file = "dist/kluster/" + file
    with open(new_file, "w") as f:
        f.write(t.render(environ.get))
    print(f"{source} => {new_file}")


def render_all():
    l = json.load(open("kluster/template_list.json"))
    for file in l:
        render(file)


def deploy():
    system("kubectl apply -f dist/kluster/")


def main():
    render_all()
    deploy()
