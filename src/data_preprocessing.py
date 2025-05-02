import os
import pandas as pd

RAW_DATA_PATH = "data/raw/listings.csv"
PROCESSED_DATA_PATH = "data/processed/listings_cleaned.csv"


def clean_price_column(df):
    df["price"] = df["price"].replace("[\$,]", "", regex=True).astype(float)
    return df


def preprocess_data():
    print("Loading data...")
    df = pd.read_csv(RAW_DATA_PATH)

    print("Initial shape:", df.shape)

    # Drop unnecessary columns
    drop_cols = [
        "listing_url",
        "scrape_id",
        "last_scraped",
        "description",
        "neighborhood_overview",
    ]
    df.drop(
        columns=[col for col in drop_cols if col in df.columns],
        inplace=True,
        errors="ignore",
    )

    # Clean price
    if "price" in df.columns:
        df = clean_price_column(df)
        df = df[df["price"] > 0]

    # Drop rows with missing price
    df = df.dropna(subset=["price"])

    # Fill or drop other NA fields
    df = df.dropna(axis=1, thresh=int(0.5 * len(df)))

    print("Final shape after cleaning: ", df.shape)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Cleaned data saved to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    preprocess_data()
