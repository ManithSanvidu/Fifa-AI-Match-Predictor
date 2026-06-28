from sklearn.metrics import(
    accuracy_score,
    classification_report,
    confusion_matrix
)

def evaluate_model(model,X_test,y_test):
    predictions=model.predict(X_test)

    accuracy=accuracy_score(y_test,predictions)

    accuracy=accuracy_score(y_test,predictions)


    print("\n==============================")
    print("MODEL EVALUATION")
    print("==============================")

    print(f"Accuracy: {accuracy:.4f}")

    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_test, predictions))

    return accuracy