export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
    task;
    task2;
  }

  return [task, task2];
}