export const calculateNDVI = (
  nir,
  red
) => {
  if (nir + red === 0) {
    return 0;
  }

  return (
    (nir - red) / (nir + red)
  );
};

export const calculateNDWI = (
  green,
  nir
) => {
  if (green + nir === 0) {
    return 0;
  }

  return (
    (green - nir) /
    (green + nir)
  );
};

export const calculateEVI = (
  nir,
  red,
  blue
) => {
  const denominator =
    nir +
    6 * red -
    7.5 * blue +
    1;

  if (denominator === 0) {
    return 0;
  }

  return (
    2.5 *
    ((nir - red) / denominator)
  );
};