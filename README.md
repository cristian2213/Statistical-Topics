# Probability and Statistics Practice

This repository contains Python implementations of statistical concepts and exercises from a probability and statistics textbook. The code is organized by sections and topics, with each file corresponding to specific problems or concepts from the book.

## Repository Structure

```
.
├── section-01/                    # Introduction to Statistics
│   ├── Visualizing data/          # Data visualization exercises
│   │   └── question-1.py          # Ogive plot implementation
│   ├── histogram/                 # Histogram implementations
│   │   ├── question-02.py
│   │   └── question-06.py
│   ├── line graph and ogives/     # Line graphs and ogive curves
│   │   ├── question-02.py
│   │   └── question-05.py
│   ├── steam-and-leaf-plot/       # Stem-and-leaf plot examples
│   │   └── question-06.py
│   └── two-way tables/            # Two-way table analysis
│       ├── question-1.py
│       ├── question-04.py
│       └── question-06.py
│
├── section-02/                    # Basic statistical measures
│   ├── measures-of-central-tendency.py
│   └── measures-of-spread.py
│
└── section-04/                    # Probability distributions
    ├── frequency-polygons-and-density-curves.py
    ├── mean-variance-deviation.py
    ├── normal-distributions-and-z-scores.py
    └── symmetric-distributions.py
```

## Topics Covered

### Section 01: Introduction to Statistics

- Data Visualization
  - Histograms
  - Line Graphs and Ogives
  - Stem-and-Leaf Plots
  - Two-way Tables

### Section 02: Basic Statistical Measures

- Measures of Central Tendency (Mean, Median, Mode)
- Measures of Spread (Range, Variance, Standard Deviation)

### Section 04: Probability Distributions

- Frequency Polygons and Density Curves
- Mean, Variance, and Standard Deviation of Probability Distributions
- Normal Distributions and Z-scores
- Symmetric Distributions

## Requirements

- Python 3.6+
- Standard library modules:
  - `statistics`
  - `math`
  - `collections`
  - `matplotlib` (for visualization)
  - `numpy` (for numerical operations)

## Usage

Each Python file is self-contained and can be run independently. The files are named according to the exercise or concept they implement. For example, to run the normal distributions and z-scores example:

```bash
python section-04/normal-distributions-and-z-scores.py
```

## Notes

- The code includes comments explaining the statistical concepts being implemented.
- Some files may include test cases or example usages at the bottom.
- The implementations are designed for educational purposes and may not be optimized for production use.

## Contributing

This is a personal learning project.
