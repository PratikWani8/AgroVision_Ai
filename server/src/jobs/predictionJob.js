import cron from "node-cron";

import District from "../models/District.js";

import Prediction from "../models/Prediction.js";

import Weather from "../models/Weather.js";

import {
  getPrediction
} from "../services/mlService.js";

import calculateRisk
  from "../utils/calculateRisk.js";

import logger from "../config/logger.js";

const predictionJob = () => {
  cron.schedule("0 */12 * * *", async () => {
    try {
      logger.info(
        "Running Prediction Job..."
      );

      const districts =
        await District.find();

      for (const district of districts) {
        const latestWeather =
          await Weather.findOne({
            district: district._id
          }).sort({
            createdAt: -1
          });

        if (!latestWeather) continue;

        const payload = {
          ndvi:
            district.vegetationIndices
              .ndvi,

          ndwi:
            district.vegetationIndices
              .ndwi,

          rainfall:
            latestWeather.rainfall,

          humidity:
            latestWeather.humidity,

          temperature:
            latestWeather.temperature,

          soilMoisture:
            latestWeather.soilMoisture ||
            30
        };

        const mlResult =
          await getPrediction(payload);

        const risk =
          calculateRisk(payload);

        district.riskLevel =
          risk.riskLevel;

        district.diseaseProbability =
          mlResult.prediction;

        await district.save();

        await Prediction.create({
          district: district._id,

          model: mlResult.model,

          prediction:
            mlResult.prediction,

          confidence:
            mlResult.confidence,

          riskLevel:
            risk.riskLevel,

          features: payload
        });
      }

      logger.info(
        "Prediction Job Completed"
      );
    } catch (error) {
      logger.error(
        `Prediction Job Error: ${error.message}`
      );
    }
  });
};

export default predictionJob;