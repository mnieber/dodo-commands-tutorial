# dodo_commands_tutorial

Tutorial project for the Dodo Commands framework. This project is referenced in the README of [dodo commands](https://github.com/mnieber/dodo_commands). The steps described in that README are also listed below, in the shape of a Dockerfile (that you can run without having anything cloned or installed yet).

<aside class="notice">
This dockerfile uses a hack that is not needed in a normal use-case. It creates an environment variable <b>HACK</b> that points to project directory containing the dodo executable. In an normal use case, you can activate a project and simply type "dodo".
</aside>

# Dockerfile explaining the tutorial steps

FROM ubuntu:latest

# Install prerequisites
RUN apt-get update && apt-get install -y python-pip git
RUN pip install --upgrade pip
RUN pip install virtualenv

# HACK: fake docker and cmake installations by using dummy executables
RUN ln -s /bin/bash /usr/bin/docker
RUN ln -s /bin/bash /usr/bin/cmake

# Install dodo commands
RUN pip install dodo_commands
RUN dodo install-default-commands standard_commands
RUN dodo install-default-commands --pip dodo_webdev_commands

# create empty tutorial project
RUN dodo activate --create dodo_tutorial

# HACK: work around inability to activate the project during a docker build.
# In a normal use-case, BIN_DIR is not needed.
ENV BIN_DIR /root/projects/dodo_tutorial/dodo_commands/env/bin

# show all commands
RUN $BIN_DIR/dodo

# bootstrap the tutorial project
RUN $BIN_DIR/dodo bootstrap src extra/dodo_commands/res --force --git-url https://github.com/mnieber/dodo_commands_tutorial.git

# show all commands again (this time there is a new cmake command)
RUN $BIN_DIR/dodo

# show cmake script
RUN cat $($BIN_DIR/dodo which --script cmake)

# show cmake command line
RUN $BIN_DIR/dodo cmake --echo

# show configuration
RUN cat $($BIN_DIR/dodo which --config)

# print expanded configuration
RUN $BIN_DIR/dodo print-config

# toggle the debug layer
RUN $BIN_DIR/dodo layer debug on

# print expanded configuration again (CMAKE_BUILD_TYPE now expands to "debug")
RUN $BIN_DIR/dodo print-config

# show cmake command line again
RUN $BIN_DIR/dodo cmake --echo
