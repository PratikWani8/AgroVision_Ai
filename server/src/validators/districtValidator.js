import { body } from "express-validator";

export const districtValidator = [
  body("name")
    .notEmpty()
    .withMessage(
      "District name is required"
    ),

  body("state")
    .notEmpty()
    .withMessage("State is required"),

  body("coordinates.lat")
    .isNumeric()
    .withMessage(
      "Latitude must be numeric"
    ),

  body("coordinates.lng")
    .isNumeric()
    .withMessage(
      "Longitude must be numeric"
    ),

  body("riskLevel")
    .optional()
    .isIn([
      "LOW",
      "MEDIUM",
      "HIGH"
    ])
    .withMessage("Invalid risk level")
];