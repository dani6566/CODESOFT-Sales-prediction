import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score



def load_data():
     #Load the advertising dataset
     df = pd.read_csv("../Data/advertising.csv")
     return df


def perform_EDA(df):
     #Perform Exploratory Data Analysis
     sale_correlation = sns.heatmap(df.corr(),annot=True,cmap="Greens")
     print("Correlation Matrix:", sale_correlation)

def Scatter_Plot(df):
     #scatter plot
     plt.scatter(df["TV"],df["Sales"],label="TV Vs Sales",alpha=0.7)
     plt.scatter(df["Radio"],df["Sales"],label="Radio Vs Sales",alpha=0.7)
     plt.xlabel("Advertising Budget")
     plt.ylabel("Sales")
     plt.title("Sales Vs Advertising Budget")
     plt.legend()
     plt.show()

def split_data(df):
     X = df[["TV","Radio","Newspaper"]]
     y = df["Sales"]

     return train_test_split(X,y,test_size=0.2,random_state=42)

def train_model(X_train,y_train):
     #trains the linear regrassion model
     model = LinearRegression()
     model.fit(X_train,y_train)
     return model

def evaluation(model,X_test,y_test):
     #Evaluation the model's performance
     y_pred = model.predict(X_test)
     mse = mean_squared_error(y_test,y_pred)
     r2 = r2_score(y_test,y_pred)
     print("Model Evaluation")
     print("Mean Squared Error:",mse)
     print("R^2 Score:",r2)

def Predict_sale(model,new_budget):
     predicted_sale = model.predict([new_budget])
     print(f'Predicted Sales for budget {new_budget}: {predicted_sale[0]}')
     # return predicted_sale[0]
