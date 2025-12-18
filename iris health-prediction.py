import tkinter as tk
from tkinter import filedialog, Label, Button, Canvas
from PIL import Image, ImageTk
import random

def upload_image():
    global img_tk
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path).resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(125, 125, image=img_tk)
        analyze_button.config(state=tk.NORMAL)

def analyze_iris():
    loading_label.config(text="Analyzing... Please wait...")
    root.after(2000, display_results)  # Simulate processing delay

def display_results():
    iris_features = {
        "Iris Color Intensity": random.randint(40, 100),
        "Crypts Density": random.randint(30, 90),
        "Collarette Structure": random.randint(20, 80),
        "Vessel Tortuosity": random.randint(10, 70),
        "Contraction Furrows": random.randint(15, 85)
    }

    # Simulated heart disease prediction
    heart_risk_score = sum(iris_features.values()) // len(iris_features)
    heart_risk_level = "Low Risk" if heart_risk_score < 50 else "Moderate Risk" if heart_risk_score < 75 else "High Risk"

    # Simulated diabetes prediction
    diabetes_risk_score = random.randint(20, 90)
    diabetes_risk_level = "Low Risk" if diabetes_risk_score < 40 else "Moderate Risk" if diabetes_risk_score < 70 else "High Risk"

    results_label.config(text=(
        f"Heart Disease Risk: {heart_risk_level}\n"
        f"Heart Risk Score: {heart_risk_score}%\n\n"
        f"Diabetes Risk: {diabetes_risk_level}\n"
        f"Diabetes Risk Score: {diabetes_risk_score}%"
    ))
    loading_label.config(text="Analysis Complete.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Iris-Based Health Prediction")
root.geometry("400x550")

Label(root, text="Upload an Iris Image", font=("Arial", 14)).pack(pady=10)
Button(root, text="Upload Image", command=upload_image).pack()

canvas = Canvas(root, width=250, height=250, bg="gray")
canvas.pack(pady=10)

analyze_button = Button(root, text="Analyze Iris", state=tk.DISABLED, command=analyze_iris)
analyze_button.pack()

loading_label = Label(root, text="", font=("Arial", 10))
loading_label.pack(pady=5)

results_label = Label(root, text="", font=("Arial", 12), fg="blue")
results_label.pack(pady=10)

root.mainloop()
