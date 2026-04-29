from services import DatasetIndexer
import pandas as pd


def test_dataset_indexer() -> None:
    """Test that the DatasetIndexer correctly builds a DataFrame from the dataset."""

    indexer = DatasetIndexer()
    df = indexer.build_dataframe()

    assert not df.empty, "DataFrame should not be empty"
    assert all(
        col in df.columns
        for col in ["file_path", "label", "width", "height", "channels"]
    ), "Missing expected columns"
    assert (
        df["file_path"]
        .apply(lambda x: x.endswith((".jpg", ".jpeg", ".png", ".bmp")))
        .all()
    ), "All file paths should be valid image formats"

    print(df)

    print(df["label"].value_counts().index)


if __name__ == "__main__":
    test_dataset_indexer()
