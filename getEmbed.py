#this fix oembeb video width bug 
#TODO fix this sorcery - add variables asap this is crap
import requests
import json

#url = 'https://x.com/redGobot/status/1842979888321749128'
#url = 'https://x.com/redGobot/status/1848225918457958535'
url =  'https://x.com/greenGobot/status/1855377011654443411'

params = {
    'url': url,
    'hide_media':False,
    'hide_thread':True,
    'omit_script':False,
    'align':'center',
    'lang':'en',
    'theme':'dark',
    'dnt':True,
    'omit_script':True,
}

response = requests.get('https://publish.twitter.com/oembed', params=params)
json_data = json.loads(response.text)

pre_blockquote = json_data['html']
pre_blockquote = pre_blockquote.split('class="twitter-tweet"')
blockquote     = f'{pre_blockquote[0]} class="twitter-tweet" data-media-max-width="1920" {pre_blockquote[1]}'
print(blockquote)

html ='''
<!DOCTYPE html>
<html>
<head>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style.css">
    <title>DEF CON Radio</title>
</head>
<body>

  <center>
   %s
   <p class="small">*for a better "experience" use stereo headphones</p>
   <p class="big">This is totally not a PSYOP Right? RIGHT?</p>
  </center>


  <div class="chat">
    <script src="https://nocomment.fiatjaf.com/embed.js" id="nocomment" 
            data-custom-base="nevent1qqsvz4kzyv9h8vske4et95nq9393y6ps28880l7qcy3qeksw2kc6rvszyqvcjq6w26u0vpk8yn695ykwsjs3sstzr2hhrq4p7ety8q9ecsnkkqcyqqqqqqgtjlel5"
            data-placeholder="The Love Placeholder is here!"
            data-skip="#"
            data-relays='["wss://nos.lol"]'>
    </script>
  </div>

</body>
<script>window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);

  t._e = [];
  t.ready = function(f) {
    t._e.push(f);
  };

  return t;
}(document, "script", "twitter-wjs"));</script> 

</html>''' % (blockquote)
with open("index.html", "w") as f:
  print(html, file=f)
