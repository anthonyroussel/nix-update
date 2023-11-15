import subprocess

import conftest

from nix_update import main


def test_main(helpers: conftest.Helpers) -> None:
    with helpers.testpkgs(init_git=True) as path:
        main(
            [
                "--file",
                str(path),
                "--commit",
                "--url",
                "https://github.com/jetty/jetty.project",
                "--version-regex",
                "jetty-(.*)",
                "fetchurl",
            ]
        )

        version = subprocess.run(
            [
                "nix",
                "eval",
                "--raw",
                "--extra-experimental-features",
                "nix-command",
                "-f",
                path,
                "fetchurl.version",
            ],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
        ).stdout.strip()
        assert tuple(map(int, version.split("."))) >= (12, 0, 3)

        diff = subprocess.run(
            ["git", "-C", path, "show"],
            text=True,
            stdout=subprocess.PIPE,
            check=True,
        ).stdout.strip()
        assert (
            "https://github.com/jetty/jetty.project/compare/jetty-12.0.2...jetty-" in diff
        )
