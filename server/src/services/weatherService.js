import axios from "axios";

const BASE_URL =
  process.env.OPEN_METEO_BASE_URL;

export const fetchWeatherData =
  async (lat, lng) => {
    try {
      const response = await axios.get(
        `${BASE_URL}?latitude=${lat}&longitude=${lng}&current=temperature_2m,relative_humidity_2m,rain,wind_speed_10m`
      );

      return response.data;
    } catch (error) {
      console.error(
        "Weather Service Error:",
        error.message
      );

      throw new Error(
        "Failed to fetch weather data"
      );
    }
  };