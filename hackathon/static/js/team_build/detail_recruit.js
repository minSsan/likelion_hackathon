const id = document.getElementById('recruit-id').innerText;
let answer_comment = "False" // 답글 여부

function updateEnter(e) {
    if (event.keyCode == 13) {
        console.log(e.parentNode.parentNode.childNodes[5].childNodes[3])
        e.parentNode.parentNode.childNodes[5].childNodes[3].click();
    }
}
function submitEnter(e) {
    if (event.keyCode == 13) {
        e.parentNode.childNodes[5].click();
    }
}

// 댓글 삭제
function deleteBtn1(e) {
    fetch("/recruit/detail_recruit/" + id + "/delete_comment/" + e.parentNode.parentNode.parentNode.parentNode.getAttribute('comment_id') + "/False").then(res => {
        if(res.status == 200) window.location.reload();
        else alert('삭제안됨');
    })
}
function deleteBtn2(e) {
    fetch("/recruit/detail_recruit/" + id + "/delete_comment/" + e.parentNode.parentNode.parentNode.parentNode.getAttribute('comment_id') + "/True").then(res => {
        if(res.status == 200) window.location.reload();
        else alert('삭제안됨');
    })
}

// 댓글 수정
function updateBtn(e) {
    if (e.innerHTML == "수정") {
        e.innerHTML = "저장";
        e.parentNode.parentNode.childNodes[3].innerHTML = `<input id="comment-edit" type=text" onkeydown="updateEnter(this)" value="${e.parentNode.parentNode.childNodes[3].innerHTML}"/>`;
    }
    else {
        text = e.parentNode.parentNode.childNodes[3].childNodes[0].value;
        answer_comment = "False"

        fetch("/recruit/detail_recruit/" + id + "/update_comment/" + e.parentNode.parentNode.parentNode.parentNode.getAttribute('comment_id'), { 
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
                e.innerHTML = "수정";
                e.parentNode.parentNode.childNodes[3].innerHTML = text
            }
            else {
                alert('수정안됨');
            }
        })
    }
}

// 대댓글 수정
function updateBtn2(e) {
    if (e.innerHTML == "수정") {
        e.innerHTML = "저장";
        e.parentNode.parentNode.childNodes[3].innerHTML = `<input id="comment-edit" type=text" onkeydown="updateEnter(this)" value="${e.parentNode.parentNode.childNodes[3].innerHTML}"/>`;
    }
    else {
        text = e.parentNode.parentNode.childNodes[3].childNodes[0].value;
        answer_comment = "True"

        fetch("/recruit/detail_recruit/" + id + "/update_comment/" + e.parentNode.parentNode.parentNode.parentNode.getAttribute('comment_id'), { 
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
                e.innerHTML = "수정";
                e.parentNode.parentNode.childNodes[3].innerHTML = text
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
    console.log(e.parentNode.parentNode.childNodes[7])
    e.parentNode.parentNode.childNodes[7].innerHTML = `            <div class="small-profile-img"></div>
    <input type="text" class="comment-input" onkeydown="submitEnter(this)" placeholder="댓글 입력"/>
    <button class="comment-btn" onclick="submitBtn(this)">작성</button>`;
    answer_comment = "True";
}

// 댓글, 대댓글 작성 버튼
function submitBtn(e) {
    console.log(e.parentNode.childNodes)
    text = e.parentNode.childNodes[3].value;
    comment_id = e.parentNode.parentNode.parentNode.parentNode.getAttribute('comment_id')

    fetch("/recruit/detail_recruit/" + id + "/create_comment/", { 
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