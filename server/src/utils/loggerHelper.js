import logger from "../config/logger.js";

export const logInfo = (
  message
) => {
  logger.info(message);
};

export const logError = (
  message
) => {
  logger.error(message);
};

export const logWarning = (
  message
) => {
  logger.warn(message);
};