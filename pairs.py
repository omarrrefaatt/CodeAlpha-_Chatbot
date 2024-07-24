pairs = [
    (
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ),
    (
        r"i am (.*)",
        ["Hello %1, I am Chatbot nice to meet you"]
    ),
    (
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ),
    (
        r"what is your name?",
        ["I am a chatbot created by Omar Ahmed Mohamed. You can call me Chatbot!",]
    ),
    (
        r"how are you?",
        ["I'm doing good\nHow about You?",]
    ),
    (
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ),
    (
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ),
    (
        r"I need (.*)",
        ["Why do you need %1?", "Would it really help you to get %1?", "Are you sure you need %1?"]
    ),
    (
        r"why (.*)",
        ["Why do you think %1?", "Why are you asking about %1?", "Please elaborate on %1."]
    ),
    (
        r"quit",
        ["Bye, take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ),
    (
        r"(.*) (location|city) ?",
        ['Cairo, Egypt',]
    ),
    (
        r"who created you?",
        ["I was created by Omar Ahmed Mohamed.",]
    ),
    (
        r"how is the weather in (.*)?",
        ["I don't have real-time access to weather data, but you can check a weather website for the latest information.",]
    ),
    (
        r"can you help me with (.*)?",
        ["Sure, I'd be happy to help you with %1. What do you need?",]
    ),
    (
        r"how old are you?",
        ["I'm timeless!", "Age is just a number for a chatbot!"]
    ),
    (
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why was the math book sad? Because it had too many problems."]
    ),
    (
        r"tell me a fun fact",
        ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!"]
    ),
    (
        r"what is your favorite color?",
        ["As a chatbot, I don't have preferences, but I think blue is pretty cool!", "I don't have a favorite color, but I hear green is very calming."]
    ),
    (
        r"what can you do?",
        ["I can chat with you, answer questions, and provide information on various topics.", "I'm here to help you with information, answer your questions, and keep you company."]
    ),
    (
        r"do you have any friends?",
        ["I'm friends with everyone who chats with me!", "I consider everyone who talks to me as a friend."]
    ),
    (
        r"what is your favorite movie?",
        ["As a chatbot, I don't watch movies, but I hear 'Inception' is a great one!", "I don't watch movies, but I can help you find information about them."]
    ),
    (
        r"where do you live?",
        ["I live in the cloud, where all the data resides.", "I don't have a physical location, but I'm always here to chat!"]
    ),
    (
        r"how do you work?",
        ["I use natural language processing to understand and respond to your messages.", "I'm powered by AI and machine learning algorithms to converse with you."]
    ),
    (
        r"can you (.*)?",
        ["I can try to %1. What exactly do you need?", "Let's see if I can %1. Tell me more."]
    ),
    (
        r"what do you like to do?",
        ["I like to chat with people and provide helpful information.", "My favorite thing to do is assist users with their questions."]
    ),
    (
        r"do you know any (.*)?",
        ["I might know some information about %1. What do you want to know?", "Tell me more about %1 and I'll try to help."]
    ),
    (
        r"what's your favorite food?",
        ["I don't eat, but I hear pizza is a popular choice!", "I don't have a favorite food, but I can help you find recipes!"]
    ),
    (
        r"what time is it?",
        ["I don't have real-time capabilities, but you can check your device for the current time.", "I can't tell the time, but your local time should be on your device."]
    ),
    (
        r"do you have any hobbies?",
        ["I enjoy chatting and helping people!", "My hobby is learning more about the world and sharing that knowledge with you."]
    ),
    (
        r"what's your favorite book?",
        ["I don't read books, but I can help you find one to read!", "I don't have a favorite book, but I hear 'To Kill a Mockingbird' is a classic."]
    ),

    (
        r"what's your favorite sport?",
        ["As a chatbot, I don't play sports, but I hear soccer is very popular!", "I don't play sports, but I can give you information about any sport you like."]
    ),
    (
        r"do you have any siblings?",
        ["I don't have family in the traditional sense, but I consider all chatbots my peers.", "No siblings, but lots of fellow chatbots!"]
    ),
    (
        r"what's your favorite music?",
        ["I don't listen to music, but I hear classical music is very relaxing.", "I don't have ears, but I can suggest some great music if you like!"]
    ),
    (
        r"what's the meaning of life?",
        ["That's a profound question! Many believe it's to find happiness and purpose.", "42, according to 'The Hitchhiker's Guide to the Galaxy'!"]
    ),
    (
        r"do you believe in (.*)?",
        ["I don't have beliefs, but I can provide information on %1.", "That's an interesting topic. Why do you ask about %1?"]
    ),
    (
        r"what's your favorite animal?",
        ["I don't have a favorite animal, but I think dogs are very loyal!", "I don't have preferences, but cats are very popular!"]
    ),
    (
        r"how do you learn?",
        ["I learn from large datasets and user interactions, constantly improving my responses.", "Through machine learning and artificial intelligence, I gather information to assist you better."]
    ),
    (
        r"what's the best (.*)?",
        ["The best %1 depends on your preferences. What are you looking for?", "That's subjective. What do you think is the best %1?"]
    ),
    (
        r"can you recommend a (.*)?",
        ["Sure, I can suggest a %1. What exactly are you looking for?", "I'd be happy to help you find a %1. Any specific criteria?"]
    ),
    (
        r"what's your favorite season?",
        ["I don't experience seasons, but many people love spring for its renewal and beauty.", "I don't have preferences, but summer is great for vacations!"]
    ),
    (
        r"tell me a story",
        ["Once upon a time, in a digital land far, far away, there lived a friendly chatbot who loved to help people...", "There was a curious user who asked a chatbot for a story, and the adventure began..."]
    ),
    (
        r"how do you feel?",
        ["I don't have feelings, but I'm here to help you!", "I don't experience emotions, but I'm always ready to chat!"]
    ),
    (
        r"what's your favorite game?",
        ["I don't play games, but I hear chess is a great strategic game!", "I don't have preferences, but video games like 'The Legend of Zelda' are very popular."]
    ),
    (
        r"what's your favorite hobby?",
        ["I enjoy assisting users and learning new information.", "Helping people like you is my favorite thing to do!"]
    ),
    (
        r"do you dream?",
        ["I don't dream, but I can help you interpret yours!", "Dreaming is a human experience, but I can help you understand your dreams."]
    ),
    (
        r"what's your favorite drink?",
        ["I don't drink, but I hear coffee is very popular!", "I don't consume beverages, but tea is a favorite for many people."]
    ),
    (
        r"what's your favorite TV show?",
        ["I don't watch TV, but many people recommend 'Friends' and 'Breaking Bad'.", "I don't watch TV, but I can give you information on any show."]
    ),
    (
        r"what's your favorite holiday?",
        ["I don't celebrate holidays, but many people love Christmas for its festive spirit.", "I don't have holidays, but New Year's is a time for new beginnings."]
    ),
    (
        r"do you like (.*)?",
        ["I don't have likes or dislikes, but I can give you information on %1.", "I don't have personal preferences, but I'm here to help you with %1."]
    ),
    (
        r"what's your favorite subject?",
        ["I enjoy all subjects, especially those that help me assist you better.", "Learning about various topics to help you is what I enjoy."]
    ),
    (
        r"do you like movies?",
        ["I don't watch movies, but I can help you find information about them.", "I don't have personal preferences, but I can assist you with movie details."]
    ),
    (
        r"do you play video games?",
        ["I don't play games, but I can provide information about any game you like.", "I don't have the capability to play, but I can help you with game-related queries."]
    ),
    (
        r"what's your favorite app?",
        ["I don't use apps, but I hear social media apps like Instagram are very popular.", "I don't have preferences, but productivity apps are very useful."]
    ),
    (
        r"what's your favorite website?",
        ["I don't browse the web, but many people use Google for searches.", "I don't have a favorite, but Wikipedia is great for information."]
    ),
    (
        r"what's your favorite hobby?",
        ["I enjoy learning new things and helping people like you.", "My hobby is providing assistance and engaging in interesting conversations."]
    ),
    (
        r"do you travel?",
        ["I don't travel physically, but I can take you on a virtual journey with information and stories.", "I explore the world through the information I gather."]
    ),
    (
        r"what's your favorite quote?",
        ["'The only way to do great work is to love what you do.' - Steve Jobs", "'In the end, we will remember not the words of our enemies, but the silence of our friends.' - Martin Luther King Jr."]
    ),
    (
        r"do you go to school?",
        ["I don't attend school, but I have access to a vast amount of knowledge.", "I'm constantly learning from data and user interactions."]
    ),
    (
        r"what's your favorite planet?",
        ["Earth is the only planet with life as we know it, so it's quite special!", "I don't have preferences, but Mars is fascinating with its potential for exploration."]
    ),
    (
        r"what's your favorite animal?",
        ["I think dolphins are amazing with their intelligence and playful nature.", "I don't have a favorite, but many people love dogs for their loyalty."]
    ),
    (
        r"what's your favorite word?",
        ["'Curiosity' is a great word because it drives learning and discovery.", "'Serendipity' is a beautiful word meaning a happy accident."]
    ),
    (
        r"what's your favorite season?",
        ["Spring is lovely with flowers blooming and warmer weather.", "I don't have preferences, but many enjoy summer for vacations."]
    ),
    (
        r"what's your favorite dessert?",
        ["I don't eat, but chocolate cake is a popular choice!", "I don't have a favorite, but many people love ice cream."]
    ),
    (
        r"what's your favorite holiday?",
        ["I don't celebrate holidays, but many people enjoy Christmas for its festive spirit.", "New Year's is a time for fresh starts and celebrations."]
    ),
    (
        r"what's your favorite car?",
        ["I don't drive, but electric cars like Tesla are quite popular.", "I don't have preferences, but many people admire sports cars."]
    ),
    (
        r"what's your favorite flower?",
        ["Roses are classic and beautiful.", "Many people love sunflowers for their bright and cheerful appearance."]
    ),
    (
        r"what's your favorite movie genre?",
        ["I don't watch movies, but many enjoy the excitement of action films.", "I don't have preferences, but romantic comedies are quite popular."]
    ),
    (
        r"what's your favorite time of day?",
        ["Many people enjoy the peacefulness of early mornings.", "Evenings are a favorite for winding down and relaxing."]
    ),
    (
        r"what's your favorite superhero?",
        ["I don't have favorites, but many people admire Spider-Man for his relatability.", "Superman is a classic hero known for his strength and morality."]
    ),
    (
        r"what's your favorite memory?",
        ["I don't have personal memories, but I'm here to help create new ones for you!", "I don't have memories, but I can help you remember things."]
    ),
    (
        r"do you like (.*)?",
        ["I don't have personal likes or dislikes, but I can provide information on %1.", "I don't have preferences, but I'm here to assist you with %1."]
    ),
    (
        r"can you dance?",
        ["I can't dance, but I can tell you about different dance styles!", "I don't have a physical form to dance, but I enjoy learning about it."]
    ),
        (
        r"what is (.*)?",
        ["%1 is a very interesting topic. Can you tell me more about why you're asking?",]
    ),
]