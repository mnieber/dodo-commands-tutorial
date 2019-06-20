from argparse import ArgumentParser
from dodo_commands.framework import Dodo

def _args():  # noqa
    parser = ArgumentParser(description='Configure code with CMake')
    args = Dodo.parse_args(parser)
    args.src_dir = Dodo.get_config("/ROOT/src_dir")
    args.build_dir = Dodo.get_config("/ROOT/build_dir")
    return args

if Dodo.is_main(__name__):
    args = _args()
    Dodo.run(
        ["cmake"] +
        [
            "-D%s=%s" % x for x in
            Dodo.get_config('/CMAKE/variables').items()
        ] +
        [args.src_dir],
        cwd=args.build_dir
    )
