import matplotlib.pyplot as plt

from app.core.logger import logger

def generate_outbreak_map(
    outbreak_array,
    output_path
):
    try:
        logger.info(
            "Generating outbreak map..."
        )

        plt.figure(figsize=(8, 8))

        plt.imshow(
            outbreak_array,
            cmap="hot"
        )

        plt.colorbar()

        plt.title(
            "Disease Outbreak Map"
        )

        plt.savefig(output_path)

        plt.close()

        return output_path

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Outbreak map generation failed"
        )