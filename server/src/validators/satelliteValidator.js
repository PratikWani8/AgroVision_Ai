import { body } from "express-validator";

export const satelliteValidator = [
  body("districtId")
    .notEmpty()
    .withMessage(
      "District ID is required"
    ),

  body("ndvi")
    .isFloat({ min: -1, max: 1 })
    .withMessage(
      "NDVI must be between -1 and 1"
    ),

  body("ndwi")
    .isFloat({ min: -1, max: 1 })
    .withMessage(
      "NDWI must be between -1 and 1"
    ),

  body("evi")
    .isNumeric()
    .withMessage(
      "EVI must be numeric"
    )
];