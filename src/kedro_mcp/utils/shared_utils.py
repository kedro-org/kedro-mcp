import os
from pathlib import Path

from dotenv import load_dotenv


def get_kedro_project_path() -> Path:
    """Get Kedro project path from env variable."""
    # temp dev block
    project_root = Path(__file__).parent.parent.parent.parent
    load_dotenv(dotenv_path=project_root / ".env")

    proj_path = os.environ.get("KEDRO_PROJECT_PATH")

    if not proj_path:
        raise OSError("KEDRO_PROJECT_PATH environment variable not set")

    path = Path(proj_path)

    if not path.exists() or not path.is_dir():
        raise FileNotFoundError(
            f"Kedro project path '{proj_path}' does not exist or is not a directory"
        )

    return path
