import os
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest,chi2
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessing:
    def __init__(self,input_path,output_path):
        self.input_path = input_path
        self.output_path = output_path

        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.selected_featurs = []


        self.df = None
        self.X = None
        self.y = None 

        os.makedirs(self.output_path,exist_ok=True)

        logger.info("Data Processing Initalized...")

    def load_data(self):
        try:
            self.df = pd.read_csv(self.input_path)
            logger.info("Data Loaded Suecssfully")

        except Exception as e:
            logger.error(f"Error While loading data {e}")
            raise CustomException("Failed to load data")


    def preprocess_data(self):
        try:
            self.df = self.df.drop(columns=['Patient_ID'])
            self.X =self.df.drop(columns=["Survival_Prediction"])
            self.y = self.df["Survival_Prediction"]


            categorical_cols = self.X.select_dtypes(include=["object"]).columns
            
            logger.info(f"categorical columns are : {categorical_cols}")

            for col in categorical_cols:
                le = LabelEncoder()
                self.X[col] = le.fit_transform(self.X[col])
                self.label_encoders[col] = le

            logger.info("Label Encoding Done...")

        except Exception as e:
            logger.error(f"Error While encoding data {e}")
            raise CustomException("Failed to encode data",str(e))

    def feature_selection(self):
        try:
            X_cat = self.X.select_dtypes(include=['int64' , 'float64'])
            chi2_selector = SelectKBest(score_func=chi2 , k="all")
            chi2_selector.fit(X_cat,self.y)

            chi2_scores = pd.DataFrame({
                    'Features' : X_cat.columns,
                    "Chi2 Score" : chi2_selector.scores_
                }).sort_values(by='Chi2 Score' , ascending=False)


            top_features = chi2_scores.head(15)["Features"].tolist()
            self.selected_featurs = top_features
            logger.info(f"Selected Features {self.selected_featurs}")


            self.X = self.X[self.selected_featurs]  # type: ignore

            logger.info("Features Selection done...")
            
        except Exception as e:
            logger.error(f"Error While feature selection data {e}")
            raise CustomException("Failed to selected featurs")



    def split_and_scale_data(self):
        try:
            X_train , X_test , y_train , y_test = train_test_split(self.X,self.y ,test_size=0.2 , random_state=42,stratify=self.y)

            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)

            logger.info("Splitting and Scaling Data done..")
            
            return X_train,X_test,y_train,y_test

        except Exception as e:
            logger.error(f"Error While splitting and Scaling Data {e}")
            raise CustomException("Failed to splitting and Scaling Data")


    def save_data_and_Scaler(self,X_train,X_test,y_train,y_test):
        try:
            joblib.dump(X_train,os.path.join(self.output_path,"X_train.pkl"))
            joblib.dump(X_test,os.path.join(self.output_path,"X_test.pkl"))
            joblib.dump(y_train,os.path.join(self.output_path,"y_train.pkl"))
            joblib.dump(y_test,os.path.join(self.output_path,"y_test.pkl"))

            joblib.dump(self.scaler,os.path.join(self.output_path,"scaler.pkl"))

            logger.info("Saveing Data done...")

        except Exception as e:
            logger.error(f"Error While Saving Data {e}")
            raise CustomException("Failed to Save Data")


    def run(self):
        self.load_data()
        self.preprocess_data()
        self.feature_selection()
        X_train,X_test,y_train,y_test = self.split_and_scale_data()
        self.save_data_and_Scaler(X_train,X_test,y_train,y_test)

        logger.info("Data Processing Pipelne done Suecssfully...")


if __name__ == "__main__":
    input_path = r"artifacts/raw/data.csv"
    output_path = r"artifacts/processed"

    processer = DataProcessing(input_path,output_path)

    processer.run()
