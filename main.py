import click
from fetcher import fetch_news
from storage import save_to_sqlite, save_to_json, load_from_sqlite
from exporter import export_to_csv, export_to_excel

@click.group()
def cli():
    """📰 News Aggregator CLI"""
    pass

@cli.command()
@click.option("--keyword", "-k", default="technology", help="Search keyword")
@click.option("--source", "-s", default=None, help="News source (e.g. bbc-news)")
@click.option("--date", "-d", default=None, help="From date (YYYY-MM-DD)")
def fetch(keyword, source, date):
    """Fetch and store news articles."""
    articles = fetch_news(keyword, source, date)
    save_to_sqlite(articles)
    save_to_json(articles)
    click.echo(f"✅ Fetched and stored {len(articles)} articles.")

@cli.command()
@click.option("--format", "-f", type=click.Choice(["csv","excel"]), default="csv")
@click.option("--output", "-o", default="news_export")
def export(format, output):
    """Export stored news to CSV or Excel."""
    articles = load_from_sqlite()
    if format == "csv":
        export_to_csv(articles, output)
    else:
        export_to_excel(articles, output)

if __name__ == "__main__":
    cli()