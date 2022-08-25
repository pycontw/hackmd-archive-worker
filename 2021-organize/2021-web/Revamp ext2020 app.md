---
tags: 2021-organize, 2021-web, dev team
---

🔙 Back to [PyCon TW Organizing 共筆](https://hackmd.io/@pycontw/SyG5_GrED/https%3A%2F%2Fhackmd.io%2F%40pycontw%2FByi2hyM9w)

# Revamp `ext2020` app

 - Trello card: ![](https://github.trello.services/images/mini-trello-icon.png) [Revamp `ext2020` app](https://trello.com/c/vYNToMLT/50-revamp-ext2020-app)
- Souce code: [pycon.tw/src/ext2020/](https://github.com/pycontw/pycon.tw/tree/master/src/ext2020)
    
## Implementation

### Verification API

**`POST` `/attendee/verify`**

#### Usage

The API is implemented for verifying if the token is valid (generated by KKTIX system and imported into our Django backend). If the token is valid, the data that is disclose only for attendee is also inserted into the response body.

#### Parameter

| Field | Type   | Description           |
| ----- | ------ | --------------------- |
| token | string | the token of Attendee |

```bash
# example
{
   "token": "80c74ec3ddb2434346280fca2a10ac97"
}
```

#### Success 200

| Field                            | Type     | Description              |
| -------------------------------- | -------- | ------------------------ |
| yotube_infos                     | Object[] | List of live rooms infos |
| &nbsp;&nbsp;&nbsp;&nbsp;room     | string   | name of live room        |
| &nbsp;&nbsp;&nbsp;&nbsp;video_id | string   | ID of the YouTube video  |

```bash
# example
{
   "youtube_infos": [
       {
           "room": "R1",
           "video_id": "FNPxeqJEbR3"
       },
       {
           "room": "R2",
           "video_id": "tN3TxBT78W3"
       },
       ...
   ]
}
```

#### Error 4xx

| Field            | Description                                                                             |
| ---------------- | --------------------------------------------------------------------------------------- |
| AttendeeNotExist | Only authenticated attendee can access the data. Please contact staff for further help. |