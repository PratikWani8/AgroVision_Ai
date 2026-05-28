import express from "express";

import protect from "../middleware/authMiddleware.js";

import authorize from "../middleware/roleMiddleware.js";

import validateMiddleware from "../middleware/validateMiddleware.js";

import { districtValidator } from "../validators/districtValidator.js";

import {
  createDistrict,
  getDistricts,
  getDistrictById,
  updateDistrict,
  deleteDistrict
} from "../controllers/districtController.js";

const router = express.Router();

router.get("/", protect, getDistricts);

router.get(
  "/:id",
  protect,
  getDistrictById
);

router.post(
  "/",
  protect,
  authorize("admin", "officer"),
  districtValidator,
  validateMiddleware,
  createDistrict
);

router.put(
  "/:id",
  protect,
  authorize("admin", "officer"),
  districtValidator,
  validateMiddleware,
  updateDistrict
);

router.delete(
  "/:id",
  protect,
  authorize("admin"),
  deleteDistrict
);

export default router;