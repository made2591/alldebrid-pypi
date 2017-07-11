# Alldebrid API
Alldebrid service torrent API (premium account required) to handle torrent download programmatically.

Run on Python v2. It has following dependencies:

- certifi==2017.4.17
- chardet==3.0.4
- idna==2.5
- requests==2.18.1
- urllib3==1.21.1

After cloning, run the following (eventually in virtualenv):

```shell
pip install -r requirements.txt
```

### Features:
- lists all torrent in download with information;
- provide unlocked link to download torrent already finished;
- upload of magnet link to alldebrid portal;

### Todo:
- improve errors handling;
- improve cli;
- porting of logging (see project ****);

### Improvements
- flood prevention;
- cookie caching (already implemented but not tested yet);
- logic control and torrent page tailing;
