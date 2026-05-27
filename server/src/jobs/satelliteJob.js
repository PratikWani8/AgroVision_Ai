import cron from "node-cron";

import District from "../models/District.js";

import SatelliteData from "../models/SatelliteData.js";

import logger from "../config/logger.js";

const satelliteJob = () => {
  cron.schedule("0 0 * * *", async () => {
    try {
      logger.info(
        "Running Satellite Processing Job..."
      );

      const districts =
        await District.find();

      for (const district of districts) {
        const simulatedNDVI =
          Math.random().toFixed(2);

        const simulatedNDWI =
          Math.random().toFixed(2);

        const simulatedEVI =
          Math.random().toFixed(2);

        district.vegetationIndices = {
          ndvi:
            parseFloat(simulatedNDVI),

          ndwi:
            parseFloat(simulatedNDWI),

          evi:
            parseFloat(simulatedEVI)
        };

        await district.save();

        await SatelliteData.create({
          district: district._id,

          satelliteSource:
            "Sentinel-2",

          imageDate: new Date(),

          ndvi:
            parseFloat(simulatedNDVI),

          ndwi:
            parseFloat(simulatedNDWI),

          evi:
            parseFloat(simulatedEVI),

          cloudCoverage:
            Math.floor(
              Math.random() * 30
            )
        });
      }

      logger.info(
        "Satellite Job Completed"
      );
    } catch (error) {
      logger.error(
        `Satellite Job Error: ${error.message}`
      );
    }
  });
};

export default satelliteJob;