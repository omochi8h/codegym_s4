 function close() {
    document.querySelector('#modal').innerHTML = '';
    document.getElementById("mask").classList.remove("active");
}

function open(task_id) {
    let update_id = task_id;
    let createHtml = '';

    createHtml = '<div class="main_modal active"><div class="modalContents"><h5>お手伝いできた？</h5>';
    createHtml += '<form method="post"><button type="button" class="close_modal" onclick="window.close();"><img src="static/img/batu.png" style="height:3vh;"></button>';
    createHtml += '<button type="submit" class="complete_task" value=\"' + update_id + '\" name="complete_id"><img src="static/img/maru.png" style="height:3vh;"></button>';
    createHtml += '</form></div></div>';

    document.querySelector('#modal').innerHTML = createHtml;
    document.getElementById("mask").classList.add("active");
}