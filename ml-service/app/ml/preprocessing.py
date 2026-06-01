from sklearn.preprocessing import StandardScaler
import pandas as pd

from app.core.logger import logger


def preprocess_data(dataframe):
    try:
        logger.info(
            "Preprocessing dataset..."
        )

        numeric_df = dataframe.select_dtypes(
            include=["number"]
        )

        scaler = StandardScaler()

        scaled = scaler.fit_transform(
            numeric_df
        )

        scaled_df = pd.DataFrame(
            scaled,
            columns=numeric_df.columns,
            index=dataframe.index
        )

        return scaled_df

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Preprocessing failed"
        )