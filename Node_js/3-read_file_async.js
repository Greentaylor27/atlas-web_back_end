const fs = require('fs');

module.exports = function countStudents(path) {
    const promise = new Promise((resolve, reject) => {
            fs.readFile(path, 'utf-8', (error, data) => {
                if (error) {
                    reject(error);
                }
                else {
                    resolve(data);
                    const lines = data.split('\n');
                    const students = lines.slice(1).map(line => line.trim().split(','));
            
                    students.pop(); // To remove the last item in the list which was empty.
            
                    // Count the number of students and list them in CS
                    const csStudents = students.filter(student => student[3] === 'CS');
            
                    // Count the number of students and list them is SWE
                    const sweStudents = students.filter(student => student[3] === 'SWE');
            
                    const count = students.length;
            
                    console.log('Number of students: ', count);
                    console.log(`Number of students in CS: ${csStudents.length}. List: ${csStudents.map(student => student[0]).join(', ')}`);
                    console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.map(student => student[0]).join(', ')}`);
                }
            }
        )
    });
    return promise;
}
