import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "Customer Purchasing Behaviors.csv"
output_report = "summary_report.md" 
 
def read_csv_file(path):
    return pd.read_csv(path)

def summary_statistics(dataframe, report_file):
    """Display summary statistics for numerical columns in the DataFrame."""
    summary = dataframe.describe().transpose()
    summary['median'] = dataframe.median(numeric_only=True)
    summary['range'] = summary['max'] - summary['min']
    summary['variance'] = dataframe.var(numeric_only=True)

    with open(report_file, 'a', encoding='utf-8') as file:
        file.write("### Summary Statistics\n")
        file.write(summary.to_string())
        file.write("\n\n")

def plot_histograms(dataframe, columns, report_file, bins=20):
    """Plot histograms for specified columns in the DataFrame."""
    plt.figure(figsize=(12, 6))
    dataframe[columns].hist(bins=bins, edgecolor='black', figsize=(14, 8))
    plt.suptitle('Distribution of age, annual income, purchase amount, and purchase frequency')
    
    plt.savefig("Histogram_column_distributions.png")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write("![Histograms](Histogram_column_distributions.png)\n\n")

def plot_scatter_with_hue(dataframe, x_col, y_col, hue_col, report_file):
    """Visualize the relationship between annual income and purchase amount across different regions."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe, hue=hue_col)
    plt.title(f'{x_col} vs. {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    
    plt.savefig("scatter_plot_hue_by_region.png")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"![{x_col} vs {y_col} with Hue](scatter_plot_hue_by_region.png)\n\n")

def plot_box_by_category(dataframe, x_col, y_col, report_file):
    """Compare the distribution of loyalty scores across different regions."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_col, y=y_col, data=dataframe)
    plt.title(f'{y_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.savefig("Loyalty_score_by_region_boxplot.png")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"![{y_col} by {x_col}](Loyalty_score_by_region_boxplot.png)\n\n")

def plot_correlation_heatmap(dataframe, columns, report_file):
    """Visualize the correlation matrix between purchase amount, purchase frequency, and loyalty score."""
    plt.figure(figsize=(8, 6))
    corr_matrix = dataframe[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')

    plt.savefig("Correlation_matrix_columns.png")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write("![Correlation Matrix](Correlation_matrix_columns.png)\n\n")

def plot_scatter_with_trend(dataframe, x_col, y_col, report_file):
    """Visualize the relationship between annual income and purchase amount with a trend line."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe)
    sns.regplot(x=x_col, y=y_col, data=dataframe, scatter=False, color='red')
    plt.title(f'{x_col} vs. {y_col} with Trend Line')
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.savefig("scatter_plot_trend_line.png")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"![{x_col} vs {y_col} with Trend](scatter_plot_trend_line.png)\n\n")

def plot_bar_by_category(dataframe, category_col, value_col, report_file):
    """Compare average purchase amounts by region."""
    plt.figure(figsize=(10, 6))
    dataframe.groupby(category_col)[value_col].mean().plot(kind='bar')
    plt.title(f'Average {value_col} by {category_col}')
    plt.xlabel(category_col)
    plt.ylabel(f'Average {value_col}')

    plt.savefig("bar_plot_average_purchase_amt_by_regions.png")
    with open(report_file, 'a', encoding='utf-8') as file:
        file.write(f"![Average {value_col} by {category_col}](bar_plot_average_purchase_amt_by_regions.png)\n\n")

# Reading the data
df = read_csv_file(file_path)

# Writing summary statistics to the summary report file
summary_statistics(df, output_report)

# Generating plots and saving them in the summary report file
plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], output_report)
plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region', output_report)
plot_box_by_category(df, 'region', 'loyalty_score', output_report)
plot_correlation_heatmap(df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'], output_report)
plot_scatter_with_trend(df, 'annual_income', 'purchase_amount', output_report)
plot_bar_by_category(df, 'region', 'purchase_amount', output_report)
