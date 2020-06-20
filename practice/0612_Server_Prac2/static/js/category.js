function show_top(country_code) {
    $('#cardBox').empty()

    $.ajax({
        type: "GET",
        url: `/api/top/${country_code}`,
        data: {},
        success: function (response) {
            let articles = response['articles_list']
            for (let i = 0; i < articles.length; i++) {
                let article = articles[i];

                let objectid = article['_id']
                let country_code = article['country_code']
                let time_unix = article['time']
                let time = fn_dateTimeToFormatted(time_unix)
                let url_title = article['url_title']
                let url = article['url']
                let url_img = article['url_img']
                let post_body = article['post_body']
                let happy = article['happy']

                if (url == '') {
                    card = make_card(country_code, time, post_body, objectid, happy);
                } else {
                    card = make_card_url(country_code, time, post_body, url_img, url_title, url, objectid, happy);
                }

                $('#cardBox').append(card)
            }
        }
    });
}

function show_new(country_code) {
    $('#cardBox').empty()

    $.ajax({
        type: "GET",
        url: `/api/new/${country_code}`,
        data: {},
        success: function (response) {
            let articles = response['articles_list']
            for (let i = 0; i < articles.length; i++) {
                let article = articles[i];

                let objectid = article['_id']
                let country_code = article['country_code']
                let time_unix = article['time']
                let time = fn_dateTimeToFormatted(time_unix)
                let url_title = article['url_title']
                let url = article['url']
                let url_img = article['url_img']
                let post_body = article['post_body']
                let happy = article['happy']

                if (url == '') {
                    card = make_card(country_code, time, post_body, objectid, happy);
                } else {
                    card = make_card_url(country_code, time, post_body, url_img, url_title, url, objectid, happy);
                }

                $('#cardBox').append(card)
            }
        }
    });
}