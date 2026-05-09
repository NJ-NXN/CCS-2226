import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    print("1. Downloading/Loading MNIST Dataset...")
    # fetch_openml downloads the dataset. 'as_frame=False' keeps the data as numpy arrays.
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    
    # X contains the image pixel data (70,000 images, each 784 pixels / 28x28)
    # y contains the actual labels (the numbers 0-9)
    X, y = mnist.data, mnist.target
    print(f"Dataset loaded! Total images: {X.shape[0]}")

    print("\n2. Preparing data for training...")
    # Normalize the pixel values from 0-255 to 0.0-1.0 to help the model learn better
    X = X / 255.0 

    # Split the data: 80% for training the model, 20% for testing its accuracy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set size: {X_train.shape[0]} images")
    print(f"Testing set size: {X_test.shape[0]} images")

    print("\n3. Training the Random Forest Classifier...")
    # Initialize the model (100 decision trees)
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    
    # Train the model using training data
    model.fit(X_train, y_train)
    print("Training complete!")

    print("\n4. Testing the model...")
    # Ask the model to predict the numbers for the test set
    y_pred = model.predict(X_test)
    
    # Calculate how many it got right
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%\n")
    
    # Print a detailed report of precision for each digit (0-9)
    print("Detailed Classification Report:")
    print(classification_report(y_test, y_pred))

    print("\n5. Visualizing some predictions...")
    # visualize the first 5 test images and see what the model guessed
    fig, axes = plt.subplots(1, 5, figsize=(15, 3))
    for i in range(5):
        # Reshape the 784-pixel flat array back into a 28x28 image grid
        image = X_test[i].reshape(28, 28)
        actual_label = y_test[i]
        predicted_label = y_pred[i]
        
        axes[i].set_title(f"Predicted: {predicted_label}\nActual: {actual_label}")
        axes[i].imshow(image, cmap='gray')
        axes[i].axis('off')
        
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()