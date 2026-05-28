export const calculateDistance = (
  lat1,
  lon1,
  lat2,
  lon2
) => {
  const R = 6371;

  const dLat =
    ((lat2 - lat1) * Math.PI) / 180;

  const dLon =
    ((lon2 - lon1) * Math.PI) / 180;

  const a =
    Math.sin(dLat / 2) *
      Math.sin(dLat / 2) +
    Math.cos(
      (lat1 * Math.PI) / 180
    ) *
      Math.cos(
        (lat2 * Math.PI) / 180
      ) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);

  const c =
    2 * Math.atan2(
      Math.sqrt(a),
      Math.sqrt(1 - a)
    );

  return R * c;
};

export const generateBoundingBox = (
  lat,
  lng,
  radiusKm = 10
) => {
  const latChange =
    radiusKm / 111;

  const lngChange =
    radiusKm /
    (111 *
      Math.cos((lat * Math.PI) / 180));

  return {
    north: lat + latChange,
    south: lat - latChange,
    east: lng + lngChange,
    west: lng - lngChange
  };
};