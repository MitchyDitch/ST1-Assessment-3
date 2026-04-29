from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
OUTPUTS_DIR = BASE_DIR / "outputs"
EDA_OUTPUT_DIR = OUTPUTS_DIR / "eda"
MODEL_OUTPUT_DIR = OUTPUTS_DIR / "models"

IMAGE_SIZE = (128, 128)
SUPPORTED_IMAGE_FORMATS = {".jpg", ".jpeg", ".png", ".bmp"}


def ensure_directories() -> None:
    """Create necessary output directories if they don't exist."""

    for directory in [EDA_OUTPUT_DIR, MODEL_OUTPUT_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
