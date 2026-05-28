import express from "express";

import {
  register,
  login,
  getProfile
} from "../controllers/authController.js";

import protect from "../middleware/authMiddleware.js";

import validateMiddleware from "../middleware/validateMiddleware.js";

import {
  registerValidator,
  loginValidator
} from "../validators/authValidator.js";

import { authLimiter } from "../middleware/rateLimiter.js";

const router = express.Router();

router.post(
  "/register",
  authLimiter,
  registerValidator,
  validateMiddleware,
  register
);

router.post(
  "/login",
  authLimiter,
  loginValidator,
  validateMiddleware,
  login
);

router.get(
  "/profile",
  protect,
  getProfile
);

export default router;