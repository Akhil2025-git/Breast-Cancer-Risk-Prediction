
BREAST CANCER RISK PREDICTION

🔍 Overview
This project is a machine learning web application that predicts the risk of breast cancer based on clinical and demographic input features. 
It leverages a Random Forest Classifier with hyperparameter tuning for optimal performance and it is deployed using Streamlit for easy accessibility.


📁 Project Structure
BREAST CANCER RISK PREDICTION

├── cancer_app.py                                       # Streamlit app for prediction
├── Breast Cancer Risk Prediction using svd .ipynb      # ML pipeline for training
├── cancer main random forest.ipynb                     # ML pipeline selected model (random forest )
├── Breast Cancer METABRIC.csv                          # Dataset of breast cancer
├── cancer project PowerBI Dashboard.pbix               # breast cancer dashboard
├── Capstone Presentation.pptx                          # Final project presentation
├── label_encoders.joblib                               # label encoded file saved as joblib
├── scaler.joblib                                       # scaler saved as joblib
├── Random_Forest.joblib                                # selected model saved as joblib


## Model Details

- **Algorithm**: Random Forest Classifier
- **Tuning**: GridSearchCV for hyperparameter optimization
- **Metrics**: Accuracy, Precision, Recall, F1-score, AUC-ROC

⚙️ Technologies Used
- Python 3.12
- Pandas, NumPy – Data preprocessing and manipulation
- Streamlit – UI development
- scikit-learn – Machine learning model and pipeline
- Power BI – Data visualization and insights
- Matplotlib, Seaborn – for data visualization


🚀 Future Enhancements

- Deploy as a mobile app: Create a lightweight Android/iOS version for broader accessibility
- Doctor’s dashboard: Provide tools for doctors to analyze patient trends over time.
- Image Recognition Integration: Incorporate OCR and CNN-based image processing to extract features from scanned pathology reports or mammogram images.
- Cloud Deployment & API Integration: Host the model on cloud services (e.g., AWS, GCP) and expose REST APIs for integration with hospital systems and EHRs.

🧠 Project Outcome
This project focuses on early detection of breast cancer using a machine learning approach. It leverages a Random Forest classifier trained on diagnostic data to predict the likelihood of breast cancer. The system is deployed via Streamlit, allowing users to interactively input clinical features and obtain risk predictions in real-time.


                             
										*** END**