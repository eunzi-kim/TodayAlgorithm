function solution(n, lost, reserve) {
  let answer = 0;

  let cloth = [];
  for (let x = 1; x <= n; x++) {
    if (lost.includes(x) && reserve.includes(x)) {
      cloth.push(1);
      answer += 1;
    } else if (lost.includes(x)) {
      cloth.push(0);
    } else if (reserve.includes(x)) {
      cloth.push(2);
      answer += 1;
    } else {
      cloth.push(1);
      answer += 1;
    }
  }

  for (let i = 0; i < n; i++) {
    let chk = 0;
    if (cloth[i] === 0) {
      if (i > 0) {
        if (cloth[i - 1] === 2) {
          cloth[i - 1] -= 1;
          cloth[i] += 1;
          chk = 1;
          answer += 1;
        }
      }
      if (chk === 0 && i < n - 1) {
        if (cloth[i + 1] === 2) {
          cloth[i + 1] -= 1;
          cloth[i] += 1;
          chk = 1;
          answer += 1;
        }
      }
    }
  }
  return answer;
}

console.log(solution(5, [2, 3, 4], [1, 3]));
