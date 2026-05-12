from pathlib import Path

paths = [
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/dataset_summary.csv"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/class_distribution.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/image_size_distribution.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/width_height_scatter.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/sample_image_grid.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/width_by_class_boxplot.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/height_by_class_boxplot.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/pixel_intensity_histogram.png"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/eda/quality_issues.csv"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/class_imbalance_report.md"
    ),
    Path(
        "C:/Users/mitch/Documents/GitHub/ST1-Assessment-3/outputs/stage2_recommendations.md"
    ),
]

file_count = len(paths)
unique_folders = set([folder.parent.name for folder in paths])
unique_folders.add("Folder")

file_count_digits = len(str(file_count))
file_name_max_length = max(len(file.name) for file in paths)
folder_name_max_length = max(len(folder) for folder in unique_folders)

print()
print(
    f"+{(file_count_digits + 2) * '-'}+{(file_name_max_length + 2) * '-'}+{(folder_name_max_length + 2) * '-'}+"
)
print(
    f"| {'#':>{file_count_digits}s} | {'File':{file_name_max_length}s} | {'Folder':{folder_name_max_length}s} |"
)
print(
    f"+{(file_count_digits + 2) * '='}+{(file_name_max_length + 2) * '='}+{(folder_name_max_length + 2) * '='}+"
)
for i in range(len(paths)):
    print(
        f"| {i + 1:{file_count_digits}d} | {paths[i].name:{file_name_max_length}s} | {paths[i].parent.name:{folder_name_max_length}s} |"
    )
    print(
        f"+{(file_count_digits + 2) * '-'}+{(file_name_max_length + 2) * '-'}+{(folder_name_max_length + 2) * '-'}+"
    )
print()
