import express from "express";

import protect from "../middleware/authMiddleware.js";

import validateMiddleware from "../middleware/validateMiddleware.js";

import { predictionValidator } from "../validators/predictionValidator.js";

import {
  generatePrediction,
  getPredictions
} from "../controllers/predictionController.js";

const router = express.Router();

router.post(
  "/",
  protect,
  predictionValidator,
  validateMiddleware,
  generatePrediction
);

router.get(
  "/",
  protect,
  getPredictions
);

export default router;