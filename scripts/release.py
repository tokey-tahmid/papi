# scripts/release.py
from __future__ import annotations
import argparse, subprocess, sys, os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def sh(*args: str, cwd: Path | None = None, env: dict | None = None) -> str:
    # Force UTF-8 output and tolerate legacy encodings
    env2 = os.environ.copy()
    env2.update({"LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"})
    if env:
        env2.update(env)
    cp = subprocess.run(
        list(args), cwd=cwd, env=env2,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
    )
    return cp.stdout.decode("utf-8", errors="replace").strip()


def run(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(list(args), cwd=cwd, check=True)

def replace_line(path: Path, startswith: str, new_line: str) -> None:
    lines = path.read_text().splitlines()
    hit = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith(startswith):
            lines[i] = new_line
            hit = True
    if not hit:
        raise RuntimeError(f"'{startswith}' not found in {path}")
    path.write_text("\n".join(lines) + "\n")

def bump(version: str) -> None:
    # Accept "auto" to derive from tag
    if version == "auto":
        version = sh("git", "describe", "--tags").removeprefix("tags/").replace("-", ".")
    major, minor, rev, inc = version.split(".")
    replace_line(ROOT/"papi.spec", "Version:", f"Version: {version}")
    replace_line(ROOT/"doc/Doxyfile-common", "PROJECT_NUMBER", f"PROJECT_NUMBER         = {version}")
    replace_line(ROOT/"src/papi.h", "#define PAPI_VERSION", f"#define PAPI_VERSION  \t\t\tPAPI_VERSION_NUMBER({major},{minor},{rev},{inc})")
    replace_line(ROOT/"src/configure.in", "AC_INIT", f"AC_INIT(PAPI, {version}, ttahmid@icl.utk.edu)")
    for var, val in {"PAPIVER":major, "PAPIREV":minor, "PAPIAGE":rev, "PAPIINC":inc}.items():
        replace_line(ROOT/"src/Makefile.in", var, f"{var}={val}")

def changelog(start_commit: str, out: Path) -> None:
    if start_commit == "LAST_TAG":
        last_tag = sh("git", "describe", "--tags", "--abbrev=0")
        start_commit = last_tag
    log = sh(
        "git", "-c", "i18n.logOutputEncoding=UTF-8", "-c", "core.quotepath=false",
        "log", "--no-merges", "--date=short",
        f"{start_commit}..HEAD",
        "--pretty=format:* %ad %an — %s"
    )
    out.write_text(log + "\n")

def package(name: str) -> None:
    dst = ROOT.parent / name
    if dst.exists():
        run("rm","-rf",str(dst))
    run("git","clone",".",str(dst), cwd=ROOT)
    # prune
    for p in [
        "PAPI_FAQ.html","doc/DataRange.html","doc/PAPI-C.html","doc/README",
        "src/buildbot_configure_with_components.sh","papi_procedures.py",
        ".git",".github",".gitattributes"
    ]:
        target = dst/p
        if target.is_dir(): run("rm","-rf",str(target))
        elif target.exists(): target.unlink()
    # tar.gz
    tar = ROOT.parent / f"{name}.tar"
    run("tar","-cvf",str(tar), name, cwd=ROOT.parent)
    run("gzip", str(tar), cwd=ROOT.parent)

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s1 = sub.add_parser("bump"); s1.add_argument("--version", required=True)
    s2 = sub.add_parser("changelog"); s2.add_argument("--from", dest="from_", required=True); s2.add_argument("--out", type=Path, required=True)
    s3 = sub.add_parser("package"); s3.add_argument("--name", required=True)
    args = ap.parse_args()
    if args.cmd == "bump": bump(args.version)
    elif args.cmd == "changelog": changelog(args.from_, args.out)
    elif args.cmd == "package": package(args.name)

if __name__ == "__main__":
    main()
