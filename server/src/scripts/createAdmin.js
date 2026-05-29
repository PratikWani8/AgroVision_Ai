import dotenv from "dotenv";

dotenv.config();

import connectDB from "../config/db.js";

import User from "../models/User.js";

import logger from "../config/logger.js";

await connectDB();

const createAdmin = async () => {
  try {
    const existingAdmin =
      await User.findOne({
        email:
          "admin@agrovision.ai"
      });

    if (existingAdmin) {
      logger.info(
        "Admin already exists"
      );

      process.exit();
    }

    const admin = await User.create({
      name: "System Admin",

      email: "admin@agrovision.ai",

      password: "password123",

      role: "admin"
    });

    logger.info(
      `Admin Created: ${admin.email}`
    );

    process.exit();
  } catch (error) {
    logger.error(error.message);

    process.exit(1);
  }
};

createAdmin();