import pandas as pd

def summary_stats(data):
    if not data:
        return {"total": 0, "operations": 0}

    df = pd.DataFrame(data)

    return {
        "total": df["amount"].sum(),
        "operations": len(df)
    }
