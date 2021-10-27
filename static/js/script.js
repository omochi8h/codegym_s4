 function close() {
    document.querySelector('#modal').innerHTML = '';
    document.getElementById("mask").classList.remove("active");
}

function open(task_id) {
    let update_id = task_id;
    let createHtml = '';

    createHtml = '<div class="main_modal active"><h2>確認</h2><div class="modalContents"><h5>お手伝いできた？</h5>';
    createHtml += '<form method="post"><a class="close_modal" onclick="window.close();">できてない</a>';
    createHtml += '<button type="submit" class="complete_task" value=\"' + update_id + '\" name="complete_id">◯</button>';
    createHtml += '</form></div></div>';

    document.querySelector('#modal').innerHTML = createHtml;
    document.getElementById("mask").classList.add("active");
}