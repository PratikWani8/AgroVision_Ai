import rateLimit from "express-rate-limit";

export const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,

  max: 10,

  message: {
    success: false,
    message:
      "Too many login attempts. Try again later."
  },

  standardHeaders: true,

  legacyHeaders: false
});

export const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,

  max: 100,

  message: {
    success: false,
    message:
      "Too many requests from this IP."
  },

  standardHeaders: true,

  legacyHeaders: false
});