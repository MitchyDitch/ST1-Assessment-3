from src.services import WorkflowService
from PIL import Image
from pandas import read_csv


class ConsoleApp:
    """Menu-driven console application for the assignment workflow."""

    def __init__(self, workflow_service: "WorkflowService") -> None:
        self.workflow_service = workflow_service

    def run(self) -> None:
        """Start the menu loop until the user chooses to exit."""

        while True:
            print("\nMacroinvertebrate Image Analysis System\n")
            print(" 1 | Generate all EDA outputs")
            print(" 2 | Show dataset summary")
            print(" 3 | Show class distribution")
            print(" 4 | Show image size distribution")
            print(" 5 | Show width vs height scatterplot")
            print(" 6 | Show sample image grid")
            print(" 7 | Show width by class boxplot")
            print(" 8 | Show height by class boxplot")
            print(" 9 | Show pixel intensity histograms")
            print("10 | Show image quality issues")
            print("11 | Show class imbalance report")
            print("12 | Show stage 2 recommendations report")
            print("13 | Exit")

            choice = input("\nSelect an option: ").strip()
            print()

            if choice == "1":
                paths = self.workflow_service.generate_eda()

                file_count = len(paths)
                unique_folders = set([folder.parent.name for folder in paths])
                unique_folders.add("Folder")

                file_count_digits = len(str(file_count))
                file_name_max_length = max(len(file.name) for file in paths)
                folder_name_max_length = max(len(folder) for folder in unique_folders)

                print("EDA outputs generated successfully.\n")
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

            elif choice == "2":
                summary_csv = read_csv(self.workflow_service.show_summary())
                print(summary_csv)

            elif choice == "3":
                dist_img = Image.open(self.workflow_service.show_class_distribution())
                dist_img.show()

            elif choice == "4":
                size_img = Image.open(
                    self.workflow_service.show_image_size_distribution()
                )
                size_img.show()

            elif choice == "5":
                scatter_img = Image.open(
                    self.workflow_service.show_width_vs_height_scatterplot()
                )
                scatter_img.show()

            elif choice == "6":
                sample_img = Image.open(self.workflow_service.show_sample_image_grid())
                sample_img.show()

            elif choice == "7":
                boxplot_img = Image.open(
                    self.workflow_service.show_width_by_class_boxplot()
                )
                boxplot_img.show()

            elif choice == "8":
                boxplot_img = Image.open(
                    self.workflow_service.show_height_by_class_boxplot()
                )
                boxplot_img.show()

            elif choice == "9":
                histogram_img = Image.open(
                    self.workflow_service.show_pixel_intensity_histogram()
                )
                histogram_img.show()

            elif choice == "10":
                quality_csv = read_csv(self.workflow_service.show_quality_issues())
                print(quality_csv)

            elif choice == "11":
                with open(
                    self.workflow_service.show_class_imbalance_report(), "r"
                ) as f:
                    report = f.read()
                print(report)

            elif choice == "12":
                with open(
                    self.workflow_service.show_stage2_recommendations(), "r"
                ) as f:
                    recommendations = f.read()
                print(recommendations)

            elif choice == "13":
                print("Exiting application.\n")
                break

            else:
                print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    workflow = WorkflowService()
    app = ConsoleApp(workflow)
    app.run()
