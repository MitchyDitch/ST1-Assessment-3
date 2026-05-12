# from config import MODEL_OUTPUT_DIR
from services import WorkflowService
# from app import MacroApp
# from utils import plotting


def main() -> None:
    """Run the default non-interactive project workflow."""

    workflow = WorkflowService()
    workflow.run_full_pipeline()
    # plotting.save_sample_grid(workflow.dataframe, MODEL_OUTPUT_DIR / "sample_grid.png")
    # app = MacroApp(workflow, MODEL_OUTPUT_DIR / "macro_classifier.joblib")
    # app.mainloop()


if __name__ == "__main__":
    main()
