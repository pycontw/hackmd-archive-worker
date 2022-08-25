---
tags: 2021-organize, 2021-web, dev team
---

# PyCon TW website API document

## ccip

- ### ~~CCIPAPIView~~
    - Code: src/ccip/views.py:187
    - Method: GET
    - URL: /ccip/
    - Responses:
        ``` json
        {
            "rooms": [
                "string"
            ],
            "sessions": [
                "string"
            ],
            "session_types": [
                "string"
            ],
            "speakers": [
                "string"
            ],
            "tags": [
                "string"
            ],
        }
        ```

---

## events

- ### TalkListView
    - Code: src/events/views.py:41
    - Method: GET
    - URL: /conference/talks/
    - Responses:
        ``` json
        {
            "talk_category_list_pairs": [
                {
                    "category": "string",
                    "talk_list": [
                        "id": 0,
                        "title": "string",
                        "speaker_names": "string",
                        "labels": "string"
                    ]
                }
            ]
            "sponsored_events": [
                {
                    "title": "string",
                    "host_name": "string",
                    "url": "string"
                }
            ]
        }
        ```

- ### TutorialListView (Benson)
    - Code: src/events/views.py:80
    - Method: GET
    - URL: /conference/tutorials/
    - Responses:
        ``` json
        {
            "tutorials": [
                {
                    "title": "string",
                    "abstract": "string",
                    "tutorial_id": integer
                }
            ]
        }
        ```
    http://127.0.0.1:8000/api/events/tutorials/
    ![](https://i.imgur.com/chdjCSs.png)




- ### ScheduleView
    - Code: src/events/views.py:95
    - Method: GET
    - URL: /conference/schedule/
    - Responses:
        ``` json
        {
            "schedule_html": "string",
            "schedule_days": [
                {
                    "date": "2020-09-05",
                    "info": "string"
                }
            ]
        }
        ```

- ### ~~ScheduleCreateView~~
    - Code: src/events/views.py:142
    - Method: POST
    - URL: /conference/schedule/new/


- ### 4. TalkDetailView (Maliao)
    - Code: src/events/views.py:256
    - Method: GET
    - URL: /conference/talk/{id}/
    - Responses:
        ``` json
        {
            "title": "string",
            "category": "string",
            "language": "string",
            "python_level": "string",
            "recording_policy": "string",
            "abstract": "string",
            "detailed_description": "string",
            "slide_link": "string",
            "slido_embed_link": "string",
            "sponsored": true,
            "speakers": [
                {
                    "thumbnail_url": "string",
                    "name": "string",
                    "github_profile_url": "string",
                    "twitter_profile_url": "string",
                    "facebook_profile_url": "string"
                }
            ]
        }
        ```

    http://127.0.0.1:8000/api/events/talk/1
    ![](https://i.imgur.com/EtT1jnk.png)


- ### ~~SponsoredEventDetailView~~
    - Code: src/events/views.py:265
    - Method: GET
    - URL: /conference/sponsored/talk/{slug}/
    - Responses:
        ``` json
        {
            "title": "string",
            "category": "string",
            "language": "string",
            "python_level": "string",
            "recording_policy": "string",
            "abstract": "string",
            "detailed_description": "string",
            "slide_link": "string",
            "slido_embed_link": "string",
            "sponsored": true,
            "speakers": [
                {
                    "thumbnail_url": "string",
                    "name": "string",
                    "github_profile_url": "string",
                    "twitter_profile_url": "string",
                    "facebook_profile_url": "string"
                }
            ]
        }
        ```

- ### TutorialDetailView
    - Code: src/events/views.py:284
    - Method: GET
    - URL: /conference/tutorial/{id}/
    - Responses:
        ``` json
        {
            "title": "string",
            "location": "string",
            "date": "2020-09-05",
            "begin_time": "2020-09-05 13:50:00",
            "end_time": "2020-09-05 15:20:00",
            "category": "string",
            "language": "string",
            "python_level": "string",
            "abstract": "string",
            "detailed_description": "string",
            "slide_link": "string",
            "slido_embed_link": "string",
            "speakers": [
                {
                    "thumbnail_url": "string",
                    "name": "string",
                    "github_profile_url": "string",
                    "twitter_profile_url": "string",
                    "facebook_profile_url": "string"
                }
            ]
        }
        ```

- ### Job Listings
    - Code: src/events/templatetags.py:135
    - Method: GET
    - URL: /events/jobs/
    - Responses:
        ``` json
        {
            "data": [
                {
                    "sponsor_logo_url": "string",
                    "sponsor_name": "string",
                    "jobs": [
                        {
                            "job_url": "string",
                            "job_name": "string",
                            "job_description": "string"
                        }
                    ]
                }
            ]
        }
        ```

---

## sponsors

- ### SponsorListView
    - Code: src/sponsors/views.py:8
    - Method: GET
    - URL: /sponsors/
    - Responses:
        ``` json
        {
            "data": [
                {
                    "level_name": "string",
                    "sponsors": [
                        {
                            "name": "string",
                            "intro": "string",
                            "website_url": "string",
                            "logo_url": "string"
                        }
                    ]
                }
                
            ]
        }
        ```
    