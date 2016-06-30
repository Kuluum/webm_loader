# Webm loader
Usable for 2ch.hk, other boards and any page that has webm.

## Version
1.0

## Parser

webm_parser.py script.

Takes html page url as parameter and returns list of webm urls from this page.

### Usage

#### Call

```sh
$ python webm_parser.py http://domain.com/webm_cool_videos.html
```

#### Result

```sh
http://domain.com/cool_story.webm
http://domain.com/asian_video.webm
http://domain.com/memes_compilation.webm
```
## Loader

Have no own loader now. But you can use wget. Easy.

```sh
$ python webm_parser.py http://domain.com/webm_cool_videos.html > webms.txt
$ wget -nc -i webms.txt -P webm_folder
```
