def load_data(filepath):
    return pd.read_csv(filepath)

def process_data(df):
    df = df.fillna(0)
    return df