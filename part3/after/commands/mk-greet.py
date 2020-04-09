from dodo_commands import Dodo

from dodo_tutorial_commands.mk import run_make

Dodo.parser.add_argument("greeting")
run_make("greeting", "GREETING=%s" % Dodo.args.greeting)
