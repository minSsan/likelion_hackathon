id = document.getElementById('recruit-id').innerText;
    
function onKeyDown(e) {
    if (event.keyCode == 13) {
        e.parentNode.parentNode.childNodes[7].click();
    }
}

function updateBtn(e) {
    if (e.innerHTML == "수정하기") {
        e.innerHTML = "저장하기";
        e.parentNode.childNodes[9].innerHTML = `<input id="comment-edit" type=text" onkeydown="onKeyDown(this)" value="${e.parentNode.childNodes[9].innerHTML}"/>`;
    }
    else {
        text = e.parentNode.childNodes[9].childNodes[0].value;

        fetch("/detail_recruit/" + id + "/update_comment/" + e.parentNode.getAttribute('comment_id'), { 
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text,
            })
        }).then(res => {
            if (res.status == 200) {
                e.innerHTML = "수정하기";
                e.parentNode.childNodes[9].innerHTML = text
            }
            else {
                alert('수정안됨');
            }
        })
    }
}
        