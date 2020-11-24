## conv 1
* greet
  - utter_greet
* cleanrooms
  - utter_ask_clean_time
* cleannow
  - utter_clean_now
* bookrooms
  - utter_no_rooms
* bookhotel{"no_of_rooms":"2"}
  - how_many_rooms
  - slot{"type_of_rooms":"Simple"}
* bookhotel{"type_of_rooms":"Simple"}
  - utter_confirmation
* goodbye
  -utter_goodbye

## conv 2
* bookrooms
  - utter_no_rooms
* bookhotel{"no_of_rooms":"2"}
  - how_many_rooms
  - slot{"type_of_rooms":"Simple"}
* bookhotel{"type_of_rooms":"Simple"}
  - utter_confirmation
* cleanrooms
  - utter_ask_clean_time
* schedulecleantime{"cleaning_hours":"3"}
  - validate_timings
* goodbye
  -utter_goodbye

## conv 3
* greet
  - utter_greet
* bookhoteladv{"no_of_rooms":"2", "type_of_rooms":"Simple"}
  - utter_confirmation
* cleanrooms
  - utter_ask_clean_time
* schedulecleantime{"cleaning_hours":"3"}
  - validate_timings
* checkintiming
  - utter_check_in_time
* checkouttime
  - utter_checkout_time
* goodbye
  -utter_goodbye

## conv 4
* greet:
  - utter_greet
* bookhotel{"no_of_rooms":"2"}
  - how_many_rooms
  - slot{"type_of_rooms":"Simple"}
* bookhotel{"type_of_rooms":"Simple"}
  - utter_confirmation
* cleanrooms
  - utter_ask_clean_time
* schedulecleantime{"cleaning_hours":"3"}
  - validate_timings
* checkintiming
  - utter_check_in_time
* checkouttime
  - utter_checkout_time
* goodbye
  -utter_goodbye

## conv 1
* cleanrooms
  - utter_ask_clean_time
* cleannow
  - utter_clean_now
* goodbye
  -utter_goodbye