import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from main import (
    summary_statistics, plot_histograms, plot_scatter_with_hue, 
    plot_box_by_category, plot_correlation_heatmap, plot_scatter_with_trend, 
    plot_bar_by_category
)

sample_data = """customer_id,age,annual_income,purchase_amount,purchase_frequency,region,loyalty_score
1,23,50000,200,5,North,80
2,45,60000,300,7,South,85
3,34,55000,250,6,East,90
4,50,65000,400,8,West,70
5,29,70000,350,7,North,75
"""

# Function to create DataFrame from sample data using StringIO
def setup_dataframe():
    return pd.read_csv(StringIO(sample_data))

def test_summary_statistics():
    """Test summary_statistics function"""
    df = setup_dataframe()
    summary_statistics(df, "test_report.md")
    print("test_summary_statistics passed")

def test_plot_histograms():
    """Test plot_histograms function"""
    df = setup_dataframe()

    # Mock plt.show to prevent actual plotting during tests
    plt.show = lambda: None
    plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], "test_report.md")
    print("test_plot_histograms passed")

def test_plot_scatter_with_hue():
    """Test plot_scatter_with_hue function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region', "test_report.md")
    print("test_plot_scatter_with_hue passed")

def test_plot_box_by_category():
    """Test plot_box_by_category function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_box_by_category(df, 'region', 'loyalty_score', "test_report.md")
    print("test_plot_box_by_category passed")

def test_plot_correlation_heatmap():
    """Test plot_correlation_heatmap function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_correlation_heatmap(df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'], "test_report.md")
    print("test_plot_correlation_heatmap passed")

def test_plot_scatter_with_trend():
    """Test plot_scatter_with_trend function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_scatter_with_trend(df, 'annual_income', 'purchase_amount', "test_report.md")
    print("test_plot_scatter_with_trend passed")

def test_plot_bar_by_category():
    """Test plot_bar_by_category function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_bar_by_category(df, 'region', 'purchase_amount', "test_report.md")
    print("test_plot_bar_by_category passed")

# Run the tests
test_summary_statistics()
test_plot_histograms()
test_plot_scatter_with_hue()
test_plot_box_by_category()
test_plot_correlation_heatmap()
test_plot_scatter_with_trend()
test_plot_bar_by_category()
