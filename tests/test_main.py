from src.main import load_data, process_data

def test_load_data():
    df = load_data("data/dataset.csv")
    assert not df.empty, "Data should not be empty"

def test_process_data():
    import pandas as pd
    raw_data = {"col1": [1, None, 3], "col2": [4, 5, None]}
    df = pd.DataFrame(raw_data)
    processed_df = process_data(df)
    assert processed_df.isnull().sum().sum() == 0, "All missing values should be filled"