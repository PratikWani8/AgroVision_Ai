import { Server } from "socket.io";

import logger from "./logger.js";

import notificationSocket from "../sockets/notificationSocket.js";

import alertSocket from "../sockets/alertSocket.js";

import predictionSocket from "../sockets/predictionSocket.js";

import weatherSocket from "../sockets/weatherSocket.js";

let io;

export const initializeSocket = (server ) => {
  io = new Server(server, {
    cors: {
      origin: "*",

      methods: [
        "GET",
        "POST"
      ]
    }
  });

  notificationSocket(io);

  alertSocket(io);

  predictionSocket(io);

  weatherSocket(io);

  logger.info(
    "Socket.IO Initialized"
  );

  return io;
};

export const getIO = () => {
  if (!io) {
    throw new Error(
      "Socket.IO not initialized"
    );
  }

  return io;
};