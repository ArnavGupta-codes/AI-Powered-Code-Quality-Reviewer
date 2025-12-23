# AI-Powered Code Quality Reviewer

A machine learning system that evaluates code quality across multiple dimensions: readability, maintainability, complexity, and security.

## Overview

This project uses Random Forest regression models trained on 218 code samples across three programming languages (C++, Python, Java) to predict code quality metrics on a 0-100 scale.

## Features

- Multi-language support: C++, Python, Java
- Four quality dimensions:
  - Readability (0-100)
  - Maintainability (0-100)
  - Complexity (0-100, lower is better)
  - Security (0-100)
- Automatic language detection
- Feature extraction using static analysis tools

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python3 models/predict.py path/to/your/code.cpp
```

### Output

```
Analysis Results
File: example.cpp
Scores (0-1): 
  readability: 0.821
  maintainability: 0.795
  complexity: 0.456
  security: 0.734
Overall: 0.702
```

## Model Performance

### Accuracy Metrics (5-Fold Cross-Validation)

| Metric | R² | MAE | Std Dev |
|--------|-----|-----|---------|
| Readability | -0.0137 | 17.90 | 0.62 |
| Maintainability | -0.0135 | 18.01 | 0.74 |
| Complexity | 0.0101 | 11.44 | 1.83 |
| Security | 0.0245 | 11.13 | 2.16 |

### Score Ranges

Good Code: 67-91/100
Average Code: 50-65/100
Poor Code: 14-38/100

## Project Structure

```
├── analyzers/
│   ├── cpp_analyzer.py
│   ├── python_analyzer.py
│   └── java_analyzer.py
├── features/
│   └── feature_extractor.py
├── models/
│   ├── train.py
│   ├── predict.py
│   └── saved/
│       ├── readability_rf.pkl
│       ├── maintainability_rf.pkl
│       ├── complexity_rf.pkl
│       └── security_rf.pkl
├── data/
│   ├── labels.csv
│   └── raw/
│       ├── cpp/
│       ├── python/
│       └── java/
└── service/
    └── language_detect.py
```

## Training

To retrain the models with your own data:

```bash
python3 models/train.py
```

The training script:
- Loads code samples from data/labels.csv
- Extracts 11 features per file
- Trains 4 separate Random Forest models (one per quality dimension)
- Uses 5-fold cross-validation for evaluation
- Saves models to models/saved/

## Features Extracted

The system extracts 11 features per code file:

1. Lines of code (normalized)
2. Average cyclomatic complexity
3. Cyclomatic complexity per function
4. Number of functions
5. Average function length
6. Issue density (warnings/LOC)
7. Comment density
8. Token count
9. Average token length
10. Include count
11. Code quality issues

## Language-Specific Analyzers

### C++ (cpp_analyzer.py)
- Uses lizard for complexity analysis
- Runs clang-tidy for warnings
- Runs cppcheck for issues
- Detects unsafe patterns (gets, strcpy, etc.)

### Python (python_analyzer.py)
- Uses pylint for linting
- Uses bandit for security issues
- Uses radon for cyclomatic complexity
- Calculates maintainability index

### Java (java_analyzer.py)
- Uses checkstyle for style issues
- Analyzes cyclomatic complexity
- Extracts token and comment metrics

## Dataset

The training dataset contains 218 code samples:
- 70 C++ files (including 2 extreme examples)
- 70 Python files (including 2 extreme examples)
- 70 Java files (including 2 extreme examples)

Labels are manually assigned quality scores (0-100) for each dimension.

## Recent Improvements

Version 2.0 added:
- 8 extreme code samples (4 excellent, 4 terrible) for better range coverage
- Expanded score range from 60-72 to 14-91
- 5-fold cross-validation for more reliable metrics
- 700 estimator Random Forest (improved from 500)

See SOLUTION_SUMMARY.md for details.

## Requirements

- Python 3.8+
- scikit-learn
- pandas
- numpy
- radon (Python complexity)
- lizard (C++ complexity)
- pylint (Python linting)
- bandit (Python security)
- clang-tidy (C++ static analysis)
- cppcheck (C++ checking)
- checkstyle (Java checking)

## Documentation

- ACCURACY_RESULTS.md - Model performance metrics
- MODEL_IMPROVEMENT_REPORT.md - Technical details
- SOLUTION_SUMMARY.md - Recent improvements and changes

## Future Improvements

1. Collect more training data (target: 500+ samples)
2. Add AST-based feature extraction
3. Implement ensemble learning with multiple algorithms
4. Add more security-specific metrics
5. Support additional languages (Go, Rust, TypeScript)

## License

MIT

## Author

Code Quality Review Team

## Contact

For questions or contributions, please open an issue or submit a pull request.
