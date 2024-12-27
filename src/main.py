from src.data_processing import load_data, process_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model
import joblib

if __name__ == "__main__":
    df = load_data("data/dataset.csv")

    df = process_data(df)

    X = df.drop(columns=["target"])
    y = df["target"]
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)

    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy}")

    joblib.dump(model, "models/model.pkl")
