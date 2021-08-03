const id = document.getElementById('recruit-id').innerText;
let answer_comment = "False" // 답글 여부

function updateEnter(e) {
    if (event.keyCode == 13) {
        e.parentNode.parentNode.childNodes[7].click();
    }
}
function submitEnter(e) {
    if (event.keyCode == 13) {
        e.parentNode.childNodes[2].click();
    }
}

// 댓글 수정
function updateBtn(e) {
    if (e.innerHTML == "수정하기") {
        e.innerHTML = "저장하기";
        e.parentNode.childNodes[11].innerHTML = `<input id="comment-edit" type=text" onkeydown="updateEnter(this)" value="${e.parentNode.childNodes[11].innerHTML}"/>`;
    }
    else {
        text = e.parentNode.childNodes[11].childNodes[0].value;
        answer_comment = "False"

        fetch("/detail_recruit/" + id + "/update_comment/" + e.parentNode.getAttribute('comment_id'), { 
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text,
                answer_comment,
            })
        }).then(res => {
            if (res.status == 200) {
                e.innerHTML = "수정하기";
                e.parentNode.childNodes[11].innerHTML = text
            }
            else {
                alert('수정안됨');
            }
        })
    }
}

// 대댓글 수정
function updateBtn2(e) {
    console.log(e.parentNode.childNodes)
    if (e.innerHTML == "수정하기") {
        e.innerHTML = "저장하기";
        e.parentNode.childNodes[9].innerHTML = `<input id="comment-edit" type=text" onkeydown="updateEnter(this)" value="${e.parentNode.childNodes[9].innerHTML}"/>`;
    }
    else {
        text = e.parentNode.childNodes[9].childNodes[0].value;
        answer_comment = "True"

        fetch("/detail_recruit/" + id + "/update_comment/" + e.parentNode.getAttribute('comment_id'), { 
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text,
                answer_comment,
            })
        }).then(res => {
            if (res.status == 200) {
                e.innerHTML = "수정하기";
                e.parentNode.childNodes[9].innerHTML = text
                answer_comment = "False"
            }
            else {
                alert('수정안됨');
            }
        })
    }
}

// 답글(대댓글) 버튼
function answerBtn(e) {
    e.parentNode.childNodes[13].innerHTML = `<input id="commit-answer" type="text" onkeydown="submitEnter(this)"/> <button onclick="submitBtn(this)">작성</button>`;
    answer_comment = "True";
}

// 댓글, 대댓글 작성 버튼
function submitBtn(e) {
    console.log(e.parentNode.childNodes[0].value)
    text = e.parentNode.childNodes[0].value;
    comment_id = e.parentNode.parentNode.getAttribute('comment_id')

    fetch("/detail_recruit/" + id + "/create_comment/", { 
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text,
            answer_comment,
            comment_id,
        })
    }).then(res => {
        if (res.status == 200) {
            answer_comment = "False"
            window.location.reload()
        }
        else {
            alert('작성안됨');
        }
    })

}