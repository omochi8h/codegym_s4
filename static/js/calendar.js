'use strict'

function close() {
    document.querySelector('#modal').innerHTML = '';
    document.getElementById("mask").classList.remove("active");
}

function open(task_id) {
    let update_id = task_id;
    let createHtml = '';

    createHtml = '<div class="main_modal active"><h2>確認</h2><div class="modalContents"><h5>お手伝いできた？</h5>';
    createHtml += '<form method="post"><a class="close_modal" onclick="window.close();">できてない</a>';
    createHtml += '<button type="submit" class="complete_task" value=\"' + update_id + '\" name="complete_id">できた！</button>';
    createHtml += '</form></div></div>';

    document.querySelector('#modal').innerHTML = createHtml;
    document.getElementById("mask").classList.add("active");
}

function close_modal() {
  document.querySelector('#modal').innerHTML = '';
  document.getElementById("mask").classList.remove("active");
}

function open_modal(work_list) {
  var work = work_list;
  let createHtml = '';

  createHtml = '<div class="main_modal active"><div class="modalContents"><h5>さすが！！</h5><div class="list">';
  for (let i = 0; i < work.length; i++){
    createHtml += '<p>' +'＊'+ work[i] + '</p>';
  }
  createHtml += '</div><a class="close_modal" onclick="window.close_modal();" style="background-color:#f2d58a;color:#800000;">閉じる</a>';
  createHtml += '</div></div>';

  document.querySelector('#modal').innerHTML = createHtml;
  document.getElementById("mask").classList.add("active");
}




