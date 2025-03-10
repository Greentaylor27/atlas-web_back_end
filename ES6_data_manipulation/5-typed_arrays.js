export default function createInt8TypedArray(length, position, value) {
  if (position > (length - 1)) {
    throw new Error('Position outside range');
  }

  const arr = new ArrayBuffer(length);
  const view = new DataView(arr);
  view.setInt8(position, value);
  return view;
}
