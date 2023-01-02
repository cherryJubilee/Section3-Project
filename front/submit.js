const form = document.querySelector("form");

function handleSubmit(event) {
  event.preventDefault();
  const answer1 = document.querySelector('input[name=answer1]:checked').value;
  const answer2 = document.querySelector('input[name=answer2]:checked').value;
  const answer3 = document.querySelector('input[name=answer3]:checked').value;
  const answer4 = document.querySelector('input[name=answer4]:checked').value;
  const answer5 = document.querySelector('input[name=answer5]:checked').value;
  const answer6 = document.querySelector('input[name=answer6]:checked').value;
  const answer7 = document.querySelector('input[name=answer7]:checked').value;
  const answer8 = document.querySelector('input[name=answer8]:checked').value;
  const answer_mbti = document.querySelector('input[name=answer_mbti]').value;
  const answers = answer1 + answer2 + answer3 + answer4 + answer5 + answer6 + answer7 + answer8 + answer_mbti;
  if (answer_mbti === "") { //Q9 문항에 답하지 않으면 동물 페이지로 이동
    fetch('http://3.39.5.135/survey/' + answers, { method: 'POST' })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
  } else { // Q9 문항에 답하면 (SQL) 데이터에 등록
    fetch('http://3.39.5.135/survey/' + answers)
  }
}


function init(){
    form.addEventListener("submit", handleSubmit);
  }
  
init();