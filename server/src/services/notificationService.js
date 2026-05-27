import { getIO } from "../config/socket.js";

export const sendRealtimeNotification =
  (event, payload) => {
    try {
      const io = getIO();

      io.emit(event, payload);

      console.log(
        `Realtime Notification Sent: ${event}`
      );
    } catch (error) {
      console.error(
        "Notification Error:",
        error.message
      );
    }
  };