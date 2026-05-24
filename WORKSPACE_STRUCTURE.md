Workspace mapping and run notes

- Real application code (FastAPI apps) for the Day 03 project is under:
  - Day 03 sturcturing git/my_ml_project/src/
    - server.py (original app)
    - server1.py (alternate app with header handshake)

- Workspace-level compatibility shim:
  - src/ (proxy) was added at the workspace root to allow `uvicorn src.server:app` to run from the workspace root without changing import paths.

- Recommended commands (from workspace root):

  - Run `server1.py` with explicit app-dir:

    uvicorn --app-dir "Day 03 sturcturing git/my_ml_project" src.server1:app --reload

  - Or change directory and run normally:

    cd "Day 03 sturcturing git/my_ml_project"
    uvicorn src.server1:app --reload

- VS Code conveniences (files added):
  - .vscode/settings.json: adds `Day 03 sturcturing git/my_ml_project` to `python.analysis.extraPaths` for autocompletion and linting.
  - .vscode/launch.json: two Uvicorn launch configurations you can use from the Run view.

- Notes and recommendations:
  - Keep the proxy `src/` only if you frequently run uvicorn from the workspace root; otherwise prefer `--app-dir` or CD into the project folder.
  - If you use a virtual environment, ensure VS Code selects the correct interpreter (bottom-right status bar).
  - Use `curl` or the open Swagger UI at `/docs` to test endpoints.
