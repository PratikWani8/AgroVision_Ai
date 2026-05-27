import District from "../models/District.js";
import Prediction from "../models/Prediction.js";
import Alert from "../models/Alert.js";

export const generateAnalytics =
  async () => {
    try {
      const totalDistricts =
        await District.countDocuments();

      const totalPredictions =
        await Prediction.countDocuments();

      const totalAlerts =
        await Alert.countDocuments();

      const highRiskDistricts =
        await District.find({
          riskLevel: "HIGH"
        });

      return {
        totalDistricts,
        totalPredictions,
        totalAlerts,
        highRiskDistricts:
          highRiskDistricts.length
      };
    } catch (error) {
      console.error(
        "Analytics Service Error:",
        error.message
      );

      throw new Error(
        "Failed to generate analytics"
      );
    }
  };

export const getDistrictTrend =
  async (districtId) => {
    try {
      const trends =
        await Prediction.find({
          district: districtId
        }).sort({
          createdAt: 1
        });

      return trends;
    } catch (error) {
      console.error(
        "Trend Analysis Error:",
        error.message
      );

      throw new Error(
        "Failed to fetch district trends"
      );
    }
  };