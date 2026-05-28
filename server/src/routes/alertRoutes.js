import express from "express";

import protect from "../middleware/authMiddleware.js";

import { createAlert, getAlerts } from "../controllers/alertController.js";

const router = express.Router();

router.post(
  "/",
  protect,
  createAlert
);

router.get(
  "/",
  protect,
  getAlerts
);

export default router;