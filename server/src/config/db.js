import mongoose from "mongoose";

import logger from "./logger.js";

import env from "./env.js";

mongoose.set("strictQuery", true);

const connectDB = async () => {
  try {
    const conn =
      await mongoose.connect(
        env.MONGO_URI
      );

    logger.info(
      `MongoDB Connected: ${conn.connection.host}`
    );
  } catch (error) {
    logger.error(
      `MongoDB Error: ${error.message}`
    );

    process.exit(1);
  }
};

export default connectDB;