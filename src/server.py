from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_app_path = (
    Path(__file__).resolve().parent.parent
    / "Day 03 sturcturing git"
    / "my_ml_project"
    / "src"
    / "server.py"
)

_spec = spec_from_file_location("my_ml_project_server", _app_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Cannot load app from {_app_path}")

_module = module_from_spec(_spec)
_spec.loader.exec_module(_module)
app = _module.app
