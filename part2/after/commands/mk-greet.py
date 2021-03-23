from dodo_commands import Dodo

Dodo.parser.add_argument("greeting")
Dodo.run(
  ["make", "greeting", "GREETING=%s" % Dodo.args.greeting],
  cwd=Dodo.get("/MAKE/cwd")
)
