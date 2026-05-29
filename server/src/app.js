import express from "express";
import cors from "cors";
import helmet from "helmet";
import compression from "compression";
import morgan from "morgan";
import corsOptions from "./config/corsOptions.js";
import { apiLimiter } from "./middleware/rateLimiter.js";
import notFoundMiddleware from "./middleware/notFoundMiddleware.js";
import errorMiddleware from "./middleware/errorMiddleware.js";
import authRoutes from "./routes/authRoutes.js";
import districtRoutes from "./routes/districtRoutes.js";
import predictionRoutes from "./routes/predictionRoutes.js";
import analyticsRoutes from "./routes/analyticsRoutes.js";
import alertRoutes from "./routes/alertRoutes.js";
import weatherRoutes from "./routes/weatherRoutes.js";
import reportRoutes from "./routes/reportRoutes.js";
import satelliteRoutes from "./routes/satelliteRoutes.js";

const app = express();

app.use(
  express.json({
    limit: "10mb"
  })
);

app.use(
  express.urlencoded({
    extended: true
  })
);

app.use(cors(corsOptions));

app.use(helmet());

app.use(compression());

app.use(morgan("dev"));

app.use(apiLimiter);

app.get("/", (req, res) => {
  res.status(200).json({
    success: true,

    service: "AgroVision AI Backend",

    status: "Running"
  });
});

app.get("/api/health", (req, res) => {
  res.status(200).json({
    success: true,

    uptime: process.uptime(),

    timestamp: new Date(),

    environment:
      process.env.NODE_ENV
  });
});

app.use(
  "/api/auth",
  authRoutes
);

app.use(
  "/api/districts",
  districtRoutes
);

app.use(
  "/api/predictions",
  predictionRoutes
);

app.use(
  "/api/analytics",
  analyticsRoutes
);

app.use(
  "/api/alerts",
  alertRoutes
);

app.use(
  "/api/weather",
  weatherRoutes
);

app.use(
  "/api/reports",
  reportRoutes
);

app.use(
  "/api/satellite",
  satelliteRoutes
);

app.use(notFoundMiddleware);

app.use(errorMiddleware);

export default app;