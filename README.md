# **Sales Prediction Using Linear Regression**  

This project demonstrates a sales prediction model using linear regression. It analyzes the impact of advertising budgets across TV, Radio, and Newspaper platforms on sales and provides actionable insights to optimize marketing strategies.  

---

## **Overview**  
The project aims to predict product sales based on advertising budgets. By identifying key drivers of sales, businesses can make data-driven decisions to optimize marketing spend.  

---

## **Dataset**  
The dataset contains 200 records with the following columns:  
- **TV**: Advertising budget for TV (in thousands of dollars).  
- **Radio**: Advertising budget for Radio (in thousands of dollars).  
- **Newspaper**: Advertising budget for Newspaper (in thousands of dollars).  
- **Sales**: Sales generated (in thousands of units).  

Key statistics and correlations are included in the analysis.  

---

## **Technologies Used**  
- **Python**: Data analysis and modeling.  
- **Libraries**:  
  - `pandas`  
  - `numpy`  
  - `matplotlib`  
  - `seaborn`  
  - `sklearn`  

---

## **Installation**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/dani6566/CODESOFT-Sales-prediction.git
   cd sales-prediction  
   ```  
2. Create a virtual environment (optional):  
   ```bash  
   python -m venv env  
   source env/bin/activate  # For Linux/Mac  
   env\Scripts\activate     # For Windows  
   ```  
3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## **Usage**  
1. Run the Jupyter Notebook:  
   ```bash  
   jupyter notebook  
   ```  
2. Open the file `sales_prediction.ipynb` to view and execute the step-by-step analysis.  

3. To predict sales for specific budgets, adjust the input in the prediction function:  
   ```python  
   predict_sales([TV_budget, Radio_budget, Newspaper_budget])  
   ```  

---

## **Model Performance**  
- **R-Squared (\( R^2 \))**: \( 0.906 \)  
  - The model explains 90.6% of the variance in Sales.  
- **Mean Squared Error (MSE)**: \( 2.91 \)  
  - Indicates a low prediction error.  

---

## **Insights and Recommendations**  
1. **TV Advertising**:  
   - The most impactful channel; prioritize budget allocation here.  

2. **Radio Advertising**:  
   - Secondary driver of sales; complement TV campaigns with Radio.  

3. **Newspaper Advertising**:  
   - Minimal impact; consider reducing spend or reallocating funds.  

4. **Synergy Testing**:  
   - Experiment with combined strategies (e.g., \( TV + Radio \)) for greater impact.  

---

## **Future Work**  
- Explore interaction effects and non-linear relationships.  
- Incorporate external factors like seasonality or economic trends.  
- Test advanced models (e.g., Ridge, Lasso, or ensemble methods).  

---


## **License**  
This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

Feel free to explore, contribute, or use this project for your sales prediction needs! 😊
