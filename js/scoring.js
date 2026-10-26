/** Pure scoring module — independent of UI/storage, used in Node regression tests. */
export function isComplete(question, value) {
  if (question.type === 'single') return typeof value === 'string' && question.options.some(x => x.id === value);
  if (question.type === 'multiple') return Array.isArray(value) && value.length > 0 && value.every(x => question.options.some(o => o.id === x));
  if (question.type === 'category') return value && typeof value === 'object' && !Array.isArray(value) && question.options.every(o => question.categories.some(c => c.id === value[o.id]));
  return false;
}
export function evaluate(question, value) {
  if (!question.graded || question.answer == null) return 'unresolved';
  if (!isComplete(question, value)) return 'unanswered';
  if (question.type === 'single') return value === question.answer[0] ? 'correct' : 'incorrect';
  if (question.type === 'multiple') {
    const chosen = [...new Set(value)].sort();
    const required = [...question.answer].sort();
    return chosen.length === required.length && chosen.every((x, i) => x === required[i]) ? 'correct' : 'incorrect';
  }
  if (question.type === 'category') return question.options.every(row => value[row.id] === question.answer[row.id]) ? 'correct' : 'incorrect';
  throw new Error(`Unsupported question type: ${question.type}`);
}
export function scoreTest(test, responses = {}) {
  const evaluations = {};
  let correct = 0, incorrect = 0, unanswered = 0, unresolved = 0, answered = 0;
  for (const q of test.questions) {
    const answer = responses[q.id];
    if (isComplete(q, answer)) answered++;
    const status = evaluate(q, answer);
    evaluations[q.id] = status;
    if (status === 'correct') correct++;
    else if (status === 'incorrect') incorrect++;
    else if (status === 'unanswered') unanswered++;
    else unresolved++;
  }
  const gradable = correct + incorrect + unanswered;
  return {evaluations, correct, incorrect, unanswered, unresolved, answered, gradable,
    total: test.questions.length, percentage: gradable > 0 ? Math.round(100 * correct / gradable) : null};
}
export function prettyAnswer(q, value) {
  if (!isComplete(q, value)) return 'Belum dijawab';
  if (q.type === 'single') return value;
  if (q.type === 'multiple') return [...new Set(value)].sort().join(', ');
  return q.options.map(r => `${r.id}: ${value[r.id] === 'Yes' ? 'Ya' : 'Tidak'}`).join(' · ');
}
export function officialAnswer(q) {
  if (!q.graded || q.answer == null) return 'Belum terverifikasi';
  if (q.type === 'category') return q.options.map(o => `${o.id}: ${q.answer[o.id] === 'Yes' ? 'Ya' : 'Tidak'}`).join(' · ');
  return q.answer.join(', ');
}
