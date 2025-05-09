function calculateNumber(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    if (type === 'SUM') {
        return roundedA + roundedB;
    }
    else if (type === 'SUBTRACT') {
        return roundedA - roundedB;
    }
    else if (type === 'DIVIDE') {
        if (roundedB === 0) {
            return 'Error';
        }
        else {
            return roundedA / roundedB;
        }
    }
    else {
        return 'Invalid operation';
    }
}
module.exports = calculateNumber
