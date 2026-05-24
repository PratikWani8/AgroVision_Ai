import District from "../models/District.js";
import Prediction from "../models/Prediction.js";
import Alert from "../models/Alert.js";

export const getDashboardAnalytics = async (
  req,
  res
) => {
  try {
    const districts = await District.countDocuments();

    const predictions =
      await Prediction.countDocuments();

    const alerts = await Alert.countDocuments();

    const highRiskDistricts =
      await District.countDocuments({
        riskLevel: "HIGH"
      });

    res.status(200).json({
      success: true,
      analytics: {
        totalDistricts: districts,
        totalPredictions: predictions,
        totalAlerts: alerts,
        highRiskDistricts
      }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
};

export const getRiskDistribution = async (
  req,
  res
) => {
  try {
    const risks = await District.aggregate([
      {
        $group: {
          _id: "$riskLevel",
          count: { $sum: 1 }
        }
      }
    ]);

    res.status(200).json({
      success: true,
      data: risks
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
};