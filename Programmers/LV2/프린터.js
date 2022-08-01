function solution(priorities, location) {
  var answer = 0;

  let idx_arr = [];
  for (x = 0; x < priorities.length; x++) {
    idx_arr.push(x);
  }

  while (priorities.length) {
    let max_v = Math.max(...priorities);
    v = priorities.shift();
    i = idx_arr.shift();

    if (v == max_v) {
      answer += 1;
      if (i == location) {
        break;
      }
    } else {
      priorities.push(v);
      idx_arr.push(i);
    }
  }
  return answer;
}
