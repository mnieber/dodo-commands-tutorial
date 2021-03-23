from dodo_commands import Dodo
from dodo_tutorial_commands.mk import run_make

if Dodo.is_main(__name__):
Dodo.parser.add_argument("greeting")
run_make("greeting", "GREETING=%s" % Dodo.args.greeting)
