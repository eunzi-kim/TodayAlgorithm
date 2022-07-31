function solution(s) {
  let max_v = -1000000000000000;
  let min_v = 1000000000000000;
  let temp = "";
  for (let v of s) {
    if (v === " ") {
      if (Number(temp) < min_v) {
        min_v = Number(temp);
      }
      if (Number(temp) > max_v) {
        max_v = Number(temp);
      }
      temp = "";
    } else if (v === "-") {
      temp = "-";
    } else {
      temp += v;
    }
  }
  if (Number(temp) < min_v) {
    min_v = Number(temp);
  }
  if (Number(temp) > max_v) {
    max_v = Number(temp);
  }

  return String(min_v) + " " + String(max_v);
}
