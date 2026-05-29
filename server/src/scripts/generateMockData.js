import dotenv from "dotenv";

dotenv.config();

import connectDB from "../config/db.js";

import District from "../models/District.js";

import Prediction from "../models/Prediction.js";

import Weather from "../models/Weather.js";

import logger from "../config/logger.js";

await connectDB();

const generateMockData =
  async () => {
    try {
      const districts =
        await District.find();

      for (const district of districts) {
        await Weather.create({
          district: district._id,

          temperature:
            Math.floor(
              Math.random() * 15 + 20
            ),

          humidity:
            Math.floor(
              Math.random() * 40 + 40
            ),

          rainfall:
            Math.floor(
              Math.random() * 300
            ),

          windSpeed:
            Math.floor(
              Math.random() * 20
            ),

          soilMoisture:
            Math.floor(
              Math.random() * 100
            ),

          forecastDate:
            new Date()
        });

        await Prediction.create({
          district: district._id,

          model: "XGBoost",

          prediction:
            Math.floor(
              Math.random() * 100
            ),

          confidence:
            Math.floor(
              Math.random() * 100
            ),

          riskLevel:
            ["LOW", "MEDIUM", "HIGH"][
              Math.floor(
                Math.random() * 3
              )
            ],

          features: {
            ndvi:
              Math.random().toFixed(2),

            ndwi:
              Math.random().toFixed(2),

            rainfall:
              Math.floor(
                Math.random() * 300
              ),

            humidity:
              Math.floor(
                Math.random() * 100
              ),

            temperature:
              Math.floor(
                Math.random() * 45
              ),

            soilMoisture:
              Math.floor(
                Math.random() * 100
              )
          }
        });
      }

      logger.info(
        "Mock Data Generated Successfully"
      );

      process.exit();
    } catch (error) {
      logger.error(error.message);

      process.exit(1);
    }
  };

generateMockData();