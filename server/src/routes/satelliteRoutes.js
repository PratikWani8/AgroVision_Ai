import express from "express";

import protect from "../middleware/authMiddleware.js";

import { uploadSatelliteMetrics } from "../controllers/satelliteController.js";

const router = express.Router();

router.post(
  "/metrics",
  protect,
  uploadSatelliteMetrics
);

export default router;