# eda_utils.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


def load_csv(file_path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    df = pd.read_csv(file_path)
    print(f"✅ Loaded {file_path} with shape {df.shape}")
    return df


def descriptive_stats(df: pd.DataFrame) -> dict:
    """Return descriptive statistics as dictionary."""
    return df.describe(include="all").transpose().fillna("").to_dict()


def missing_values(df: pd.DataFrame) -> dict:
    """Return missing values (%) per column."""
    missing = (df.isnull().sum() / len(df) * 100).round(2)
    return missing[missing > 0].to_dict()


def correlation_matrix(df: pd.DataFrame) -> str:
    """Return correlation heatmap as base64 image string."""
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(8, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


def quick_info(df: pd.DataFrame) -> str:
    """Return DataFrame info as string."""
    buffer = io.StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()


def run_full_eda(df: pd.DataFrame) -> dict:
    """Run full EDA pipeline and return structured results."""
    return {
        "info": quick_info(df),
        "descriptive_stats": descriptive_stats(df),
        "missing_values": missing_values(df),
        "correlation_matrix": correlation_matrix(df)
    }
