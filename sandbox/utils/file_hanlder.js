
export const readFile = async (path) => {
  const response = await fetch(path);
  const data = await response.text();
  return data;
}
