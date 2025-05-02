import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

INPUT_PATH = "data/processed/listings_cleaned.csv"
OUTPUT_PATH = "data/processed/features.cvs"


def select_features(df):
    selected_columns = [
        "price",
        "room_type",
        "neighbourhood",
        "availability_365",
        "number_of_reviews",
        "reviews_per_month",
        "minimum_nights",
        "latitude",
        "longitude",
    ]
    return df[selected_columns].copy()


def engineer_features(df):
    # Handle missing values
    # df = df.dropna(subset=["review_scores_rating"])

    # One-hot encode categorial features
    categorical_cols = ["room_type", "neighbourhood"]
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Standardize numerical features (excluding target and coordinates)
    numeric_cols = [
        "availability_365",
        "number_of_reviews",
        # "review_scores_rating",
        "minimum_nights",
    ]

    scaler = StandardScaler()
    df_encoded[numeric_cols] = scaler.fit_transform(df_encoded[numeric_cols])

    return df_encoded


def save_features(df):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Feature-enginered data saved t")


def main():
    print("Loading cleaned data...")
    df = pd.read_csv(INPUT_PATH)
    print("Initial shape: ", df.shape)

    df = select_features(df)
    print("After selection: ", df.shape)

    df_fe = engineer_features(df)
    print("After feature engineering: ", df_fe.shape)

    save_features(df_fe)


if __name__ == "__main__":
    main()
