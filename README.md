# Probability and Statistics Practice

A comprehensive collection of Python scripts and notebooks for practicing probability and statistics concepts. This project covers various statistical topics from basic data visualization to advanced correlation analysis.

## Project Structure

```
Probability and Statistics/
├── README.md                 # Project documentation
├── helpers.py               # Utility functions and statistical calculations
├── requirements.txt         # Python dependencies
├── section-01/             # Data Visualization and Basic Statistics
│   ├── Visualizing data/   # Basic data visualization exercises
│   ├── histogram/          # Histogram creation and analysis
│   ├── line graph and ogives/  # Line graphs and ogive plots
│   ├── steam-and-leaf-plot/    # Stem-and-leaf plot implementations
│   └── two-way tables/     # Two-way frequency table analysis
├── section-02/             # Measures of Central Tendency and Spread
│   ├── measures-of-central-tedency.py  # Mean, median, mode calculations
│   └── measures-of-spread.py         # Range, variance, standard deviation
├── section-03/             # Advanced Statistical Analysis
│   ├── workbook.py         # Comprehensive statistical exercises
│   └── output/             # Generated plots and outputs
└── section-04/             # Data Distributions and Correlation
    ├── covariance.py                     # Covariance calculations
    ├── frequency-polygons-and-desity-curves.py  # Frequency polygons and density curves
    ├── mean-variance-deviation.py        # Mean, variance, and deviation analysis
    ├── normal-distributions-and-z-cores.py     # Normal distributions and z-scores
    ├── p-correlation-coefficient-questions.py   # Pearson correlation exercises
    ├── pearson-correlation-coefficient.py      # Pearson correlation implementation
    ├── symmetric-distributions.py             # Symmetric distribution analysis
    ├── weighted-means-and-grouped-data.py      # Weighted means and grouped data
    ├── workbook.py         # Section 4 exercises and examples
    └── output/             # Generated plots and visualizations
```

## Key Features

### helpers.py
A comprehensive utility module containing:
- **Statistics Class**: Core statistical functions
  - `get_mode()`: Calculate mode of a dataset
  - `get_median()`: Calculate median of a dataset
  - `get_mean()`: Calculate mean of a dataset
  - `get_variance()`: Calculate population/sample variance
  - `get_standard_deviation()`: Calculate standard deviation
  - `get_range()`: Calculate range of data
  - `get_iqr()`: Calculate interquartile range
  - `get_weighted_mean()`: Calculate weighted mean
  - `get_interval_frequencies()`: Calculate frequency distributions
  - `get_list_from_steam_and_leaf()`: Convert stem-and-leaf to list
  - `get_full_list_from_frequency()`: Convert frequency data to full list

- **TemperatureConverter Class**: Temperature conversion utilities
- **Normalizer Class**: Data normalization utilities

### Section Breakdown

#### Section 01: Data Visualization and Basic Statistics
- **Visualizing Data**: Basic plotting and data representation
- **Histograms**: Creating and interpreting histograms
- **Line Graphs and Ogives**: Cumulative frequency plots
- **Stem-and-Leaf Plots**: Alternative data visualization method
- **Two-Way Tables**: Contingency table analysis

#### Section 02: Measures of Central Tendency and Spread
- **Central Tendency**: Mean, median, and mode calculations
- **Measures of Spread**: Range, variance, standard deviation, IQR

#### Section 03: Advanced Statistical Analysis
- Comprehensive workbook covering advanced statistical concepts
- Box plots and whisker plots
- Statistical inference concepts

#### Section 04: Data Distributions and Correlation
- **Covariance**: Measuring joint variability
- **Frequency Polygons**: Advanced frequency visualization
- **Normal Distributions**: Bell curve analysis and z-scores
- **Pearson Correlation**: Linear relationship analysis
- **Symmetric Distributions**: Distribution symmetry analysis
- **Weighted Means**: Advanced mean calculations
- **Grouped Data**: Statistical analysis of grouped datasets

## Dependencies

Install required packages using:
```bash
pip install -r requirements.txt
```

Key dependencies include:
- `matplotlib`: For data visualization and plotting
- `numpy`: For numerical computations
- `pillow`: For image processing
- `contourpy`: For contour plotting
- Various supporting libraries for data manipulation

## Usage

Each section contains standalone Python scripts that can be run independently. Most scripts generate visual outputs saved in the respective `output/` directories.

Example usage:
```python
from helpers import Statistics

# Calculate basic statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = Statistics.get_mean(data)
median = Statistics.get_median(data)
variance = Statistics.get_variance(data)
std_dev = Statistics.get_standard_deviation(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
```

## Output Files

The project generates various output files including:
- PNG plots and charts
- Statistical analysis results
- Frequency distributions
- Correlation matrices

These are typically saved in `output/` subdirectories within each section.

## Contributing

This project is designed for educational purposes and continuous learning. Feel free to extend the existing modules or add new statistical concepts.

## License

This project is for educational and learning purposes.

