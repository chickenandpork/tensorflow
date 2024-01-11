load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_pkg",
    sha256 = "e93b7309591cabd68828a1bcddade1c158954d323be2205063e718763627682a",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/0.10.0/rules_pkg-0.10.0.tar.gz",
        "https://github.com/bazelbuild/rules_pkg/releases/download/0.10.0/rules_pkg-0.10.0.tar.gz",
    ],
)

http_archive(
    name = "rules_python",
    sha256 = "48a838a6e1983e4884b26812b2c748a35ad284fd339eb8e2a6f3adf95307fbcd",
    strip_prefix = "rules_python-0.16.2",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.16.2.tar.gz",
)

#
# Python version-locked requirements
#
register_toolchains("//lib/python:python_toolchain")

load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip",
    requirements_lock = "//lib/python:requirements_lock.txt",
)
load("@pip//:requirements.bzl", "install_deps")

install_deps()

#load("@rules_python//python:repositories.bzl", "py_repositories")
#
#py_repositories()

load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")

rules_pkg_dependencies()
