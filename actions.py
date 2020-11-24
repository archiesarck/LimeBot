# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, Form
import logging
import datetime

#logger = logging.getLogger(__name__)

#REQUESTED_SLOT = "requested_slot"

# no_of_rooms = 0


class ValidateTimings(Action):
    def name(self) -> Text:
        return "validate_timings"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        hours = tracker.get_slot("cleaning_hours")
        current_date_and_time = datetime.datetime.now()
        hours_added = datetime.timedelta(hours = hours)
        future_date_and_time = current_date_and_time + hours_added
        hrs = future_date_and_time.strftime("%H")
        if (int(hrs) >= 21) or (int(hrs) <= 4):
            msg = "Sorry, cleaning service is unavailable in this time. Can you try some other time?"
        else:
            msg = "I will arrange a cleaning at " + hrs + " hrs today."
        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_message(text=msg)
        return []


class HowManyRooms(Action):
    def name(self) -> Text:
        return "how_many_rooms"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        types = ["Simple", "Deluxe"]
        for t in types:
            payload = "/bookhotel{\"type_of_rooms\": \"" + t + "\"}"

            buttons.append(
                {"title": "{}".format(t),
                 "payload": payload})
        
        # TODO: update rasa core version for configurable `button_type`
        dispatcher.utter_button_template("utter_select_type_of_rooms", buttons, tracker)
        return []
