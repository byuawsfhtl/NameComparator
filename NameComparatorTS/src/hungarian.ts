type Matrix = number[][];

function padMatrix(matrix: Matrix, padValue: number = Number.MAX_SAFE_INTEGER): Matrix {
  const n = matrix.length;
  const m = matrix[0].length;
  const size = Math.max(n, m);
  const padded = Array.from({ length: size }, (_, i) =>
    Array.from({ length: size }, (_, j) =>
      i < n && j < m ? matrix[i][j] : padValue
    )
  );
  return padded;
}

function findZero(matrix: Matrix, rowCover: boolean[], colCover: boolean[]): [number, number] | null {
  for (let i = 0; i < matrix.length; i++) {
    if (rowCover[i]) continue;
    for (let j = 0; j < matrix[0].length; j++) {
      if (!colCover[j] && matrix[i][j] === 0) {
        return [i, j];
      }
    }
  }
  return null;
}

// subtract row and column minimum
function step1(matrix: Matrix): void {
  const n = matrix.length;
  const m = matrix[0].length;

  // Subtract row minima
  for (let i = 0; i < n; i++) {
    const rowMin = Math.min(...matrix[i]);
    for (let j = 0; j < m; j++) {
      matrix[i][j] -= rowMin;
    }
  }

  // Subtract column minima
  for (let j = 0; j < m; j++) {
    let colMin = Infinity;
    for (let i = 0; i < n; i++) {
      colMin = Math.min(colMin, matrix[i][j]);
    }
    for (let i = 0; i < n; i++) {
      matrix[i][j] -= colMin;
    }
  }
}
  

function step3(matrix: Matrix, mask: number[][], rowCover: boolean[], colCover: boolean[]): void {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] === 0 && !rowCover[i] && !colCover[j]) {
        mask[i][j] = 1;
        rowCover[i] = true;
        colCover[j] = true;
      }
    }
  }
  rowCover.fill(false);
  colCover.fill(false);
}

function coverColumns(mask: number[][], colCover: boolean[]): number {
  const nCols = mask[0].length;
  let count = 0;
  for (let j = 0; j < nCols; j++) {
    for (let i = 0; i < mask.length; i++) {
      if (mask[i][j] === 1) {
        colCover[j] = true;
        count++;
        break;
      }
    }
  }
  return count;
}

function step4(matrix: Matrix, mask: number[][], rowCover: boolean[], colCover: boolean[], path: [number, number][]): number {
  while (true) {
    const zero = findZero(matrix, rowCover, colCover);
    if (!zero) return 6;

    const [row, col] = zero;
    mask[row][col] = 2;

    const starCol = mask[row].indexOf(1);
    if (starCol !== -1) {
      rowCover[row] = true;
      colCover[starCol] = false;
    } else {
      path.push([row, col]);
      return 5;
    }
  }
}

function step5(mask: number[][], path: [number, number][]): void {
  let done = false;
  let [r, c] = path[0];

  while (!done) {
    let row = -1;
    for (let i = 0; i < mask.length; i++) {
      if (mask[i][c] === 1) {
        row = i;
        break;
      }
    }

    if (row === -1) {
      done = true;
    } else {
      path.push([row, c]);
      const col = mask[row].findIndex(val => val === 2);
      path.push([row, col]);
      [r, c] = [row, col];
    }
  }

  // Flip stars and primes
  for (const [i, j] of path) {
    if (mask[i][j] === 1) {
      mask[i][j] = 0;
    } else if (mask[i][j] === 2) {
      mask[i][j] = 1;
    }
  }

  // Clear all primes
  for (let i = 0; i < mask.length; i++) {
    for (let j = 0; j < mask[i].length; j++) {
      if (mask[i][j] === 2) mask[i][j] = 0;
    }
  }
}


function step6(matrix: Matrix, rowCover: boolean[], colCover: boolean[]): void {
  let minVal = Infinity;
  for (let i = 0; i < matrix.length; i++) {
    if (!rowCover[i]) {
      for (let j = 0; j < matrix[i].length; j++) {
        if (!colCover[j]) {
          minVal = Math.min(minVal, matrix[i][j]);
        }
      }
    }
  }

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (rowCover[i]) matrix[i][j] += minVal;
      if (!colCover[j]) matrix[i][j] -= minVal;
    }
  }
}

export function hungarianAlgorithm(costMatrix: Matrix): [number[], number[]] {
  const n = costMatrix.length;
  const m = costMatrix[0].length;
  const size = Math.max(n, m);

  const paddedMatrix = padMatrix(costMatrix);
  const matrix = paddedMatrix.map(row => row.slice());
  const mask = Array.from({ length: size }, () => Array(size).fill(0));
  const rowCover = Array(size).fill(false);
  const colCover = Array(size).fill(false);
  let path: [number, number][] = [];

  step1(matrix);
  step3(matrix, mask, rowCover, colCover);
  let step = 3;

  while (true) {
    switch (step) {
      case 3:
        const count = coverColumns(mask, colCover);
        step = count >= size ? 7 : 4;
        break;
      case 4:
        path = [];
        step = step4(matrix, mask, rowCover, colCover, path);
        break;
      case 5:
        step5(mask, path);
        rowCover.fill(false);
        colCover.fill(false);
        step = 3;
        break;
      case 6:
        step6(matrix, rowCover, colCover);
        step = 4;
        break;
      case 7:
        const row_ind: number[] = [];
        const col_ind: number[] = [];
        for (let i = 0; i < n; i++) { // only real (unpadded) rows
          for (let j = 0; j < m; j++) { // only real (unpadded) cols
            if (mask[i][j] === 1) {
              row_ind.push(i);
              col_ind.push(j);
              break;
            }
          }
        }
        return [row_ind, col_ind];
    }
  }
}

// const costMatrix1 = [
//   [4, 1, 3],
//   [2, 0, 5],
//   [3, 2, 2],
// ];

// const [rows1, cols1] = hungarianAlgorithm(costMatrix1);
// console.log("Test 1 - Simple 3x3:", rows1, cols1);
// // Expected optimal assignment: [(0,1), (1,0), (2,2)] or equivalent

// const costMatrix2 = [
//   [1, 100, 100, 100],
//   [100, 1, 100, 100],
//   [100, 100, 1, 100],
//   [100, 100, 100, 1],
// ];

// const [rows2, cols2] = hungarianAlgorithm(costMatrix2);
// console.log("Test 2 - Diagonal Minima:", rows2, cols2);
// // Expected: (0,0), (1,1), (2,2), (3,3)

// const costMatrix3 = [
//   [5, 9, 1],
//   [10, 3, 2],
// ];

// const [rows3, cols3] = hungarianAlgorithm(costMatrix3);
// console.log("Test 3 - Rectangular (2x3):", rows3, cols3);
// // Expected: 2 assignments like (0,2), (1,1)


// const costMatrix4 = [
//   [5, 8],
//   [7, 3],
//   [2, 6],
// ];

// const [rows4, cols4] = hungarianAlgorithm(costMatrix4);
// console.log("Test 4 - Rectangular (3x2):", rows4, cols4);
// // Expected: 2 assignments like (1,1), (2,0)

// const costMatrix5 = [
//   [1, 1, 1],
//   [1, 1, 1],
//   [1, 1, 1],
// ];

// const [rows5, cols5] = hungarianAlgorithm(costMatrix5);
// console.log("Test 5 - Equal Costs:", rows5, cols5);
// // Any full assignment is valid, total cost will be 3

