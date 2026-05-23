#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
localize_3d.py — 把 profile-3d-contrib/*.svg 里 yoshi389111 硬编码的英文 label
全部替换成中文。Workflow 里也跑同样的替换,这是本地立即生效用。

替换映射:
  Commit         -> 提交
  Issue          -> 议题
  PullReq        -> PR
  Review         -> 评审
  Repo           -> 仓库
  contributions  -> 次贡献
"""
import os, glob, io

REPL = [
    (">Commit<",        ">提交<"),
    (">Issue<",         ">议题<"),
    (">PullReq<",       ">PR<"),
    (">Review<",        ">评审<"),
    (">Repo<",          ">仓库<"),
    (">contributions<", ">次贡献<"),
]

base = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "profile-3d-contrib"))
files = sorted(glob.glob(os.path.join(base, "*.svg")))
print(f"found {len(files)} SVG(s) under {base}")

for f in files:
    with io.open(f, encoding="utf-8") as fh:
        s = fh.read()
    orig = s
    for a, b in REPL:
        s = s.replace(a, b)
    if s != orig:
        with io.open(f, "w", encoding="utf-8") as fh:
            fh.write(s)
        print(f"  ✓ {os.path.basename(f)}")
    else:
        print(f"  - {os.path.basename(f)} (no change)")
