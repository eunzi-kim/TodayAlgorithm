function solution(s) {
  let answer = "";

  const N = s.length;
  let first_word = true;
  for (let v of s) {
    if (v === " ") {
      first_word = true;
      answer += v;
    } else {
      if (first_word && isNaN(Number(v))) {
        answer += v.toUpperCase();
      } else if (isNaN(Number(v))) {
        answer += v.toLowerCase();
      } else {
        answer += String(v);
      }
      first_word = false;
    }
  }
  return answer;
}
