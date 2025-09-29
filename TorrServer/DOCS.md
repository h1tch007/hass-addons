### Http Api of TorrServer:
#### GET

###### /echo 
*Return version of server*

###### /shutdown 
*Shutdown server*

###### /stream...
#### args:
* link - magnet/hash/link to torrent
* index - index of file
* preload - preload torrent
* stat - return stat of torrent
* save - save to db
* m3u - return m3u
* fromlast - return m3u from last play
* play - start stream torrent
* title - set title of torrent
* poster - set poster link of torrent

##### Examples:
>**get stat**
>
>http://127.0.0.1:8090/stream/fname?link=...&stat
>
>**get m3u**
>
>http://127.0.0.1:8090/stream/fname?link=...&index=1&m3u
>http://127.0.0.1:8090/stream/fname?link=...&index=1&m3u&fromlast
>
>**stream torrent**
>
>http://127.0.0.1:8090/stream/fname?link=...&index=1&play
>http://127.0.0.1:8090/stream/fname?link=...&index=1&play&save
>http://127.0.0.1:8090/stream/fname?link=...&index=1&play&save&title=...&poster=...
>
>**only save**
>
>http://127.0.0.1:8090/stream/fname?link=...&save&title=...&poster=...

###### /play/:hash/:id
#### params:
* hash - hash of torrent
* index - index of file

###### /playlistall/all.m3u
*Get all http links of all torrents in m3u list*

###### /playlist
*Get http link of torrent in m3u list*
#### args:
* hash - hash of torrent
* fromlast - from last play file

#
#### POST
###### /torrents
##### Send json:
{\
    "action": "add/get/set/rem/list/drop",\
    "link": "hash/magnet/link to torrent",\
    "hash": "hash of torrent",\
    "title": "title of torrent",\
    "poster": "link to poster of torrent",\
    "data": "custom data of torrent, may be json",\
    "save_to_db": true/false\
}
##### Return json of torrent(s)

###### /torrent/upload
##### Send multipart/form data
Only one file support
#### args:
* title - set title of torrent
* poster - set poster link of torrent
* data - set custom data of torrent, may be json
* save - save to db

###### /cache
##### Send json:
{\
    "action": "get"\
    "hash" : ""hash": "hash of torrent",\
}
##### Return cache stat 
https://github.com/YouROK/TorrServer/blob/d36d0c28f805ceab39adb4aac2869cd7a272085b/server/torr/storage/state/state.go

###### /settings
##### Send json:
{\
    "action": "get/set/def",\
    _fields of BTSets_\
}
##### Return json of BTSets
https://github.com/YouROK/TorrServer/blob/d36d0c28f805ceab39adb4aac2869cd7a272085b/server/settings/btsets.go

###### /viewed
##### Send json:
{\
    "action": "set/rem/list",\
    "hash": "hash of torrent",\
    "file_index": int, id of file,\
}
##### Return
if hash is empty, return all viewed files\
if hash is not empty, return viewed file of torrent 
##### Json struct see in
https://github.com/YouROK/TorrServer/blob/d36d0c28f805ceab39adb4aac2869cd7a272085b/server/settings/viewed.go



#
### Authorization

The user data file should be located near to the settings.\
Basic auth, read more in wiki \
https://en.wikipedia.org/wiki/Basic_access_authentication

File name: *accs.db*\
File format:

{\
    "User1": "Pass1",\
    "User2": "Pass2"\
}



#
### Whitelist/Blacklist ip
The lists file should be located near to the settings.

whitelist file name: wip.txt\
blacklist file name: bip.txt

whitelist has prior

Example:\
local:127.0.0.0-127.0.0.255\
127.0.0.0-127.0.0.255\
local:127.0.0.1\
127.0.0.1\
\# at the beginning of the line, comment


#
### Developed by
###### **YouROK** [github.com/YouROK](https://github.com/YouROK/)
https://github.com/YouROK/TorrServer