function createCalendar(histry, p_year, p_month, get_child_id) {

  const date = new Date();
  var year = date.getFullYear();
  if (year != p_year) {
    year = p_year
  }
  var month = date.getMonth() + 1;
  if (month != p_month) {
    month = p_month
  }
  //最初の日付
  const firstDate = new Date(year, month-1, 1);
  //最初の曜日
  const firstDay = firstDate.getDay();
  //最後の日付
  const lastDate = new Date(year, month, 0);
  const lastDayCount = lastDate.getDate();

  let dayCount = 1;
  let createHtml = '';

  createHtml = '<form method="post" action="http://127.0.0.1:8000/child_history/tab1"><button class="mae" name="key" value=\"-,0,' + year + '-' + month + ',' +  get_child_id + '\">まえのつき</button>'
  createHtml += '<span>' + year + 'ねん' + month + 'がつ' + '</span>';
  createHtml += '<form method="post"><button name="key" class ="usiro" value=\"+,0,' + year + '-' + month + ',' +  get_child_id + '\">つぎのつき</button></form>'

  createHtml += '<table>' + '<tr>';

  const weeks = ['にち','げつ','か','すい','もく','きん','ど'];
  for (let i = 0; i < weeks.length; i++) {
      createHtml += '<td>' + weeks[i] + '</td>';
  }
  createHtml += '</tr>';

  for (let n = 0; n < 6; n++) {
      createHtml += '<tr>';
      if (dayCount > lastDayCount) {
        break;
      }

      for (let d = 0; d < 7; d++) {
          if (n == 0 && d < firstDay) {
              createHtml += '<td></td>';
          } else if (dayCount > lastDayCount) {
              createHtml += '<td></td>';
          } else {
              if (histry[dayCount - 1] == 0) {
                createHtml += '<td>' + dayCount + '</td>';
                dayCount += 1;
              } else {
                let work_list = histry[dayCount - 1];
                let len = work_list.length;
                let array = [];
                for (let i = 0; i < len; i++){
                  if(len == 1) {
                    var work = '[\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else if(i == 0) {
                    var work = '[\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  } else if(i == len - 1) {
                    var work = '\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else {
                    var work = '\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  }
                }
                createHtml += '<td class="good" onclick=\"window.open_modal(' + array + ')\"><img class="p_img" src="../../static/img/good.png"><a class="day">' + dayCount + '</a></td>';
                dayCount += 1;
              }

          }

      }

      createHtml += '</tr>';
  }
  createHtml += '</table>';

  document.querySelector('#calendar').innerHTML = createHtml;
}

function createCalendar2(histry, p_year, p_month, get_child_id) {
  const date = new Date();
  var year = date.getFullYear();
  if (year != p_year) {
    year = p_year
  }
  var month = date.getMonth() + 1;
  if (month != p_month) {
    month = p_month
  }
  //最初の日付
  const firstDate = new Date(year, month-1, 1);
  //最初の曜日
  const firstDay = firstDate.getDay();
  //最後の日付
  const lastDate = new Date(year, month, 0);
  const lastDayCount = lastDate.getDate();

  let dayCount = 1;
  let createHtml = '';


  createHtml = '<form method="post" action="http://127.0.0.1:8000/child_history/tab2"><button name="key" class="mae" value=\"-,1,' + year + '-' + month + ',' +  get_child_id + '\">まえのつき</button>'

  createHtml += '<span>' + year + 'ねん' + month + 'がつ' + '</span>';
  createHtml += '<form method="post"><button name="key"  class ="usiro" value=\"+,1,' + year + '-' + month + ',' +  get_child_id + '\">つぎのつき</button></form>'
  createHtml += '<table>' + '<tr>';

  const weeks = ['にち','げつ','か','すい','もく','きん','ど'];
  for (let i = 0; i < weeks.length; i++) {
      createHtml += '<td>' + weeks[i] + '</td>';
  }
  createHtml += '</tr>';

  for (let n = 0; n < 6; n++) {
      createHtml += '<tr>';
    if (dayCount > lastDayCount) {
        break;
      }
      for (let d = 0; d < 7; d++) {
          if (n == 0 && d < firstDay) {
              createHtml += '<td></td>';
          } else if (dayCount > lastDayCount) {
              createHtml += '<td></td>';
          } else {
              if (histry[dayCount - 1] == 0) {
                createHtml += '<td>' + dayCount + '</td>';
                dayCount += 1;
              } else {
                let work_list = histry[dayCount - 1];
                let len = work_list.length;
                let array = [];
                for (let i = 0; i < len; i++){
                  if(len == 1) {
                    var work = '[\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else if(i == 0) {
                    var work = '[\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  } else if(i == len - 1) {
                    var work = '\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else {
                    var work = '\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  }
                }
                createHtml += '<td class="good" onclick=\"window.open_modal(' + array + ')\"><img class="p_img" src="../../static/img/good.png"><a class="day" onclick=\"window.open_modal(' + array + ')\">' + dayCount + '</a></td>';
                dayCount += 1;
              }

          }

      }

      createHtml += '</tr>';
  }
  createHtml += '</table>';

  document.querySelector('#calendar2').innerHTML = createHtml;
}

function createCalendar3(histry, p_year, p_month, get_child_id) {
  const date = new Date();
  var year = date.getFullYear();
  if (year != p_year) {
    year = p_year
  }
  var month = date.getMonth() + 1;
  if (month != p_month) {
    month = p_month
  }
  //最初の日付
  const firstDate = new Date(year, month-1, 1);
  //最初の曜日
  const firstDay = firstDate.getDay();
  //最後の日付
  const lastDate = new Date(year, month, 0);
  const lastDayCount = lastDate.getDate();

  let dayCount = 1;
  let createHtml = '';


  createHtml = '<form method="post" action="http://127.0.0.1:8000/child_history/tab3"><button class="mae" name="key" value=\"-,2,' + year + '-' + month + ',' +  get_child_id + '\">まえのつき</button>'

  createHtml += '<span>' + year + 'ねん' + month + 'がつ' + '</span>';
  createHtml += '<form method="post"><button name="key" class ="usiro" value=\"+,2,' + year + '-' + month + ',' +  get_child_id + '\">つぎのつき</button></form>'
  createHtml += '<table>' + '<tr>';

  const weeks = ['にち','げつ','か','すい','もく','きん','ど'];
  for (let i = 0; i < weeks.length; i++) {
      createHtml += '<td>' + weeks[i] + '</td>';
  }
  createHtml += '</tr>';

  for (let n = 0; n < 6; n++) {
      createHtml += '<tr>';
      if (dayCount > lastDayCount) {
        break;
      }

      for (let d = 0; d < 7; d++) {
          if (n == 0 && d < firstDay) {
              createHtml += '<td></td>';
          } else if (dayCount > lastDayCount) {
              createHtml += '<td></td>';
          } else {
              if (histry[dayCount - 1] == 0) {
                createHtml += '<td>' + dayCount + '</td>';
                dayCount += 1;
              } else {
                let work_list = histry[dayCount - 1];
                let len = work_list.length;
                let array = [];
                for (let i = 0; i < len; i++){
                  if(len == 1) {
                    var work = '[\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else if(i == 0) {
                    var work = '[\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  } else if(i == len - 1) {
                    var work = '\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else {
                    var work = '\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  }
                }
                createHtml += '<td class="good" onclick=\"window.open_modal(' + array + ')\"><img class="p_img" src="../../static/img/good.png"><a class="day" onclick=\"window.open_modal(' + array + ')\">' + dayCount + '</a></td>';
                dayCount += 1;
              }

          }

      }

      createHtml += '</tr>';
  }
  createHtml += '</table>';

  document.querySelector('#calendar3').innerHTML = createHtml;
}

function createCalendar4(histry, p_year, p_month, get_child_id) {
  const date = new Date();
  var year = date.getFullYear();
  if (year != p_year) {
    year = p_year
  }
  var month = date.getMonth() + 1;
  if (month != p_month) {
    month = p_month
  }
  //最初の日付
  const firstDate = new Date(year, month-1, 1);
  //最初の曜日
  const firstDay = firstDate.getDay();
  //最後の日付
  const lastDate = new Date(year, month, 0);
  const lastDayCount = lastDate.getDate();

  let dayCount = 1;
  let createHtml = '';
  createHtml = '<form method="post" action="http://127.0.0.1:8000/child_history/tab4"><button class="mae" name="key" value=\"-,3,' + year + '-' + month + ',' +  get_child_id + '\">まえのつき</button>'
  createHtml += '<span>' + year + 'ねん' + month + 'がつ' + '</span>';
  createHtml += '<form method="post"><button name="key" class ="usiro" value=\"+,3,' + year + '-' + month + ',' +  get_child_id + '\">つぎのつき</button></form>'
  createHtml += '<table>' + '<tr>';

  const weeks = ['にち','げつ','か','すい','もく','きん','ど'];
  for (let i = 0; i < weeks.length; i++) {
      createHtml += '<td>' + weeks[i] + '</td>';
  }
  createHtml += '</tr>';

  for (let n = 0; n < 6; n++) {
      createHtml += '<tr>';

      for (let d = 0; d < 7; d++) {
          if (n == 0 && d < firstDay) {
              createHtml += '<td></td>';
          } else if (dayCount > lastDayCount) {
              createHtml += '<td></td>';
          } else {
              if (histry[dayCount - 1] == 0) {
                createHtml += '<td>' + dayCount + '</td>';
                dayCount += 1;
              } else {
                let work_list = histry[dayCount - 1];
                let len = work_list.length;
                let array = [];
                for (let i = 0; i < len; i++){
                  if(len == 1) {
                    var work = '[\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else if(i == 0) {
                    var work = '[\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  } else if(i == len - 1) {
                    var work = '\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else {
                    var work = '\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  }
                }
                createHtml += '<td class="good"><img class="p_img" src="../../static/img/good.png"><a class="day" onclick=\"window.open_modal(' + array + ')\">' + dayCount + '</a></td>';
                dayCount += 1;
              }

          }

      }

      createHtml += '</tr>';
  }
  createHtml += '</table>';

  document.querySelector('#calendar4').innerHTML = createHtml;
}

function createCalendar5(histry, p_year, p_month, get_child_id) {
  const date = new Date();
  var year = date.getFullYear();
  if (year != p_year) {
    year = p_year
  }
  var month = date.getMonth() + 1;
  if (month != p_month) {
    month = p_month
  }
  //最初の日付
  const firstDate = new Date(year, month-1, 1);
  //最初の曜日
  const firstDay = firstDate.getDay();
  //最後の日付
  const lastDate = new Date(year, month, 0);
  const lastDayCount = lastDate.getDate();

  let dayCount = 1;
  let createHtml = '';

  createHtml = '<form method="post" action="http://127.0.0.1:8000/child_history/tab5"><button name="key" value=\"-,4,' + year + '-' + month + ',' +  get_child_id + '\">まえのつき</button>'
  createHtml += '<span>' + year + 'ねん' + month + 'がつ' + '</span>';
  createHtml += '<form method="post"><button name="key" class ="usiro" value=\"+,4,' + year + '-' + month + ',' +  get_child_id + '\">つぎのつき</button></form>'
  createHtml += '<table>' + '<tr>';

  const weeks = ['にち','げつ','か','すい','もく','きん','ど'];
  for (let i = 0; i < weeks.length; i++) {
      createHtml += '<td>' + weeks[i] + '</td>';
  }
  createHtml += '</tr>';

  for (let n = 0; n < 6; n++) {
      createHtml += '<tr>';

      for (let d = 0; d < 7; d++) {
          if (n == 0 && d < firstDay) {
              createHtml += '<td></td>';
          } else if (dayCount > lastDayCount) {
              createHtml += '<td></td>';
          } else {
              if (histry[dayCount - 1] == 0) {
                createHtml += '<td>' + dayCount + '</td>';
                dayCount += 1;
              } else {
                let work_list = histry[dayCount - 1];
                let len = work_list.length;
                let array = [];
                for (let i = 0; i < len; i++){
                  if(len == 1) {
                    var work = '[\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else if(i == 0) {
                    var work = '[\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  } else if(i == len - 1) {
                    var work = '\'' + String(work_list[i]) + '\']';
                    array.push(work);
                  } else {
                    var work = '\'' + String(work_list[i]) + '\'';
                    array.push(work);
                  }
                }
                createHtml += '<td class="good"><img class="p_img" src="../../static/img/good.png"><a class="day" onclick=\"window.open_modal(' + array + ')\">' + dayCount + '</a></td>';
                dayCount += 1;
              }

          }

      }

      createHtml += '</tr>';
  }
  createHtml += '</table>';

  document.querySelector('#calendar5').innerHTML = createHtml;
}
window.addEventListener('DOMContentLoaded', function(){

	var input_genders = document.querySelectorAll("input[name=gender]");

	for(var element of input_genders) {
		element.checked = false;
	}

	var url = location.href;
    if (url.length >= 37) {
        var get_id = url.substr(36,39);
    } else {
        var get_id = 'tab1';
    }
    console.log(get_id);

    var element = document.getElementById(get_id) ;
    element.checked = true ;
});




