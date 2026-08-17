#!/usr/bin/env bash
#
# Finishes the steps setup_env.sh exited before completing.
# Idempotent - safe to run more than once.
#
set -uo pipefail        # deliberately NOT -e: loops below may return non-zero

REPO="$HOME/Desktop/Aryan Space/Gods-Plan"
cd "$REPO" || exit 1

say() { printf '\n\033[1;36m==> %s\033[0m\n' "$1"; }
ok()  { printf '    \033[0;32mok\033[0m %s\n' "$1"; }

# ---------------------------------------------------------------- 0. Clear stale lock
say "Clearing stale git lock"
if [ -f .git/index.lock ]; then
  rm -f .git/index.lock && ok "removed .git/index.lock"
else
  ok "none present"
fi

# ---------------------------------------------------------------- 1. Finish untracking
say "Finishing the .DS_Store cleanup"
git ls-files | grep -i 'DS_Store' > /tmp/_ds.txt 2>/dev/null
if [ -s /tmp/_ds.txt ]; then
  while IFS= read -r f; do
    git rm --cached -q -- "$f" 2>/dev/null && printf '    untracked: %s\n' "$f"
  done < /tmp/_ds.txt
else
  ok "nothing left tracked"
fi
rm -f /tmp/_ds.txt
find . -name .DS_Store -not -path "./.git/*" -delete 2>/dev/null
ok "deleted from disk"

# ---------------------------------------------------------------- 2. Dockerfile casing
say "Renaming 'dockerfile' -> 'Dockerfile'"
found=0
while IFS= read -r f; do
  [ -n "$f" ] || continue
  dir=$(dirname "$f")
  mv "$f" "$dir/Dockerfile.tmp" && mv "$dir/Dockerfile.tmp" "$dir/Dockerfile"
  printf '    %s/Dockerfile\n' "$dir"
  found=1
done < <(find days -maxdepth 3 -name dockerfile -type f 2>/dev/null)
[ "$found" -eq 0 ] && ok "already named Dockerfile"

# ---------------------------------------------------------------- 3. VS Code paths
say "Updating .vscode paths"
if [ -d .vscode ]; then
  sed -i '' 's|Day 03 sturcturing git|days/001-050/Day 003 structuring git|g' .vscode/*.json 2>/dev/null
  grep -ho 'days/001-050[^"]*' .vscode/*.json 2>/dev/null | sort -u | sed 's/^/    /'
  ok ".vscode updated"
else
  ok "no .vscode dir"
fi

# ---------------------------------------------------------------- 4. Day 016 import fix
say "Repairing the Day 016 -> Day 003 import"
S016=$(find days -maxdepth 4 -path "*Day 016*" -name server.py 2>/dev/null | head -1)
if [ -n "${S016:-}" ]; then
  python3 - "$S016" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = old = p.read_text()
t = t.replace('Path(__file__).resolve().parent.parent',
              'Path(__file__).resolve().parents[2]')
t = t.replace('"Day 03 sturcturing git"', '"Day 003 structuring git"')
if t != old:
    p.write_text(t); print("    patched:", p)
else:
    print("    already correct:", p)
PY
else
  echo "    Day 016 server.py not found"
fi

# ---------------------------------------------------------------- 5. Any other stale refs
say "Sweeping for other references to old folder names"
while IFS= read -r f; do
  [ -n "$f" ] || continue
  sed -i '' -e 's|Day 03 sturcturing git|Day 003 structuring git|g' \
            -e 's|1.2 notes in gerneral|1.2 notes in general|g' \
            -e 's|(async:await)|(async-await)|g' "$f"
  printf '    %s\n' "$f"
done < <(grep -rlE 'sturcturing|gerneral|async:await' \
           --include='*.py' --include='*.txt' --include='*.ini' --include='*.md' . 2>/dev/null \
         | grep -v '/\.venv/')

# ---------------------------------------------------------------- Verify
say "Verification"
printf '  Python:        %s\n' "$(.venv/bin/python -V 2>&1)"
printf '  Interpreter:   %s\n' "$(.venv/bin/python -c 'import sys; print(sys.executable)')"
printf '  Old venvs:     %s left\n' "$(find . -maxdepth 4 -name pyvenv.cfg -not -path './.venv/*' 2>/dev/null | wc -l | tr -d ' ')"
printf '  Repo size:     %s\n' "$(du -sh . 2>/dev/null | awk '{print $1}')"
printf '  Day folders:   %s\n' "$(find days -mindepth 2 -maxdepth 2 -type d -name 'Day *' 2>/dev/null | wc -l | tr -d ' ')"
printf '  DS_Store:      %s tracked\n' "$(git ls-files | grep -ci DS_Store)"

say "Next"
cat <<'EOF'
  git status
  git add -A && git commit -m "Finish restructure: Dockerfile casing, path repairs"
EOF
