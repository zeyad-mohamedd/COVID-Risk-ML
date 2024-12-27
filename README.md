# COVID-Risk-ML  🌍🦠

## 📜 Project Description
This project leverages machine learning algorithms to predict the risk levels of countries during the COVID-19 pandemic. By analyzing critical data such as deaths, confirmed cases, and recoveries, the model classifies countries into risk categories to support informed decision-making.

---

## 📝 Project Structure

COVID-Risk-ML/

│
├── data/                       
│   ├── raw/                    
│   ├── processed/              
│   └── dataset.csv             
│
├── src/                        
│   ├── __init__.py             
│   ├── data_processing.py      
│   ├── model_training.py       
│   ├── model_evaluation.py     
│   └── main.py                 
│
├── models/                     
│   └── model.pkl               
│
├── notebooks/                  
│   └── exploration.ipynb       
│
├── tests/                      
│   └── test_main.py            
│
├── requirements.txt            
├── README.md                   
├── LICENSE                     
└── .gitignore                  
                        
---

## 📂 Features 
- Predicts risk levels of countries based on COVID-19 data.
- Utilizes a variety of machine learning algorithms:
  - Decision Tree Classifier 🌳
  - K-Nearest Neighbors (KNN) 🤖
  - Random Forest Classifier 🌲
  - Logistic Regression 📊
  - Naive Bayes 📈
- Focuses on the mean death rates for accurate risk assessment.

---

## 🛠️ Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/COVID-Risk-ML.git
   ```
2. Navigate to the project directory:
   ```bash
   cd COVID-Risk-ML
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Usage 
Run the main script to train the models and make predictions:
```bash
python main.py
```

---

## 🎯 Objective 
The model evaluates the risk level of each country based on its mean death rate and other COVID-19 statistics. The final output provides a classification of high-risk and low-risk countries.

---

## 🤝 Contributing 
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## 📄 License 
This project is licensed under the MIT License. See the LICENSE file for details.

---

## ✨ Acknowledgements 
- COVID-19 data sourced from reliable public datasets.
- Inspired by the need for efficient risk assessment during global health crises.

---

## 🔗 Contact 
For any inquiries or suggestions, please reach out to Me (mziad4467@gmail.com).
