import PDFDocument from "pdfkit";

export const generatePDF = (
  predictions,
  res
) => {
  try {
    const doc = new PDFDocument();

    res.setHeader(
      "Content-Type",
      "application/pdf"
    );

    res.setHeader(
      "Content-Disposition",
      "attachment; filename=agrovision-report.pdf"
    );

    doc.pipe(res);

    doc
      .fontSize(22)
      .text(
        "AgroVision AI Intelligence Report",
        {
          align: "center"
        }
      );

    doc.moveDown();

    predictions.forEach((prediction) => {
      doc
        .fontSize(14)
        .text(
          `District: ${prediction.district?.name}`
        );

      doc.text(
        `Prediction Score: ${prediction.prediction}`
      );

      doc.text(
        `Confidence: ${prediction.confidence}`
      );

      doc.text(
        `Risk Level: ${prediction.riskLevel}`
      );

      doc.moveDown();
    });

    doc.end();
  } catch (error) {
    console.error(
      "PDF Service Error:",
      error.message
    );

    throw new Error(
      "Failed to generate PDF report"
    );
  }
};