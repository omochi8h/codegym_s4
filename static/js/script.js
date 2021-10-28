 function close() {
    document.querySelector('#modal').innerHTML = '';
    document.getElementById("mask").classList.remove("active");
}

function open(task_id, id_name) {
    let update_id = task_id;
    let tab_name = id_name;
    let createHtml = '';


    createHtml = '<div class="main_modal active"><div class="modalContents"><h5>お手伝いできた？</h5>';
    createHtml += '<form method="post" action=\"http://127.0.0.1:8000/child_tasklist/' + tab_name + '\"><button type="button" class="close_modal" onclick="window.close();"><img src="static/img/batu.png" style="height:3vh;"></button>';
    createHtml += '<button type="submit" class="complete_task" value=\"' + update_id + '\" name="complete_id"><img src="static/img/maru.png" style="height:3vh;"></button>';
/*
    createHtml = '<div class="main_modal active"><h2>確認</h2><div class="modalContents"><h5>お手伝いできた？</h5>';
    createHtml += '<form method="post" action=\"http://127.0.0.1:8000/child_tasklist/' + tab_name + '\"><a class="close_modal" onclick="window.close();">できてない</a>';
    createHtml += '<button type="submit" class="complete_task" value=\"' + update_id + '\" name="complete_id">◯</button>';
*/
    createHtml += '</form></div></div>';
    document.querySelector('#modal').innerHTML = createHtml;
    document.getElementById("mask").classList.add("active");
}

window.addEventListener('DOMContentLoaded', function(){

	var input_genders = document.querySelectorAll("input[name=gender]");

	for(var element of input_genders) {
		element.checked = false;
	}

	var url = location.href;
    if (url.length >= 38) {
        var get_id = url.substr(37,70);
    } else {
        var get_id = 'tab1';
    }

    var element = document.getElementById(get_id) ;
    element.checked = true ;
});


