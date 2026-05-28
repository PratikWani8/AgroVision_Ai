import express from "express";

import protect from "../middleware/authMiddleware.js";

import { exportPDFReport } from "../controllers/reportController.js";

const router = express.Router();

router.get(
  "/pdf",
  protect,
  exportPDFReport
);

export default router;