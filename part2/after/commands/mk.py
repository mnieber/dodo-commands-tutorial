from dodo_commands import Dodo

Dodo.parser.add_argument("what")
Dodo.run(["make", Dodo.args.what], cwd=Dodo.get("/MAKE/cwd"))
