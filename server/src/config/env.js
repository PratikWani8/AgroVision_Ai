import dotenv from "dotenv";

dotenv.config();

const env = {
  PORT: process.env.PORT || 5000,

  NODE_ENV:
    process.env.NODE_ENV || "development",

  MONGO_URI:
    process.env.MONGO_URI,

  JWT_SECRET:
    process.env.JWT_SECRET,

  JWT_EXPIRE:
    process.env.JWT_EXPIRE || "7d",

  CLIENT_URL:
    process.env.CLIENT_URL ||
    "http://localhost:5173",

  ML_SERVICE_URL:
    process.env.ML_SERVICE_URL ||
    "http://localhost:8000",

  OPEN_METEO_BASE_URL:
    process.env.OPEN_METEO_BASE_URL ||
    "https://api.open-meteo.com/v1/forecast",

  LOG_LEVEL:
    process.env.LOG_LEVEL || "info",

  MAX_FILE_SIZE:
    process.env.MAX_FILE_SIZE ||
    5242880
};

export default env;