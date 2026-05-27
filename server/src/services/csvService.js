import { createObjectCsvWriter } from "csv-writer";

export const exportPredictionsCSV =
  async (predictions, filePath) => {
    try {
      const csvWriter =
        createObjectCsvWriter({
          path: filePath,

          header: [
            {
              id: "district",
              title: "District"
            },

            {
              id: "prediction",
              title: "Prediction"
            },

            {
              id: "confidence",
              title: "Confidence"
            },

            {
              id: "riskLevel",
              title: "Risk Level"
            }
          ]
        });

      const data = predictions.map((p) => ({
        district: p.district?.name,
        prediction: p.prediction,
        confidence: p.confidence,
        riskLevel: p.riskLevel
      }));

      await csvWriter.writeRecords(data);

      return filePath;
    } catch (error) {
      console.error(
        "CSV Export Error:",
        error.message
      );

      throw new Error(
        "Failed to export CSV"
      );
    }
  };