import jinja2
import json
from os import environ, system


def render(file):
    source = "kluster/templates/" + file + ".j2"
    with open(source, "r") as s:
        t = jinja2.Template(s.read())
    new_file = "dist/kluster/" + file
    with open(new_file, "w") as f:
        f.write(t.render(env=environ.get))
    print(f"{source} => {new_file}")


def render_all():
    l = list(json.load(open("kluster/template_list.json")))
    for file in l:
        render(file)


def deploy():
    system("kubectl apply -f dist/kluster/")


def main():
    render_all()
    deploy()


if __name__ == "__main__":
    main()
