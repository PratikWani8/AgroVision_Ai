import matplotlib.pyplot as plt

from app.core.logger import logger

def generate_heatmap(
    index_array,
    output_path
):
    try:
        logger.info(
            "Generating heatmap..."
        )

        plt.figure(figsize=(8, 8))

        plt.imshow(
            index_array,
            cmap="RdYlGn"
        )

        plt.colorbar()

        plt.title(
            "Vegetation Heatmap"
        )

        plt.savefig(output_path)

        plt.close()

        return output_path

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "Heatmap generation failed"
        )