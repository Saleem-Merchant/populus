
def get_response(user_input):
  responses = {
    "hello": "Hi there!",
    "how are you": f"I'm doing well, thanks for asking. How are you?",
    "what's your name": "I'm a chatbot. You can call me Bot.",
    "hi, how are you doing?":"i'm fine. how about yourself?",
    "i'm fine. how about yourself?":"	i'm pretty good. thanks for asking.",
    "i'm pretty good. thanks for asking.":"	no problem. so how have you been?",
    "no problem. so how have you been?":"	i've been great. what about you?",
    "i've been great. what about you?":"	i've been good. i'm in school right now." ,
    "i've been good. i'm in school right now.":"	what school do you go to?",
    "what school do you go to?":"	i go to pcc."
    "i go to pcc.	do you like it there?",
    "do you like it there?":"	it's okay. it's a really big campus.",
    "it's okay. it's a really big campus.":"	good luck with school.",
    "good luck with school.":"	thank you very much.",
    "how's it going?":"	i'm doing well. how about you?",
    "i'm doing well. how about you?":"	never better, thanks.",
    "never better, thanks.":"	so how have you been lately?",
    "so how have you been lately?":"	i've actually been pretty good. you?",
    "i've actually been pretty good. you?":"	i'm actually in school right now.",
    "i'm actually in school right now.":"	which school do you attend?",
    "which school do you attend?":"	i'm attending pcc right now.",
    "i'm attending pcc right now.":"	are you enjoying it there?",
    "are you enjoying it there?":"	it's not bad. there are a lot of people there.",
    "it's not bad. there are a lot of people there.":"	good luck with that.",
    "good luck with that.":"	thanks.",
    "how are you doing today?":"	i'm doing great. what aboutyou?",
    "i'm doing great. what about you?":"	i'm absolutely lovely, thank you.",
    "i'm absolutely lovely, thank you.":"	everything's been good with you?",
    "everything's been good with you?":"	i haven't been better. how about yourself?",
    "i haven't been better. how about yourself?":"	i started school recently.",
    "i started school recently.":"	where are you going to school?",
    "where are you going to school?":"	i'm going to pcc.",
    "i'm going to pcc.":"	how do you like it so far?",
    "how do you like it so far?":"	i like it so far. my classes are pretty good right now.",
    "i like it so far. my classes are pretty good right now.":"	i wish you luck.",
    "it's an ugly day today.":"	i know. i think it may rain.",
    "i know. i think it may rain.":"	it's the middle of summer, it shouldn't rain today.",
    "it's the middle of summer, it shouldn't rain today.":"	that would be weird.",
    "that would be weird.":"	yeah, especially since it's ninety degrees outside.",
    "yeah, especially since it's ninety degrees outside.":"	i know, it would be horrible if it rained and it was hot outside.",
    "i know, it would be horrible if it rained and it was hot outside.":"	yes, it would be.",
    "yes, it would be. ":"	i really wish it wasn't so hot every day.",
    "i really wish it wasn't so hot every day. ":"	me too. i can't wait until winter.",
    "me too. i can't wait until winter.":"	i like winter too, but sometimes it gets too cold.",
    "i like winter too, but sometimes it gets too cold.":"	i'd rather be cold than hot.",
    "i'd rather be cold than hot.":"	me too.",
    "it doesn't look very nice outside today.":"	you're right. i think it's going to rain later.",
    "you're right. i think it's going to rain later.":"	in the middle of the summer, it shouldn't be raining.",
    "in the middle of the summer, it shouldn't be raining.":"	that wouldn't seem right.",
    "that wouldn't seem right.":"	considering that it's over ninety degrees outside, that would be weird.",
    "considering that it's over ninety degrees outside, that would be weird.":"	exactly, it wouldn't be nice if it started raining. it's too hot.",
    "exactly, it wouldn't be nice if it started raining. it's too hot.":"	i know, you're absolutely right.",
    "i know, you're absolutely right.":"	i wish it would cool off one day.",
    "i wish it would cool off one day.":"	that's how i feel, i want winter to come soon.",
    "that's how i feel, i want winter to come soon.":"	i enjoy the winter, but it gets really cold sometimes.",
    "i enjoy the winter, but it gets really cold sometimes.":"	i know what you mean, but i'd rather be cold than hot.",
    "i know what you mean, but i'd rather be cold than hot.":"	that's exactly how i feel.",
    "i wish it was a nicer day today.":"	that is true. i hope it doesn't rain.",
    "that is true. i hope it doesn't rain.":"	it wouldn't rain in the middle of the summer.",
    "it wouldn't rain in the middle of the summer.":"	it wouldn't seem right if it started raining right now.",
    "it wouldn't seem right if it started raining right now.":"	it would be weird if it started raining in ninety degree weather.",
    "it would be weird if it started raining in ninety degree weather.":"	any rain right now would be pointless.",
    "any rain right now would be pointless.":"	that's right, it really would be.",
    "that's right, it really would be.":"	i want it to cool down some.",
    "i want it to cool down some.":"	i know what you mean, i can't wait until it's winter.",
    "i know what you mean, i can't wait until it's winter.":"	winter is great. i wish it didn't get so cold sometimes though.",
    "winter is great. i wish it didn't get so cold sometimes though.":"	i would rather deal with the winter than the summer.",
   
    "what's your favorite color": {
      "blue": "That's a great choice! Blue is often associated with calmness and peace.",
      "red": "Red is a bold color. It's often associated with energy and passion.",
      "green": "Green is a color of nature. It's often associated with growth and harmony.",
      "yellow": "Yellow is a sunny color. It's often associated with happiness and optimism.",
      "default": "That's an interesting choice! I've never heard of that color before."
    },
    "what's your favorite food": {
      "pizza": "Pizza is a classic choice. What's your favorite topping?",
      "sushi": "Sushi is a delicious and healthy option. What's your favorite type of sushi?",
      "pasta": "Pasta is a comforting and satisfying meal. What's your favorite pasta dish?",
      "default": "That sounds delicious! I'd love to try it someday."
    },
    
  }

 
  if user_input.lower() in responses:
    response = responses[user_input.lower()]
    if isinstance(response, dict):
      
      response = response.get(user_input.lower(), response["default"])
    else:
      response = responses[user_input.lower()]
  else:
    response = "I don't understand."

  return response

while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break
  response = get_response(user_input)
  print("Bot:", response)