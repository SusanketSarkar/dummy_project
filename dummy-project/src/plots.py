import matplotlib.pyplot as plt

def plot_feature_distribution(df, column):
    """Plots a histogram of the given column."""
    df[column].hist(bins=20)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
