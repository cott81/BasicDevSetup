"""Utility functions for sphinx conf.py configuration files."""

import os
from pathlib import Path

import git


class GitWrapper:
    def __init__(self) -> None:
        self.repo = git.Repo(Path.cwd(), search_parent_directories=True)

    def url(self) -> str:
        _url = next(self.repo.remote().urls)
        if _url.endswith(".git"):
            _url = _url[: -len(".git")]
        return _url

    def toplevel(self) -> os.PathLike:
        top = self.repo.git.rev_parse("--show-toplevel")
        return Path(top)

    def commit(self) -> str:
        return self.repo.head.commit.hexsha

    def describe(
        self,
        /,
        *,
        dirty: bool = True,
        always: bool = False,
        tags: bool = False,
        match: str | list[str] | None = None,
    ) -> str:
        cmd = []

        if dirty:
            cmd.append("--dirty")
        if always:
            cmd.append("--always")
        if tags:
            cmd.append("--tags")

        if isinstance(match, list):
            cmd.extend(f"--match={m}" for m in match)

        if isinstance(match, str):
            cmd.append(f"--match={match}")

        return self.repo.git.describe(*cmd)
