#!/usr/bin/env bash
#
# Gods-Plan reset: one environment, structure built to hold 450 days.
#
#   1. Installs uv and a real Python 3.12 (never Apple's CommandLineTools Python again)
#   2. Deletes all 14 stale Python 3.9 venvs (~469 MB)
#   3. Builds ONE .venv that every day shares
#   4. Restructures into days/001-050/Day 0NN Topic/  with 3-digit padding
#   5. Untracks .DS_Store and the generated .db / .log / .joblib files
#   6. Repairs every path reference the renames would have broken
#
# Safe to run more than once. Re-run it after adding new days to re-file them.
#
set -euo pipefail

REPO="$HOME/Desktop/Aryan Space/Gods-Plan"
cd "$REPO"

say() { printf '\n\033[1;36m==> %s\033[0m\n' "$1"; }
ok()  { printf '    \033[0;32mok\033[0m %s\n' "$1"; }

[ -d .git ] || { echo "Not a git repo: $REPO"; exit 1; }

# ---------------------------------------------------------------- 1. uv + Python
say "Installing uv"
if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
uv --version

say "Installing a real Python 3.12 (managed by uv, not Apple)"
uv python install 3.12

# ---------------------------------------------------------------- 2. Remove old venvs
say "Removing the old Python 3.9 venvs"
FREED=$(du -ch ./*/.venv 2>/dev/null | tail -1 | awk '{print $1}' || echo 0)
find . -maxdepth 4 -type d -name ".venv" -not -path "./.venv" -print -exec rm -rf {} + 2>/dev/null || true
rm -rf _superseded .writetest2 2>/dev/null || true
ok "freed ~${FREED}"

# ---------------------------------------------------------------- 3. Restructure
say "Restructuring into days/<block>/Day 0NN Topic/"

mkdir -p days
shopt -s nullglob
for d in "Day "*; do
  [ -d "$d" ] || continue

  num=$(printf '%s' "$d" | sed -E 's/^Day 0*([0-9]+).*/\1/')
  case "$num" in ''|*[!0-9]*) echo "    skip (no day number): $d"; continue ;; esac

  rest=$(printf '%s' "$d" | sed -E 's/^Day [0-9]+[[:space:]]*//')
  rest=$(printf '%s' "$rest" \
          | sed -e 's/:/-/g'            `# a colon shows as / in Finder and breaks paths` \
                -e 's/sturcturing/structuring/' \
                -e 's/[[:space:].]*$//' `# trailing dots and spaces` )

  start=$(( ((num - 1) / 50) * 50 + 1 ))
  end=$(( start + 49 ))
  block=$(printf 'days/%03d-%03d' "$start" "$end")
  new=$(printf '%s/Day %03d %s' "$block" "$num" "$rest")

  mkdir -p "$block"
  [ -e "$new" ] && { echo "    skip (target exists): $new"; continue; }
  git mv "$d" "$new" 2>/dev/null || mv "$d" "$new"
  printf '    %s\n      -> %s\n' "$d" "$new"
done
shopt -u nullglob

if [ -d "1.2 notes in gerneral" ] && [ ! -e "1.2 notes in general" ]; then
  git mv "1.2 notes in gerneral" "1.2 notes in general" 2>/dev/null \
    || mv "1.2 notes in gerneral" "1.2 notes in general"
  ok "1.2 notes in gerneral -> 1.2 notes in general"
fi

# ---------------------------------------------------------------- 4. The one environment
say "Building .venv  (one environment, shared by every day)"
uv venv .venv --python 3.12
uv pip compile requirements.in --python-version 3.12 -o requirements.txt -q
uv pip install --python .venv/bin/python -r requirements.txt -q
ok "$(uv pip list --python .venv/bin/python 2>/dev/null | tail -n +3 | wc -l | tr -d ' ') packages, $(du -sh .venv | awk '{print $1}')"

# ---------------------------------------------------------------- 5. Clean the git index
say "Untracking files that regenerate themselves"
git ls-files | grep -iE '(DS_Store|\.db$|\.sqlite3?$|\.log$|\.joblib$|\.pkl$)' \
  | while IFS= read -r f; do
      git rm --cached -q -- "$f" 2>/dev/null && printf '    %s\n' "$f"
    done
find . -name .DS_Store -not -path "./.git/*" -delete 2>/dev/null || true
ok "the files stay on disk; git just stops tracking them"

# ---------------------------------------------------------------- 6. Dockerfile casing
say "Renaming 'dockerfile' -> 'Dockerfile'"
find days -maxdepth 3 -name dockerfile -type f | while IFS= read -r f; do
  dir=$(dirname "$f")
  mv "$f" "$dir/Dockerfile.tmp" && mv "$dir/Dockerfile.tmp" "$dir/Dockerfile"
  printf '    %s/Dockerfile\n' "$dir"
done

# ---------------------------------------------------------------- 7. Repair path references
say "Repairing path references broken by the renames"

if [ -d .vscode ]; then
  sed -i '' 's|Day 03 sturcturing git|days/001-050/Day 003 structuring git|g' .vscode/*.json 2>/dev/null || true
  sed -i '' 's|"\*\*/\.venv": true|"**/.venv": true|' .vscode/settings.json 2>/dev/null || true
  ok ".vscode/launch.json + settings.json"
fi

# Day 016 loads Day 003's app by path. It walked up 2 levels, but the file sits
# two directories deep (Day 016/src/server.py), so it needed 3 -- already broken.
# In the new layout its sibling day is in the same block folder, so parents[2] is
# now the correct anchor.
S016=$(find days -maxdepth 3 -path "*Day 016*" -name server.py 2>/dev/null | head -1)
if [ -n "${S016:-}" ]; then
  python3 - "$S016" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text()
t = t.replace('Path(__file__).resolve().parent.parent', 'Path(__file__).resolve().parents[2]')
t = t.replace('"Day 03 sturcturing git"', '"Day 003 structuring git"')
p.write_text(t); print("    " + str(p))
PY
fi

grep -rlE 'sturcturing|gerneral|async:await' \
     --include='*.py' --include='*.txt' --include='*.ini' --include='*.md' . 2>/dev/null \
  | grep -v '/\.venv/' | while IFS= read -r f; do
      sed -i '' -e 's|Day 03 sturcturing git|Day 003 structuring git|g' \
                -e 's|1.2 notes in gerneral|1.2 notes in general|g' \
                -e 's|(async:await)|(async-await)|g' "$f"
      printf '    %s\n' "$f"
    done

# ---------------------------------------------------------------- Done
say "Done"
cat <<'EOF'

  Activate:   source .venv/bin/activate
  Verify:     python -V     # must say 3.12.x, not 3.9.6

  VS Code: Cmd+Shift+P -> "Python: Select Interpreter" -> ./.venv/bin/python
  Do that once and it sticks for every day.

  Day 31 onward:
      mkdir -p "days/001-050/Day 031 Your Topic"
      source .venv/bin/activate       # the same env, always

  Need a new library:
      1. add the name to requirements.in
      2. uv pip compile requirements.in -o requirements.txt
      3. uv pip sync --python .venv/bin/python requirements.txt

  Review, then commit:
      git status
      git add -A
      git commit -m "Restructure for 450 days; one Python 3.12 env via uv"

EOF
printf '  Repo size now: %s\n' "$(du -sh . 2>/dev/null | awk '{print $1}')"
printf '  Day folders:   %s\n' "$(find days -maxdepth 2 -mindepth 2 -type d -name 'Day *' | wc -l | tr -d ' ')"
