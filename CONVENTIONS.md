# Gods-Plan conventions

Rules for Day 031 through Day 450. Follow these and the repo stays navigable at
Day 450 the same way it is at Day 30.

## The environment

**There is one environment. Every day uses it.**

```bash
source .venv/bin/activate
```

That's the whole thing. No new venv on Day 31, no new venv on Day 200. When a
day needs a library that isn't installed yet, you add it to the shared env — you
do not build a second environment.

In VS Code, select `./.venv/bin/python` as your interpreter once
(`Cmd+Shift+P` → "Python: Select Interpreter") and it stays correct forever.

### Adding a library

```bash
# 1. add the package name to requirements.in  (no version number)
# 2. regenerate the pinned lock
uv pip compile requirements.in -o requirements.txt
# 3. apply it
uv pip sync --python .venv/bin/python requirements.txt
```

`requirements.in` is what you asked for. `requirements.txt` is what you got,
pinned to exact versions. **Never edit the `.txt` by hand** — it's generated.

### Why one env is fine

The usual argument for splitting environments is disk. It doesn't apply here:
uv hardlinks every package from a single global cache, so packages are stored
once no matter how many environments reference them. Measured on this repo, one
combined env and two split envs cost the same (263 MB vs 264 MB). So the split
buys nothing and costs you a decision every single day.

### The one case that would justify a second env

A genuine version conflict — some future day needs, say, pydantic 1.x while
everything else is on 2.x. `uv pip compile` will fail loudly and tell you.

Handle it *then*, for that one day only:

```bash
uv venv "days/151-200/Day 173 Legacy Thing/.venv" --python 3.12
```

Don't pre-split for a conflict that hasn't happened. In 30 days it hasn't.

## Creating a new day

```bash
mkdir -p "days/001-050/Day 031 Your Topic Here"
```

Three rules, each because breaking it costs real time later:

1. **Always three digits.** `Day 031`, not `Day 31`. Two digits sorts `Day 100`
   next to `Day 10` and puts `Day 99` last. Fixed once now, not at Day 200.
2. **Block of 50 by day number.** Days 1–50 in `days/001-050/`, 51–100 in
   `days/051-100/`, up to `days/401-450/`. Create each block the first time you
   need it.
3. **No `:` `/` or trailing `.` in the name.** A colon typed in Finder is stored
   as `/` on disk and breaks every shell command and Docker `COPY` touching that
   path. Parentheses and `&` are fine, but quote them in the shell.

## Python version

Pinned to **3.12** in `.python-version`, managed by uv.

Never use `/usr/bin/python3` or anything under
`/Library/Developer/CommandLineTools/`. That is Apple's Xcode Python: it's 3.9
(end of life), Apple replaces it without warning, and it silently caps your
libraries. It's what held numpy at 2.0.2 and scikit-learn at 1.6.1 for the first
thirty days.

Check before starting work: `python -V` must say `3.12.x`.

## What never goes in git

Already in `.gitignore`, listed here so you know the reasoning:

- `.venv/`, `__pycache__/` — rebuildable from `requirements.txt`
- `*.db`, `*.sqlite3` — every run rewrites them, so every run makes a diff
- `*.log` — same
- `*.joblib`, `*.pkl`, `*.pt` — trained models are outputs; commit `train.py`, not the artifact
- `.DS_Store` — Finder metadata, pure noise

Raw input data (`data/raw/*.csv`) **is** committed. Processed output is not.

Need a model artifact back? `python train.py`.

## Docker days

The image builds on `python:3.12`, which is why local is 3.12 too. When those
drift you get bugs that appear only inside the container.

Note that a Docker day keeps its **own** `requirements.txt`, separate from the
root one, and that's deliberate — it's a pinned lock resolved for
linux/python:3.12, and it lists only what the image actually needs. Your local
env being one big shared environment has no effect on image size. Regenerate it
with:

```bash
uv pip compile ../../../requirements.in --python-version 3.12 -o requirements.txt
```

...then trim it to what the service imports.

## Known loose ends

- `Day 004 exception handling` and `Day 004 exception handling and logging` are
  duplicates; the second is a superset. Delete the first when you're sure.
- Days 007 and 014 have no folder.
