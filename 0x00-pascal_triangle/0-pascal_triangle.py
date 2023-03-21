// returns a list of lists of integers representing the Pascal’s triangle of n

const pascal_triangle = (n) => {
  if (n <= 0) {
    return [];
  }
  
  const triangle = [[1]];
  
  for (let i = 1; i < n; i++) {
    const prevRow = triangle[i - 1];
    const currRow = [1];
    
    for (let j = 1; j < i; j++) {
      currRow.push(prevRow[j - 1] + prevRow[j]);
    }
    
    currRow.push(1);
    triangle.push(currRow);
  }
  
  return triangle;
};

