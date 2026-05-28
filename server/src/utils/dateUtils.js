export const formatDate = (
  date
) => {
  return new Date(date)
    .toISOString()
    .split("T")[0];
};

export const getCurrentTimestamp =
  () => {
    return new Date().toISOString();
  };

export const getDaysDifference = (
  date1,
  date2
) => {
  const diff =
    Math.abs(
      new Date(date2) -
        new Date(date1)
    );

  return Math.ceil(
    diff / (1000 * 60 * 60 * 24)
  );
};