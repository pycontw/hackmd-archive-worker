# Automate the Boring Stuff with Slackbot - Takanori Suzuki

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/qphn7osl" height=450 width=100%></iframe>

> 從這開始

[slides](https://gitpitch.com/takanory/slides?p=20190922pycontw#/)

## About speaker
* Takanori Suzuki
    * [twitter](https://twitter.com/takanory)

## Q&A
* How to avoid 3 second response time limit from slack api?
    * We send manual message instead of program response, so we don't really have this 3 second timeout issue.
* how to debug slack api if the slack message is not show up as expected?
    * You can set channel or username to `ERRORS_TO` in `slackbot_settings.py`. Then you can get error report from slackbot in the channel or DM.


###### tags: `PyConTW2019`
