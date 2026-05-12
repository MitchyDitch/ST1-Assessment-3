from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
OUTPUTS_DIR = BASE_DIR / "outputs"
EDA_OUTPUT_DIR = OUTPUTS_DIR / "eda"
MODEL_OUTPUT_DIR = OUTPUTS_DIR / "models"
CLASS_IMBALANCE_REPORT_PATH = OUTPUTS_DIR / "class_imbalance_report.txt"
PIXEL_ANALYSIS_SAMPLE_SIZE = 1000
QUALITY_ISSUES_PATH = OUTPUTS_DIR / "quality_issues.txt"
REPORT_OUTPUT_DIR = OUTPUTS_DIR / "reports"
SAMPLE_GRID_MAX_IMAGES = 16
STAGE2_RECOMMENDATIONS_PATH = OUTPUTS_DIR / "stage2_recommendations.txt"
UNUSUAL_ASPECT_RATIO_HIGH = 3.0
UNUSUAL_ASPECT_RATIO_LOW = 0.33
VERY_SMALL_IMAGE_THRESHOLD = 50

IMAGE_SIZE = (128, 128)
SUPPORTED_IMAGE_FORMATS = {".jpg", ".jpeg", ".png", ".bmp"}


def ensure_directories() -> None:
    """Create necessary output directories if they don't exist."""

    for directory in [
        RAW_DATA_DIR,
        EDA_OUTPUT_DIR,
        MODEL_OUTPUT_DIR,
        REPORT_OUTPUT_DIR,
    ]:
        directory.mkdir(parents=True, exist_ok=True)
