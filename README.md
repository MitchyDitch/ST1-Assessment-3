# Macroinvertebrate Image Analysis System in Python

## Project Goal
The main purpose of this project is to develop a Python-based application to identify and analyse freshwater macroinvertebrates using the image-based data which is related to the classification, organisation, processing, visualisation, or analysis of macroinvertebrate image data. Freshwater macroinvertebrates consist of small aquatic organisms such as insect-larvae, worms, snails and crustaceans. This project aims to:
- design software using objects and classes
- process and manage data in a structured way
- apply appropriate Python libraries to solve practical problems
- present results clearly through outputs or visualisations
- produce readable, maintainable, and well-documented code

## Main Features
- Dataset indexing
- EDA including:
  - Dataset summary
  - Class distribution
  - Image property charts
  - Sample images
  - image quality report
  - class imbalance report
  - Predictive analysis recommendations

## Packages Used
- matplotlib
- numpy
- opencv-python
- pandas
- pillow
- seaborn

## How to Install and Run
1. Install dependencies with 'pip install -r requirements.txt'
2. Place the dataset inside 'data/raw'
3. Run 'python -m src.main'
4. Run 'python -m src.console_app' for the console-driven version

## Folder Structure

```
macro-project/
|-- data/
|   |-- raw/
|-- outputs/
|   |--eda/
|   |--reports/
|-- src/
|   |-- models/
|   |   |-- records.py
|   |-- services/
|   |   |-- __init__.py
|   |   |-- dataset_indexer.py
|   |   |-- eda_service.py
|   |   |-- workflow_service.py
|   |-- app.py
|   |-- config.py
|   |-- console_app.py
|   |-- main.py
|-- .gitignore
|-- README.md
|-- requirements.txt
```
