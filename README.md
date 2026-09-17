# Phitron AI/ML Learning Repository

This repository contains coursework, practice problems, mini-projects, and datasets from the **Phitron AI/ML** learning path. It is organized into two main tracks:

- **AI Programming With Python**
- **Machine Learning**

The materials are primarily Jupyter notebooks (`.ipynb`) with supporting Python scripts, datasets, and a few Streamlit applications.

## Repository Structure

```text
Phitron-AI-ML/
├── AI Programming With Python/
│   ├── Introduction-to-Python-and-Machine-Learning/
│   ├── Week01/
│   ├── Week02/
│   ├── Week03/
│   └── Week04/
└── Machine Learning/
    ├── Week01/
    ├── Week02/
    ├── Week03/
    ├── Week04/
    ├── Week05/
    └── Week06/
```

## What’s Inside

### 1) AI Programming With Python

This track starts from Python fundamentals and gradually moves into data handling and visualization.

- **Introduction-to-Python-and-Machine-Learning**
  - Intro notebook modules on operators, indexing/slicing, tuples
  - Multiple beginner Python problem-solving scripts (`problem01.py` ... `problem19.py`)

- **Week01**
  - Functions, file handling, and functional programming concepts (`lambda`, `map`, `filter`, `reduce`)
  - Text-based practice tasks and small utility scripts

- **Week02**
  - OOP practice and conceptual notebooks
  - Streamlit practice apps (input/media handling, profile/info cards, text styling)
  - Gemini API-integrated mini-projects:
    - AI Code Debugger
    - Note Summary + Quiz Generator

- **Week03**
  - NumPy and Pandas modules with practice notebooks
  - Tabular data exercises (`student_data.csv`, `student_scores.csv`, etc.)

- **Week04**
  - Data filtering and visualization with Matplotlib/Seaborn
  - Multiple CSV files for plotting and exploratory analysis

### 2) Machine Learning

This track focuses on practical ML workflows from EDA to supervised and unsupervised learning.

- **Week01**
  - EDA foundations, multivariate analysis, missing value imputation
  - Titanic-based assignment and practice notebooks

- **Week02**
  - Feature engineering and outlier handling
  - Missing value treatment, encoding, and scaling (including robust scaling)

- **Week03**
  - Linear regression concepts and implementation from scratch
  - Assignment work and student/advertising datasets

- **Week04**
  - Logistic regression and model selection practice (including GridSearchCV tasks)

- **Week05**
  - Random Forest, SVM, DBSCAN practice notebooks

- **Week06**
  - K-Means and DBSCAN clustering practice
  - Final ML evaluation notebook

## Datasets & File Types

Across both tracks, you will find:

- **Notebooks** (`.ipynb`) for lecture/practice flow
- **Python scripts** (`.py`) for coding exercises and app logic
- **Datasets** (`.csv`, `.xlsx`) for analysis/modeling
- **Supporting resources** (`.pdf`, `.docx`, media files)

## Getting Started

### Prerequisites

- Python 3.10+
- Jupyter Notebook or JupyterLab
- (Optional) Streamlit for app-based modules

### Install dependencies for Streamlit + Gemini projects

Use either requirements file from Week02 (both are similar):

```bash
pip install -r "AI Programming With Python/Week02/Module07/requirements.txt"
```

### Environment variables (for Gemini API projects)

Create a `.env` file in the relevant app folder and set:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run a Streamlit app

Example:

```bash
cd "AI Programming With Python/Week02/Module07"
streamlit run app.py
```

## Notes

- This repo is learning-oriented, so many notebooks include guided exercises, assignments, and exploratory outputs.
- Some folders contain duplicated-style practice content to reinforce concepts across modules.
- If you are reviewing progress, start with week folders in order for each track.
