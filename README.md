# dodo_commands_tutorial

Tutorial project for the Dodo Commands framework. This project is referenced in the README of [dodo commands](https://github.com/mnieber/dodo_commands).

    ```
    FROM ubuntu:latest

    # Install prerequisites
    RUN apt-get update && apt-get install -y python-pip git
    RUN pip install --upgrade pip
    RUN pip install virtualenv

    # HACK: fake docker and cmake installations by using dummy executables
    RUN ln -s /bin/bash /usr/bin/docker
    RUN ln -s /bin/bash /usr/bin/cmake
    ```
