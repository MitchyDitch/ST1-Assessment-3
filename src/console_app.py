from services import WorkflowService


class ConsoleApp:
    """Menu-driven console application for the assignment workflow."""

    def __init__(self, workflow_service: "WorkflowService") -> None:
        self.workflow_service = workflow_service

    def run(self) -> None:
        """Start the menu loop until the user chooses to exit."""

        while True:
            print("\nMacroinvertebrate Image Analysis System\n")
            print("1. Show dataset summary")
            print("2. Generate EDA outputs")
            print("3. Train baseline classifier")
            print("4. Predict an image")
            print("5. Exit")

            choice = input("\nSelect an option: ").strip()
            print()

            if choice == "1":
                self.workflow_service.show_summary()
            elif choice == "2":
                self.workflow_service.generate_eda()
            elif choice == "3":
                self.workflow_service.train_model()
            elif choice == "4":
                image_path = input("Enter image path: ").strip()
                self.workflow_service.predict_image(image_path)
            elif choice == "5":
                print("Exiting application.")
                break
            else:
                print("Invalid option. Please try again.")
