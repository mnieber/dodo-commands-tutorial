from dodo_commands import Dodo

import dominate


def run_make(*what):
    Dodo.run(["make", *what], cwd=Dodo.get("/MAKE/cwd"))


if Dodo.is_main(__name__):
    Dodo.parser.add_argument("what")
    run_make(Dodo.args.what)
