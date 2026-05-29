import dotenv from "dotenv";

dotenv.config();

import connectDB from "../config/db.js";

import User from "../models/User.js";

import District from "../models/District.js";

import Prediction from "../models/Prediction.js";

import Alert from "../models/Alert.js";

import Weather from "../models/Weather.js";

import SatelliteData from "../models/SatelliteData.js";

import logger from "../config/logger.js";

await connectDB();

const resetDatabase =
  async () => {
    try {
      await User.deleteMany();

      await District.deleteMany();

      await Prediction.deleteMany();

      await Alert.deleteMany();

      await Weather.deleteMany();

      await SatelliteData.deleteMany();

      logger.info(
        "Database Reset Successful"
      );

      process.exit();
    } catch (error) {
      logger.error(error.message);

      process.exit(1);
    }
  };

resetDatabase();