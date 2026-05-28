const pagination = (
  page = 1,
  limit = 10
) => {
  const currentPage =
    parseInt(page);

  const currentLimit =
    parseInt(limit);

  const skip =
    (currentPage - 1) *
    currentLimit;

  return {
    skip,
    limit: currentLimit
  };
};

export default pagination;