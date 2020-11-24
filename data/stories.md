## booking hotel
* greet
  - utter_greet
* bookrooms
  - utter_how_many_rooms
* bookhotel{"no_of_rooms":"2"}
  - utter_select_type_of_rooms
* bookhotel{"type_of_rooms":"Simple"}
  - utter_confirmation
*goodbye
  -utter_goodbye

## booking hotel 1
*bookrooms
  - utter_how_many_rooms
* bookhotel{"no_of_rooms":"2"}
  - utter_select_type_of_rooms
* bookhotel{"type_of_rooms":"Simple"}
  - utter_confirmation
*goodbye
  -utter_goodbye

## booking hotel 2
* greet
  - utter_greet
* bookroomsadv{"no_of_rooms":"2", "type_of_rooms":"Simple"}
  - utter_confirmation
*goodbye
  -utter_goodbye

## cleaning rooms
* greet
  - utter_greet
* cleanrooms
  - utter_ask_clean_time
* cleannow
  - utter_clean_now
* goodbye
  - utter_goodbye

## cleaning rooms 1
* greet
  - utter_greet
* cleanrooms
  - utter_ask_clean_time
* cleanlater{"hours":"2"}
  - validate_timings
* goodbye
  - utter_goodbye

## faqs

## say goodbye
* goodbye
  - utter_goodbye
