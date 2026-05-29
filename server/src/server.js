import dotenv from "dotenv";
import http from "http";
import app from "./app.js";
import connectDB from "./config/db.js";
import { initializeSocket } from "./config/socket.js";
import logger from "./config/logger.js";
import weatherJob from "./jobs/weatherJob.js";
import predictionJob from "./jobs/predictionJob.js";
import alertJob from "./jobs/alertJob.js";
import satelliteJob from "./jobs/satelliteJob.js";
import cleanupJob from "./jobs/cleanupJob.js";

dotenv.config();

const PORT = process.env.PORT || 5000;

await connectDB();

const server = http.createServer(app);

initializeSocket(server);

weatherJob();

predictionJob();

alertJob();

satelliteJob();

cleanupJob();

server.listen(PORT, () => {
  logger.info(
    `AgroVision Backend Running on Port ${PORT}`
  );
});

process.on(
  "unhandledRejection",
  (err) => {
    logger.error(
      `Unhandled Rejection: ${err.message}`
    );

    server.close(() => {
      process.exit(1);
    });
  }
);

process.on(
  "uncaughtException",
  (err) => {
    logger.error(
      `Uncaught Exception: ${err.message}`
    );

    process.exit(1);
  }
);

process.on("SIGTERM", () => {
  logger.info(
    "SIGTERM received. Shutting down gracefully."
  );

  server.close(() => {
    logger.info(
      "Process terminated."
    );
  });
});