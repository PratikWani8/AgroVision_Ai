import matplotlib.pyplot as plt

from app.core.logger import logger

def plot_series(
    values,
    title="Chart"
):
    try:
        logger.info(
            "Generating visualization..."
        )

        plt.figure(figsize=(10, 5))

        plt.plot(values)

        plt.title(title)

        plt.show()

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Visualization failed"
        )