const alumnosUrl = 'http://lb-prodpro-1434514222.us-east-1.elb.amazonaws.com:8000/students';
const profesoresUrl = 'http://lb-prodpro-1434514222.us-east-1.elb.amazonaws.com:8080/professors';
const clasesUrl = 'http://lb-prodpro-1434514222.us-east-1.elb.amazonaws.com:8081/classes';

function loadStudents() {
    fetch(alumnosUrl)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = JSON.stringify(data.students, null, 2);
        })
        .catch(error => console.error('Error:', error));
}

function loadProfessors() {
    fetch(profesoresUrl)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = JSON.stringify(data.professors, null, 2);
        })
        .catch(error => console.error('Error:', error));
}

function loadClasses() {
    fetch(clasesUrl)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = JSON.stringify(data.classes, null, 2);
        })
        .catch(error => console.error('Error:', error));
}
