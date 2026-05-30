import matplotlib.pyplot as plt

from app.core.logger import logger

def export_png(
    data,
    output_path
):
    try:
        logger.info(
            "Exporting PNG..."
        )

        plt.figure(figsize=(8, 8))

        plt.imshow(
            data,
            cmap="viridis"
        )

        plt.axis("off")

        plt.savefig(
            output_path,
            bbox_inches="tight"
        )

        plt.close()

        return output_path

    except Exception as e:
        logger.error(str(e))

        raise Exception(
            "PNG export failed"
        )