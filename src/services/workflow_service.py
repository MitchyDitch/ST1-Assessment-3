import pandas as pd
from config import EDA_OUTPUT_DIR, ensure_directories
from services.dataset_indexer import DatasetIndexer
from services.eda_service import EDAService


class WorkflowService:
    """Coordinate the shared workflow used by batch, GUI, and console entry points."""

    def __init__(self) -> None:
        ensure_directories()

        self.indexer = DatasetIndexer()
        self.dataframe: pd.DataFrame | None = None

    def load_dataframe(self) -> None:
        """Load and cache the indexed dataset."""

        if self.dataframe is None:
            self.dataframe = self.indexer.build_dataframe()

    def show_summary(self) -> dict[str, float]:
        """Build and print dataset summary statistics."""

        self.load_dataframe()
        eda = EDAService(self.dataframe, EDA_OUTPUT_DIR)
        summary = eda.build_summary()
        return summary

    def generate_eda(self) -> None:
        """Create and save the main EDA outputs."""

        self.load_dataframe()
        eda = EDAService(self.dataframe, EDA_OUTPUT_DIR)
        eda.save_class_distribution()
        eda.save_image_size_distribution()

    def run_full_pipeline(self) -> None:
        """Run the default Stage 1 workflow."""

        self.show_summary()
        self.generate_eda()
