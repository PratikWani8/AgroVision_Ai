import mongoose from "mongoose";

const weatherSchema =
  new mongoose.Schema(
    {
      district: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "District"
      },

      temperature: Number,

      humidity: Number,

      rainfall: Number,

      windSpeed: Number,

      soilMoisture: Number,

      forecastDate: Date
    },
    {
      timestamps: true
    }
  );

export default mongoose.model(
  "Weather",
  weatherSchema
);