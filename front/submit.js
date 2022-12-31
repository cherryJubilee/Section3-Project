const submitButton = document.querySelector(".button--submit");


const form = document.querySelector("form");

function handleSubmit(event){
    event.preventDefault();
    const answer1 = document.querySelector('input[name=answer1]:checked').value;
    const answer2 = document.querySelector('input[name=answer2]:checked').value;
    const answer3 = document.querySelector('input[name=answer3]:checked').value;
    const answer4 = document.querySelector('input[name=answer4]:checked').value;
    const answer5 = document.querySelector('input[name=answer5]:checked').value;
    const answers = answer1 + answer2 + answer3 + answer4 + answer5;
    fetch('http://127.0.0.1:8000/survey/' + answers)
    .then(function(response) {
        console.log(JSON.stringify(response));
        return response.json();
    })
  }


function init(){
    form.addEventListener("submit", handleSubmit);
  }
  
init();