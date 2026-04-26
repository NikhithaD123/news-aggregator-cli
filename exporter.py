import pandas as pd

def export_to_csv(articles, filename="news_export"):
    df = pd.DataFrame(articles)
    df.to_csv(f"{filename}.csv", index=False)
    print(f"Saved to {filename}.csv")

def export_to_excel(articles, filename="news_export"):
    df = pd.DataFrame(articles)
    df.to_excel(f"{filename}.xlsx", index=False)
    print(f"Saved to {filename}.xlsx")