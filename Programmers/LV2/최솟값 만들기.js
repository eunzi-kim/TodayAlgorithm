function solution(A, B) {
  var answer = 0;

  A.sort((a, b) => {
    return a - b;
  });
  B.sort((a, b) => {
    return a - b;
  });

  for (let i = 0; i < A.length; i++) {
    answer += A[i] * B[A.length - i - 1];
  }

  return answer;
}
