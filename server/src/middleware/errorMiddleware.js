import logger from "../config/logger.js";

const errorMiddleware = (
  err,
  req,
  res,
  next
) => {
  logger.error(err.stack);

  let statusCode = err.statusCode || 500;

  let message =
    err.message || "Internal Server Error";

  if (err.name === "CastError") {
    statusCode = 400;
    message = "Invalid resource ID";
  }

  if (err.code === 11000) {
    statusCode = 400;
    message = "Duplicate field value";
  }

  res.status(statusCode).json({
    success: false,
    message,
    stack:
      process.env.NODE_ENV === "production"
        ? null
        : err.stack
  });
};

export default errorMiddleware;