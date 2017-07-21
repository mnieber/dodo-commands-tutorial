"""Configure code with CMake."""
from dodo_commands.system_commands import DodoCommand

class Command(DodoCommand):  # noqa
    def handle_imp(self, **kwargs):  # noqa
        self.runcmd(
            ["cmake"] +
            [
                "-D%s=%s" % x for x in
                self.get_config('/CMAKE/variables').items()
            ] +
            [self.get_config("/ROOT/src_dir")],
            cwd=self.get_config("/ROOT/build_dir")
        )
