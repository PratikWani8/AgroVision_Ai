import mongoose from "mongoose";

const satelliteDataSchema =
  new mongoose.Schema(
    {
      district: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "District"
      },

      satelliteSource: {
        type: String,
        enum: [
          "Sentinel-2",
          "Landsat-8",
          "Drone"
        ],
        default: "Sentinel-2"
      },

      imageDate: {
        type: Date,
        required: true
      },

      imageUrl: {
        type: String
      },

      cloudCoverage: {
        type: Number,
        default: 0
      },

      ndvi: Number,

      ndwi: Number,

      evi: Number,

      rasterMetadata: {
        resolution: String,

        projection: String,

        bands: Number
      }
    },
    {
      timestamps: true
    }
  );

export default mongoose.model(
  "SatelliteData",
  satelliteDataSchema
);