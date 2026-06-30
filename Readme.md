# Cricket Batsman Ranker: Player Segmentation using K-Means Clustering

## Project Overview

This project applies K-Means Clustering to cricket player statistics to segment batsmen into distinct performance groups. By analyzing key batting metrics, the model identifies players with similar performance patterns, enabling comparative analysis and player profiling. This approach helps in understanding different player archetypes (e.g., aggressive hitters, consistent performers, specialists) within the sport.

## Features

- Data Cleaning and Preprocessing: Handle missing values, duplicates, and data inconsistencies
- Feature Engineering: Calculate career experience and derive meaningful metrics
- Outlier Analysis: Identify and handle anomalies in player statistics
- Feature Scaling: Normalize data using StandardScaler for optimal clustering
- Optimal Cluster Selection:
  - Elbow Method for determining optimal cluster count
  - Silhouette Score analysis for cluster quality assessment
- K-Means Clustering: Segment players into homogeneous groups
- 2D and 3D Visualization: Interactive and static cluster visualizations using Plotly and Matplotlib

## Tech Stack

- Python 3.13
- Pandas - Data manipulation and analysis
- NumPy - Numerical computations
- Scikit-Learn - Machine learning (K-Means, preprocessing)
- Matplotlib & Seaborn - Statistical visualizations
- Plotly - Interactive 3D visualizations
- Jupyter Notebook - Interactive development environment
- opencv
## Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

## Installation & Setup

1. Clone the repository
   ```bash
   git clone https://github.com/ashutoshkarspacex-cmd/Cricket_Batsman_Ranker.git
   cd Cricket_Batsman_Ranker
   ```

2. Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn plotly jupyter
   ```

3. Launch Jupyter Notebook
   ```bash
   jupyter notebook
   ```

4. Run the analysis
   - Open the main notebook file
   - Execute all cells sequentially to reproduce the analysis

## Project Structure

```
Cricket_Batsman_Ranker/
├── Readme                          # Project documentation
├── requirements.txt               # Python dependencies
├── Cricket_Batsman_Ranker.ipynb   # Main analysis notebook
├── data/                          # Dataset files
│   └── cricket_players.csv        # Cricket player statistics
└── outputs/                       # Generated visualizations and results
    ├── elbow_curve.png           # Elbow method plot
    ├── silhouette_plot.png       # Silhouette score analysis
    └── cluster_visualization.html # Interactive 3D cluster plot
```

## Dataset

- Source: Cricket player statistics database
- Records: Multiple professional cricket batsmen
- Key Features:
  - Runs scored
  - Batting average
  - Strike rate
  - Number of innings
  - Wickets lost
  - Career span (for experience calculation)

## Workflow

Data Collection → Data Cleaning → Feature Engineering → Feature Scaling → Cluster Analysis → Visualization & Insights

## Methodology

Why K-Means Clustering?
- Efficient for large datasets
- Simple to interpret and implement
- Effective for identifying player archetypes
- Scalable for performance metrics analysis

Key Steps:
1. Preprocessed cricket statistics data
2. Engineered career experience as a derived feature
3. Scaled features to ensure equal weighting
4. Applied Elbow Method and Silhouette analysis to determine optimal clusters
5. Executed K-Means algorithm with identified cluster count
6. Generated 2D and 3D visualizations for interpretation

## Results

Players were successfully segmented into distinct clusters based on their batting statistics:

- Cluster Distribution: Players grouped by similar performance profiles
- Key Insights:
  - Identification of aggressive batting styles (high strike rate, moderate average)
  - Recognition of consistent performers (high average, lower strike rate)
  - Discovery of specialist categories based on career metrics
  - Outlier detection revealing unique player profiles
- Silhouette Score: Validates cluster quality and separation
- Elbow Point: Confirmed optimal number of clusters for the dataset
- Visualization: 2D and 3D interactive plots showcase cluster boundaries and player positions

## How to Use

1. Modify Input Data: Replace data/cricket_players.csv with your dataset
2. Adjust Parameters: Edit cluster count, features, or scaling methods in the notebook
3. Regenerate Analysis: Re-run cells to create new clusters and visualizations
4. Export Results: Save cluster assignments and visualizations for reporting

## Example Insights

The clustering analysis reveals patterns such as:
- Players grouped by batting style (aggressive vs. conservative)
- Career experience impact on performance metrics
- Performance tier classification (elite, intermediate, developing)
- Identification of comparable players for benchmarking

## License

This project is open source and available under the MIT License.

## Author

Ashutosh Kar
- GitHub: https://github.com/ashutoshkarspacex-cmd

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements or new features.

Last Updated: June 2026
