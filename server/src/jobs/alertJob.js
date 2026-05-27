import cron from "node-cron";

import District from "../models/District.js";

import { createSystemAlert } from "../services/alertService.js";

import logger from "../config/logger.js";

const alertJob = () => {
  cron.schedule("*/30 * * * *", async () => {
    try {
      logger.info(
        "Running Alert Monitoring Job..."
      );

      const districts =
        await District.find({
          riskLevel: "HIGH"
        });

      for (const district of districts) {
        await createSystemAlert({
          district: district._id,

          type: "OUTBREAK",

          severity: "HIGH",

          title:
            "High Disease Risk Detected",

          message: `Potential crop disease outbreak detected in ${district.name}`
        });
      }

      logger.info(
        "Alert Monitoring Job Completed"
      );
    } catch (error) {
      logger.error(
        `Alert Job Error: ${error.message}`
      );
    }
  });
};

export default alertJob;