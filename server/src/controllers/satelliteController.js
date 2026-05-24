import District from "../models/District.js";

export const uploadSatelliteMetrics = async (
  req,
  res
) => {
  try {
    const {
      districtId,
      ndvi,
      ndwi,
      evi
    } = req.body;

    const district = await District.findById(
      districtId
    );

    if (!district) {
      return res.status(404).json({
        success: false,
        message: "District not found"
      });
    }

    district.vegetationIndices = {
      ndvi,
      ndwi,
      evi
    };

    await district.save();

    res.status(200).json({
      success: true,
      data: district
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
};