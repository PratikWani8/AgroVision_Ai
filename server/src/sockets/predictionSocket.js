import logger from "../config/logger.js";

const predictionSocket = (io) => {
  io.on("connection", (socket) => {
    logger.info(
      `Prediction Socket Connected: ${socket.id}`
    );

    socket.on(
      "subscribe-predictions",
      () => {
        socket.join("predictions");

        logger.info(
          `Socket ${socket.id} subscribed to predictions`
        );
      }
    );

    socket.on(
      "unsubscribe-predictions",
      () => {
        socket.leave("predictions");

        logger.info(
          `Socket ${socket.id} unsubscribed from predictions`
        );
      }
    );

    socket.on("disconnect", () => {
      logger.info(
        `Prediction Socket Disconnected: ${socket.id}`
      );
    });
  });
};

export const emitPrediction = (
  io,
  prediction
) => {
  io.to("predictions").emit(
    "prediction-update",
    prediction
  );

  logger.info(
    "Prediction emitted successfully"
  );
};

export default predictionSocket;