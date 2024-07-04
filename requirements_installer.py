import pip

def install_library(name):
    requirements = [
        "install",
        name,
    ]
    pip.main(requirements)
