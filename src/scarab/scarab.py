"""
Scarab node
"""
import importlib
import json
import os
import subprocess
import sys
import tempfile
import uuid
import venv
from contextlib import contextmanager
from pathlib import Path
from argparse import ArgumentParser
from logging import getLogger
from tempfile import tempdir

import pip


logger = getLogger(__name__)


def get_args(argv):
    args = ArgumentParser(description=__doc__)
    args.add_argument(
        "TASK",
        help="Filepath to task definition or entry point",
    )
    return args.parse_args(argv)


@contextmanager
def environ_context(env: dict):
    """context manager for environment variables"""

    old_env = os.environ.copy()
    try:
        os.environ.clear()
        os.environ.update(env)
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_env)


@contextmanager
def venv_context(name=uuid.uuid4()):
    """create virtual environment with context manager"""
    
    with tempfile.TemporaryDirectory() as temp:
        venv_pth = Path(temp) / f"venv_{name}"
        venv.create(venv_pth, with_pip=True)
        output = subprocess.check_output(
            [
                venv_pth / "Scripts" if (sys.platform == "win32") else "bin" / "python",
                "-c",
                "import os, json; print(json.dumps(dict(os.environ)))"
            ],
            shell=(sys.platform == "win32")
        )
        env = json.loads(output)
        os.environ.clear()
        os.environ.update(env)
        with environ_context(env):
            yield venv_pth


def main(argv=sys.argv):
    args = get_args(argv)

    # invoke venv
    with venv_context() as venv_pth:
        # Inastll TASK as local package
        pip.main(["install", "-e", args.TASK])
        task_module = importlib.import_module(args.TASK)
        task_module.run(args)

    return 0


if __name__ == "__main__":
    logger.info("SCARAB")
    os.exit(main())
