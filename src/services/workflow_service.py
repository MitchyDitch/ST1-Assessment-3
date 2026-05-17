import pandas as pd
from pathlib import Path
from src.config import ensure_directories
from .dataset_indexer import DatasetIndexer
from .eda_service import EDAService


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

    def show_summary(self) -> Path:
        """Build and print dataset summary statistics."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        summary = eda.generate_dataset_summary()
        return summary

    def show_class_distribution(self) -> Path:
        """Print the class distribution of the dataset."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        class_dist = eda.generate_class_distribution_chart()
        return class_dist

    def show_image_size_distribution(self) -> Path:
        """Print the image size distribution of the dataset."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        size_dist = eda.generate_image_size_distribution_chart()
        return size_dist

    def show_width_vs_height_scatterplot(self) -> Path:
        """Print a scatterplot of image width vs height."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        scatterplot = eda.generate_width_height_scatter_plot()
        return scatterplot

    def show_sample_image_grid(self) -> Path:
        """Print a grid of representative sample images."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        sample_grid = eda.generate_sample_image_grid()
        return sample_grid

    def show_width_by_class_boxplot(self) -> Path:
        """Print a boxplot of image width by class."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        boxplot = eda.generate_width_by_class_boxplot()
        return boxplot

    def show_height_by_class_boxplot(self) -> Path:
        """Print a boxplot of image height by class."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        boxplot = eda.generate_height_by_class_boxplot()
        return boxplot

    def show_pixel_intensity_histogram(self) -> Path:
        """Print a histogram of pixel intensity distributions."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        histogram = eda.generate_pixel_intensity_histogram()
        return histogram

    def show_quality_issues(self) -> Path:
        """Print a report of image quality issues."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        quality_issues_report = eda.generate_image_quality_issues()
        return quality_issues_report

    def show_class_imbalance_report(self) -> Path:
        """Print a report of class imbalance issues."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        imbalance_report = eda.generate_class_imbalance_report()
        return imbalance_report

    def show_stage2_recommendations(self) -> Path:
        """Print a report of recommendations for Stage 2."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        recommendations_report = eda.generate_stage2_recommendations()
        return recommendations_report

    def generate_eda(self) -> None:
        """Create and save all EDA outputs."""

        self.load_dataframe()
        eda = EDAService(self.dataframe)
        paths = eda.generate_all_outputs()
        return paths

    def run_full_pipeline(self) -> None:
        """Run the default Stage 1 workflow."""

        self.generate_eda()
