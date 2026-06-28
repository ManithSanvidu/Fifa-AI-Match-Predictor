import pandas as pd

def load_csv(path):
    try:
        df=pd.read_csv(path)

        print(f"{path} loaded successfully")

        return df

    except Exception as e:

        print (e)

        return None

def save_csv(df,path):
    df.to_csv(path,index=False)

    print(f"Saved to {path}")