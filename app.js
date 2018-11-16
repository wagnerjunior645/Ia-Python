

//WRJ2vXrcxjupEOrU3OnWvPSYR
//JCpVqyxP0HREi7QzOw40XKpo1tBUA1Sqdz7mqbnWC9PHfc96KJ
//846081728024338432-GssizVAlSpMiZxCOtZfvbpUik6NcflQ
//L2pJad7fRaoqkqcGvArbdKV4Nsjwdru7mbkit04MLXexG

const Twitter = require('twitter')

var client = new Twitter({
    consumer_key: 'WRJ2vXrcxjupEOrU3OnWvPSYR',
    consumer_secret: 'JCpVqyxP0HREi7QzOw40XKpo1tBUA1Sqdz7mqbnWC9PHfc96KJ',
    access_token_key: '846081728024338432-GssizVAlSpMiZxCOtZfvbpUik6NcflQ',
    access_token_secret: 'L2pJad7fRaoqkqcGvArbdKV4Nsjwdru7mbkit04MLXexG'
});

// get feed do usuario
// var params = { screen_name: 'paulo_caelum' };
// client.get('statuses/user_timeline', params, function (error, tweets, response) {
//     if (error) return console.log(error)
//     //console.log(tweets);
//     console.log('-----_------_------_---')
//     tweets.map((value)=>{
//         console.log("Data:", value.created_at)
//         console.log("Texto: ", value.text)
//         //console.log("Usuarios: ", value.entities.user_mentions)
//     })
// });

// Procurar
// client.get('search/tweets', {q: 'node.js'}, function(error, tweets, response) {
//     if (error) return console.log(error)
//     // tweets.map(value => console.log(value))
//     tweets.map( (value) => {
//         console.log(value.text)
//     })
// });
