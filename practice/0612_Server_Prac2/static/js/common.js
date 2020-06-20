function fn_dateTimeToFormatted(dt) {
  var min = 60 * 1000;
  var c = new Date()
  var d = new Date(dt * 1000);
  var minsAgo = Math.floor((c - d) / (min));

  var result = {
    'raw': d.getFullYear() + '-' + (d.getMonth() + 1 > 9 ? '' : '0') + (d.getMonth() + 1) + '-' + (d.getDate() > 9 ? '' : '0') + d.getDate() + ' ' + (d.getHours() > 9 ? '' : '0') + d.getHours() + ':' + (d.getMinutes() > 9 ? '' : '0') + d.getMinutes() + ':' + (d.getSeconds() > 9 ? '' : '0') + d.getSeconds(),
    'formatted': '',
  };

  if (minsAgo < 60) { // 1시간 내
    result.formatted = minsAgo + '분 전';
  } else if (minsAgo < 60 * 24) { // 하루 내
    result.formatted = Math.floor(minsAgo / 60) + '시간 전';
  } else if (minsAgo < 60 * 24 * 30) { // 하루 이상
    result.formatted = Math.floor(minsAgo / 60 / 24) + '일 전';
  } else if (minsAgo < 60 * 24 * 365) { // 1달 이상
    result.formatted = Math.floor(minsAgo / 60 / 24 / 30) + '달 전';
  } else { // 1년 이상
    result.formatted = Math.floor(minsAgo / 60 / 24 / 365) + '년 전';
  };

  return result.formatted;
};

function make_card(country_code, time, post_body, objectid, happy) {
  let temp_html =
    `<div class="card">
      <header>
        <a href="/${country_code}">${country_code}</a>
        <p>${time}</p>
      </header>

      <section>
        <h3>${post_body}</h3>
      </section>

      <div>
        <button onclick="delete_card('${objectid}')">
          삭제
        </button>
      </div>

      <footer class="card-footer">
        <button onclick="happy('${objectid}')">
          <div>😊</div>
          <div id="happy_${objectid}">${happy}</div>
        </button>
        <a href="/${country_code}/${objectid}">
          <div>💬</div>
          <div id="happy_${objectid}">${happy}</div>
        </a>
      </footer>
    </div>`
  return temp_html;
}

function make_card_url(country_code, time, post_body, url_img, url_title, url, objectid, happy) {
  let temp_html =
    `<div class="card">
      <header>
        <a href="/${country_code}">${country_code}</a>
        <p>${time}</p>
      </header>

      <section>
        <h3>${post_body}</h3>
        <div class="thumbnail_box">
          <div class="thumbnail_image">
            <img src="${url_img}" alt="thumbnail image"/>
          </div>
          <a href="${url}" target="_blank">${url_title}</a>
        </div>
      </section>

      <div>
        <button onclick="delete_card('${objectid}')">
          삭제
        </button>
      </div>

      <footer class="card-footer">
        <button onclick="happy('${objectid}')">
          <div>😊</div>
          <div id="happy_${objectid}">${happy}</div>
        </button>
        <a href="/${country_code}/${objectid}">
          <div>💬</div>
          <div id="happy_${objectid}">${happy}</div>
        </a>
      </footer>
    </div>`
  return temp_html;
}



function posting() {
  let post_body = $('#postingBody').val();
  let country_code = $('#countryCode').val();

  $.ajax({
    type: "POST",
    url: "/api/compose",
    data: {
      'country_code_give': country_code, 
      'post_body_give': post_body
    },
    success: function(response) {
      if (response['result'] == 'success') {
        window.location.reload()
      }
    }
  })
}



function happy(objectid) {
  $.ajax({
    type: "POST",
    url: "/api/happy",
    data: { 'objectid_give': objectid },
    success: function(response) {
      if (response['result'] == 'success') {
        let new_happy = response['article_happy'] + 1;
        let happyCount = parseInt($('#happy_' + objectid).text());
        happyCount = $('#happy_' + objectid).text(new_happy)
      }
    }
  });
}

function delete_card(objectid) {
  $.ajax({
    type: "POST",
    url: "/api/delete",
    data: { 'objectid_give': objectid },
    success: function(response) {
      if (response['result'] == 'success') {
        alert('삭제 완료!')
        window.location.reload()
      }
    }
  });
}