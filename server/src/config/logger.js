import winston from "winston";

import env from "./env.js";

const logger =
  winston.createLogger({
    level: env.LOG_LEVEL,

    format:
      winston.format.combine(
        winston.format.timestamp(),

        winston.format.printf(
          ({
            timestamp,
            level,
            message
          }) => {
            return `${timestamp} [${level.toUpperCase()}]: ${message}`;
          }
        )
      ),

    transports: [
      new winston.transports.Console()
    ]
  });

export default logger;