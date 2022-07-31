function solution(arr) {
  var answer = 1;

  for (let v of arr) {
    let min_v = Math.min(answer, v);
    let max_v = Math.max(answer, v);
    let temp = 1;
    for (let x = 1; x <= min_v; x++) {
      if (min_v % x === 0 && max_v % x === 0) {
        temp = x;
      }
    }

    answer = parseInt((min_v * max_v) / temp);
  }
  return answer;
}
