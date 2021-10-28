$(function() {
	//クリックしたときのファンクションをまとめて指定
	$('ul.tab_area li').click(function() {
		//.index()を使いクリックされたタブが何番目かを調べ、
//		indexという変数に代入します。
		var index = $('ul.tab_area li').index(this);

		//コンテンツを一度すべて非表示にし、
		$('.content_area').css('display','none');

		//クリックされたタブと同じ順番のコンテンツを表示します。
		$('.content_area').eq(index).fadeIn();

		//タブについているクラスselectを消し、
		$('.tab_area li').removeClass('select');

		//クリックされたタブのみにクラスselectをつけます。
		$(this).addClass('select')
	});
});

function close() {
    document.querySelector('#modal').innerHTML = '';
    document.getElementById("mask").classList.remove("active");
}

function open(task_id, idName) {
    let update_id = task_id;
    let id_name = idName;
    console.log(id_name);
    let createHtml = '';

    createHtml = '<div class="main_modal active"><h2>確認</h2><div class="modalContents"><h5>お手伝いできた？</h5>';
    createHtml += '<form method="post" action="child_test/#' + id_name + '\"><a class="close_modal" onclick="window.close();">できてない</a>';
    createHtml += '<button type="submit" class="complete_task" value=\"' + update_id + '\" name="complete_id">できた！</button>';
    createHtml += '</form></div></div>';

    document.querySelector('#modal').innerHTML = createHtml;
    document.getElementById("mask").classList.add("active");
}