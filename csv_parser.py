import pandas as pd
import matplotlib.pyplot as plt
import click

@click.group()
def cli():
    '''Can display and plot csv files'''
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    '''Displays the column names and their data types'''
    df = pd.read_csv(filename)
    print(df.dtypes)

@cli.command()
@click.argument('filename')
@click.option('--column', default=None)
def plot(filename, column):
    '''Plots a histogram of a column of the csv'''
    df = pd.read_csv(filename)
    if column is None:
        df.hist()
    else:
        df[column].hist()
        plt.title(column)
    plt.show()
    
if __name__ == '__main__':
    cli()

