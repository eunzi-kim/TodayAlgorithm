function solution(n) {
  let arr = [];

  for (let i = 0; i <= n; i++) {
    if (i <= 1) {
      arr.push(i);
    } else {
      let temp = (arr[i - 1] + arr[i - 2]) % 1234567;
      arr.push(temp);
    }
  }

  return arr[n];
}
