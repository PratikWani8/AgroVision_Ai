import mongoose from "mongoose";

const districtSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true
    },

    state: {
      type: String,
      required: true
    },

    coordinates: {
      lat: {
        type: Number,
        required: true
      },

      lng: {
        type: Number,
        required: true
      }
    },

    polygon: {
      type: [[Number]],
      default: []
    },

    vegetationIndices: {
      ndvi: {
        type: Number,
        default: 0
      },

      ndwi: {
        type: Number,
        default: 0
      },

      evi: {
        type: Number,
        default: 0
      }
    },

    diseaseProbability: {
      type: Number,
      default: 0
    },

    riskLevel: {
      type: String,
      enum: [
        "LOW",
        "MEDIUM",
        "HIGH"
      ],
      default: "LOW"
    },

    affectedArea: {
      type: Number,
      default: 0
    },

    cropType: {
      type: String,
      default: "Wheat"
    }
  },
  {
    timestamps: true
  }
);

export default mongoose.model(
  "District",
  districtSchema
);