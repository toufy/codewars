// Does my number look big in this?
// https://www.codewars.com/kata/5287e858c6b5a9678200083c

function narcissistic(value) {
    const numLen = Math.floor(Math.log10(Math.abs(value))) + 1;
    const digits = Math.abs(value).toString().split("").map(Number);
    const digitsExp = digits.map((i) => i ** numLen);
    const sum = digitsExp.reduce((accum, current) => accum + current, 0);
    return sum == value;
}
