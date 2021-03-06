import random

positive_responses = ['Yes', 'Definitely', 'Absolutely', 'Always', '100%']
negative_responses = ['No', 'Never', 'No Chance', '0%', "I don't know"]
responses_list = positive_responses + negative_responses
pep_words = ['frankie', 'pep']
sus_words = ['sus']


def response(message):
    message = str(message).lower()
    if any(word in message for word in pep_words) and any(
            word in message for word in sus_words) and not "not" in message:
        index = random.randint(0, len(positive_responses) - 1)
        return positive_responses[index]
    else:
        index = random.randint(0, len(responses_list) - 1)
        return responses_list[index]
