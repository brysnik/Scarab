import typing
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape
from .. import templates

if typing.TYPE_CHECKING:
    from jinja2 import Template


class Jinja:

    _env: Environment = None

    @classmethod
    @property
    def env(cls) -> Environment:
        if not cls._env:
            cls._env = Environment(
                loader=PackageLoader(
                    "scarab.web.templates",
                    package_path=str(Path(templates.__file__).parent)
                ),
                autoescape=select_autoescape(['html', 'xml'])
            )
        return cls._env

    @classmethod
    def load(cls, name):
        return cls.env.loader.load(cls.env, name)


def get_template(name) -> 'Template':
    return Jinja.load(name)


def render_template(name) -> str:
    return get_template(name).render()
