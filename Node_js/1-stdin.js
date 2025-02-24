process.stdout.write("Welcome to Holberton School, what is your name?\n");
process.stdin.on('data', data => {
    data = data.toString().charAt(0).toUpperCase() + data.slice(1);
    console.log(`Your name is: ${data}`);
});
process.on('exit', () => {
    process.stdout.write("This important software is now closing\n");
});
