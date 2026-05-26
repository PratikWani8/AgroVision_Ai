import { query } from "express-validator";

export const weatherValidator = [
  query("lat")
    .isNumeric()
    .withMessage(
      "Latitude must be numeric"
    ),

  query("lng")
    .isNumeric()
    .withMessage(
      "Longitude must be numeric"
    )
];