
import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa.core.events import UserUtteranceReverted

TURING_ROBOT_URL = 'http://openapi.tuling123.com/openapi/api/v2'


class DefaultFallback(Action):
    def name(self):
        return "action_customize_default_fallback"

    def call_turing_robot(self, msg, req_type=0):
        data = {
            "reqType": req_type,
            "perception":{
                "inputText":{
                    "text": msg
                }
            },
            "userInfo":{
                "apiKey": "fe8aeb632d174a708e89ef915833d546",
                "userId": "58dfd2f343de724c"
            }
        }
        print(data)
        resp = requests.post(TURING_ROBOT_URL, json=data)
        result = resp.json()
        print('---------------------------')
        print(result)
        return [r['values'] for r in result.get("results", [])]

    def run(self, dispatcher, tracker, domain):

        text = tracker.latest_message.get('text')

        # msg = self.call_turing_robot(text)

        # if msg:
        #     return [create_bot_utterance(msg)]
        #     # dispatcher.utter_message(msg)
        # else:
        dispatcher.utter_template('utter_default', tracker)

        return []