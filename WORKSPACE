load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_pkg",
    sha256 = "d20c951960ed77cb7b341c2a59488534e494d5ad1d30c4818c736d57772a9fef",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/1.0.1/rules_pkg-1.0.1.tar.gz",
        "https://github.com/bazelbuild/rules_pkg/releases/download/1.0.1/rules_pkg-1.0.1.tar.gz",
    ],
)

http_archive(
    name = "rules_python",
    sha256 = "0cc05ddb27614baecace068986931e2a6e9f69114e6115fc5dc58250faf56e0f",
    strip_prefix = "rules_python-0.37.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.37.0.tar.gz",
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
