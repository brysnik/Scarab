from jinja2 import Environment, PackageLoader, select_autoescape

jinja2_env = Environment(
    loader=PackageLoader('resources', package_path="."),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_template(name):
    return jinja2_env.loader.load(name)
