import pandas as pd

def summary_stats(data):
    if not data:
        return {
            "total": 0,
            "operations": 0,
            "max": 0,
            "min": 0,
            "avg": 0
        }

    df = pd.DataFrame(data)

    return {
        "total": round(df["amount"].sum(), 2),
        "operations": len(df),
        "max": df["amount"].max(),
        "min": df["amount"].min(),
        "avg": round(df["amount"].mean(), 2)
    }


def build_dataframe(data):
    if not data:
        return pd.DataFrame(columns=["file", "client", "amount"])

    return pd.DataFrame(data)


def totals_by_client(data):
    df = build_dataframe(data)
    return df.groupby("client")["amount"].sum().reset_index()
