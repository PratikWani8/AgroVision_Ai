import logger from "../config/logger.js";

const alertSocket = (io) => {
  io.on("connection", (socket) => {
    logger.info(
      `Alert Socket Connected: ${socket.id}`
    );

    socket.on(
      "subscribe-alerts",
      () => {
        socket.join("alerts");

        logger.info(
          `Socket ${socket.id} subscribed to alerts`
        );
      }
    );

    socket.on(
      "unsubscribe-alerts",
      () => {
        socket.leave("alerts");

        logger.info(
          `Socket ${socket.id} unsubscribed from alerts`
        );
      }
    );

    socket.on("disconnect", () => {
      logger.info(
        `Alert Socket Disconnected: ${socket.id}`
      );
    });
  });
};

export const emitAlert = (
  io,
  alertData
) => {
  io.to("alerts").emit(
    "new-alert",
    alertData
  );

  logger.info(
    `Alert emitted: ${alertData.title}`
  );
};

export default alertSocket;