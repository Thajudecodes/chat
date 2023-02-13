import re


def Bot_Response(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        Bot_Response(message, ['hello', 'hi', 'hey', 'sup'],
                     'Hello there, your AI companion is here to serve you.\nYou can talk normally or Type (cmd) to get started '),

        Bot_Response(message, ['bye', 'goodbye'], 'Please don\'t go!'),

        Bot_Response(message, ['cmd', 'type cmd'], 'click me /list'),

        Bot_Response(message, ['how', 'are', 'you'],
                     'I\'m doing fine thanks!'),
        # new
        Bot_Response(message, ['how', 'you', 'created'],
                     'I was created by using python and got deployed on Herkou'),

        # Name
        Bot_Response(message, ['your', 'name'],
                     'My name is thaju\'s Bot, nice to meet you!'),
        # Help
        Bot_Response(message, ['help', 'please'],
                     'I will do my best to assist you!'),
        # Website
        Bot_Response(message, ['link', 'links', ], 'website https://github.com/Thajudecodes'),

        # Song
        Bot_Response(message, ['play', 'song', ],
                     'https://youtu.be/edzt82nC45k'),

        # Notes
        Bot_Response(message, ['notes', 'note', ],
                     'Soon, notes will be available'),

        Bot_Response(message, ['socials', 'socials', ],
                     'Here you Go\n /socials'),

        Bot_Response(message, ['source', 'code', ],
                     'Here you Go\n /source_code'),

        # Nude Joke Lol
        Bot_Response(message, [
                     'nude', 'nudes', ], 'I just took a screenshot, and I\'m sending your photo to @armiy_v right now, you lil horny ass😏'),

        # When Querry
        Bot_Response(message, ['when', '?', 'query', 'question', 'inform',
                     'developer'], 'Inquire with the developer about this. @armiy_v'),

        # When Website
        Bot_Response(message, ['website', 'amrohan', 'web', 'developer'],
                     'https://github.com/Thajudecodes'),

        # When Projects
        Bot_Response(message, ['projects', 'project', 'proj','pro','projec', 'proje'],
                     'Here you Go\n /projects'),

    ]

    response_scores = [response[0] for response in response_list]
    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response
