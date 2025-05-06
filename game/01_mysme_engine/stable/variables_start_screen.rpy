init -6 python:
    class DayGreeting(object):
        """
        Class to keep track of different daily greetings. Can include
        Korean/English translations.

        Attributes:
        -----------
        sound_file : string
            Path to the file for the greeting sound.
        english : string
            Dialogue of the greeting, in English.
        korean : string
            Dialogue of the greeting, in Korean.
        extension : string
            The extension for this file. If none is given, defaults to
            greeting_audio_extension.
        """

        def __init__(self, sound_file, english=False, korean=False,
                extension=None):
            """Creates a DayGreeting object to store a daily greeting."""

            ext = extension if extension is not None else greeting_audio_extension
            self.sound_file = (store.greeting_audio_path + sound_file + ext)
            self.english = english or "Welcome to Mysterious Messenger!"
            self.korean = korean or "제 프로그램으로 환영합니다!"


## Greeting Text
## These are defaults for when the DayGreeting object does not have
## a translation
default greet_text_korean = _("제 프로그램으로 환영합니다!")
default greet_text_english = _("Welcome to Mysterious Messenger!")
default greet_eng_size = 27
default greet_kor_size = 25

## This lets the program randomly pick a greet
## character to display for greetings
default greet_char = 's'

# Path where the audio files for greetings are stored
define greeting_audio_path = "audio/sfx/Main Menu Greetings/"
define greeting_audio_extension = ".wav"

#************************************
# Menu Greeting Lookup
#************************************

## Dictionary with the speaking character as the key and a list of
## DayGreetings as the value. Allows the program to look up a greeting
## based on the time of day
define late_night_greeting = {
    'ja': [ DayGreeting('Jaehee/Late Night/ja-ln-1',
            "Working so hard till late.",
            "늦은 밤까지 열심이시군요"),
            DayGreeting('Jaehee/Late Night/ja-ln-2',
            "I watched Zen's DVD all night and it's now the break of dawn.",
            "젠 씨의 DVD 보다보니 벌써 새벽이 되었네요."),
            DayGreeting('Jaehee/Late Night/ja-ln-3',
            "Why don't you go to sleep early in preparation for tomorrow?",
            "내일을 위해 일찍 주무시는 건 어떨까요?")],

    'ju': [ DayGreeting('Jumin/Late Night/ju-ln-1',
            "Still awake?",
            "아직 깨어있었나?"),
            DayGreeting('Jumin/Late Night/ju-ln-2',
            "Why not try some wine if you can't sleep?",
            "잠이 안 온다면 와인을 마시는 건 어때?"),
            DayGreeting('Jumin/Late Night/ju-ln-3',
            "Nocturnal, just like Elizabeth the 3rd.",
            "야행성인 건 엘리자베스 3세와 닮았군")],

    's': [ DayGreeting('Seven/Late Night/s-ln-1',
            "1 kitty, 2 kitties, 3 kitties, 4 kitties",
            "고양이 한 마리 고양이 두 마리 고양이 세 마리 고양이 네 마리"),
            DayGreeting('Seven/Late Night/s-ln-2',
            "Aren't you sleeping yet?",
            "당신, 아직도 안 잤어요?"),
            DayGreeting('Seven/Late Night/s-ln-3',
            "U wanted to talk till late with us, right? Yippee!",
            "이 늦은 시간에도 우리랑 이야기하고 싶은 거예요? 오예 신난다!")],

    'u': [ DayGreeting('Unknown/Late Night/u-ln-1',
            "I'll be watching over your every move",
            "내가 네 일거수일투족을 지켜보겠어"),
            DayGreeting('Unknown/Late Night/u-ln-2',
            "I'll gulp you down in the dead of the night when you least expect it.",
            "방심하면 새벽이 널 잡아먹을 거야"),
            DayGreeting('Unknown/Late Night/u-ln-3',
            "Sleep tight, the results aren't going to change whether you sleep or not.",
            "푹 자도 돼. 깨어있든 잠을 자든 결과는 바뀌지 않을 테니")],

    'v': [ DayGreeting('V/Late Night/v-ln-1',
            "Look at that night sky. I should take out my camera.",
            "밤하늘을 봐요. 사진기를 꺼내야겠어요."),
            DayGreeting('V/Late Night/v-ln-2',
            "The wee hours of the night will keep our secrets.",
            "새벽은 우리의 비밀을 지켜주겠죠."),
            DayGreeting('V/Late Night/v-ln-3',
            "I want to take this to heart",
            "이 시간을 눈에 새기고 싶네요")],

    'y': [ DayGreeting('Yoosung/Late Night/y-ln-1',
            "Don't tell me···. u haven't slept because u were also playing LOLOL?",
            "설마..그 쪽도 롤롤 하느라 지금까지 안 잔 거예요?"),
            DayGreeting('Yoosung/Late Night/y-ln-2',
            "Don't stay up too late.",
            "늦게까지 무리하지 마세요!"),
            DayGreeting('Yoosung/Late Night/y-ln-3',
            "Did u look at the time? Time slipped by without me realizing",
            "지금 시계 봤어요? 어느새 이렇게 되었죠?")],

    'z': [ DayGreeting('Zen/Late Night/z-ln-1',
            "Hey there, it's time to go to sleep~",
            "거기 청년, 잘 시간이라구요?"),
            DayGreeting('Zen/Late Night/z-ln-2',
            "What's keeping you awake, honey? I'll take care of it.",
            "뭐가 우리 자기를 잠 못들게 하는 거야? 내가 해결해줄게"),
            DayGreeting('Zen/Late Night/z-ln-3',
            "I've always enjoyed the air in the middle of the night.",
            "난 새벽 공기가 참 좋더라.")] }

define morning_greeting = {
    'ja': [ DayGreeting('Jaehee/Morning/ja-m-1',
            "A brand new day has started",
            "새로운 하루가 시작되었네요"),
            DayGreeting('Jaehee/Morning/ja-m-2',
            "Did you have breakfast?",
            "아침 식사는 하셨나요?"),
            DayGreeting('Jaehee/Morning/ja-m-3',
            "I pray that I can get off work on the dot today.",
            "오늘은 칼퇴할 수 있길 소망합니다.")],

    'ju': [ DayGreeting('Jumin/Morning/ju-m-1',
            "Good morning",
            "좋은 아침"),
            DayGreeting('Jumin/Morning/ju-m-2',
            "Chef made breakfast··· would you care to join?",
            "셰프가 차려주는 아침...그대도 먹고 싶나?"),
            DayGreeting('Jumin/Morning/ju-m-3',
            "Elizabeth the 3rd, I'm heading to work.",
            "회사 다녀올게, 엘리자베스 3세")],

    's': [ DayGreeting('Seven/Morning/s-m-1',
            "Good Mooorning!",
            "굿모~~닝!"),
            DayGreeting('Seven/Morning/s-m-2',
            "I wonder what kind of events await us today? Thump Thump!",
            "오늘은 어떤 사건사고가 우릴 기다릴까요! 두근두근"),
            DayGreeting('Seven/Morning/s-m-3',
            "Guess what we chatted about last night~!",
            "밤 중에 우리가 무슨 이야기 했게~요!")],

    'u': [ DayGreeting('Unknown/Morning/u-m-1',
            "I'm excited for what kind of day today is going to be",
            "오늘은 또 어떤 일이 생길지 기대해"),
            DayGreeting('Unknown/Morning/u-m-2',
            "Shadows are created when the sun rises.",
            "태양이 뜨면 반드시 그림자도 생기는 법이지"),
            DayGreeting('Unknown/Morning/u-m-3',
            "I wonder how many more mornings like today will you have.",
            "오늘 같은 아침이 앞으로 며칠이나 더 있을까?")],

    'v': [ DayGreeting('V/Morning/v-m-1',
            "Wishing you a peaceful day.",
            "평온한 하루가 되길 바라요."),
            DayGreeting('V/Morning/v-m-2',
            "Awakening to the sounds of birds chirping.",
            "새의 지저귀는 소리가 날 깨워요"),
            DayGreeting('V/Morning/v-m-3',
            "Are you awake?",
            "일어났어요?")],

    'y': [ DayGreeting('Yoosung/Morning/y-m-1',
            "Did you sleep well?",
            "안녕히 주무셨어요?"),
            DayGreeting('Yoosung/Morning/y-m-2',
            "Come and chat with us! Pretty plz?",
            "얼른 우리랑 채팅해요! 빨리요~ 네?"),
            DayGreeting('Yoosung/Morning/y-m-3',
            "Cooking Breakfast: Success!",
            "아침밥 만들기 성공!")],

    'z': [ DayGreeting('Zen/Morning/z-m-1',
            "Did you sleep well?",
            "잘 잤어?"),
            DayGreeting('Zen/Morning/z-m-2',
            "My face even in the mornings···. so handsome.",
            "아침에도 내 얼굴은 크흐...잘생겼다 진짜!"),
            DayGreeting('Zen/Morning/z-m-3',
            "Waited all night for you to come in.",
            "네가 들어오기를 밤새 기다렸어.")] }

define afternoon_greeting = {
    'ja': [ DayGreeting('Jaehee/Afternoon/ja-a-1',
            "I think deciding what to have for lunch is the most difficult thing to do.",
            "직장인에게 가장 어려운 건 점심 메뉴 고르는 것 같아요."),
            DayGreeting('Jaehee/Afternoon/ja-a-2',
            "I'm quite anxious as Mr. Han seems to be planning another strange business project.",
            "이사님께서 또 이상한 사업을 계획하시는 것 같아 불안합니다."),
            DayGreeting('Jaehee/Afternoon/ja-a-3',
            "Don't you feel lonely all by yourself?",
            "혼자 계시느라 외롭진 않으신가요?")],

    'ju': [ DayGreeting('Jumin/Afternoon/ju-a-1',
            "A new business plan for cats have come to my mind.",
            "새로운 고양이 사업 아이디어가 떠올랐어."),
            DayGreeting('Jumin/Afternoon/ju-a-2',
            "I miss Elizabeth the 3rd.",
            "엘리자베스 3세가 보고 싶군."),
            DayGreeting('Jumin/Afternoon/ju-a-3',
            "I'm working right now.",
            "난 일하는 중이야.")],

    's': [ DayGreeting('Seven/Afternoon/s-a-1',
            "You've come to listen to my classy jokes, right?",
            "오, 내 하이개그 들으러 온 거죠?"),
            DayGreeting('Seven/Afternoon/s-a-2',
            "Gotcha, darn hacker!",
            "요 해커자식, 잡았다!"),
            DayGreeting('Seven/Afternoon/s-a-3',
            "[[Hack Alert] This app is currently being hacked. JK, did I scare you?",
            "지금 이 앱은 해킹되고 있습니다. 농담이에요, 놀랐어요?")],

    'u': [ DayGreeting('Unknown/Afternoon/u-a-1',
            "I just saw you smile. Haha.",
            "방금 네 웃는 모습 봤다 크크"),
            DayGreeting('Unknown/Afternoon/u-a-2',
            "Is it fun chatting in the chatroom?",
            "그 채팅방에서 이야기하면 즐겁나?"),
            DayGreeting('Unknown/Afternoon/u-a-3',
            "You'll become my eyes.",
            "너는 내 눈이 되는 거야")],

    'v': [ DayGreeting('V/Afternoon/v-a-1',
            "You should eat well.",
            "식사 잘 챙겨드세요"),
            DayGreeting('V/Afternoon/v-a-2',
            "If there is any inconvenience, do not hesitate to tell me.",
            "불편한 게 있다면 언제든 말해주세요."),
            DayGreeting('V/Afternoon/v-a-3',
            "I think the photo I just took turned up pretty well.",
            "방금 사진을 찍었는데 잘 나온 것 같아요.")],

    'y': [ DayGreeting('Yoosung/Afternoon/y-a-1',
            "I hope the cafeteria serves only the good stuff today!",
            "오늘 학식에 다 맛있는 거만 나오면 좋겠다!"),
            DayGreeting('Yoosung/Afternoon/y-a-2',
            "To go to class or to play LOLOL, that is the question.",
            "수업이냐 롤롤이냐 그것이 문제로다.."),
            DayGreeting('Yoosung/Afternoon/y-a-3',
            "I'm so curious about what u r doing right now!",
            "지금 뭐하고 있을까 궁금해요!")],

    'z': [ DayGreeting('Zen/Afternoon/z-a-1',
            "I hope you enjoyed your lunch.",
            "점심 맛있게 먹었어?"),
            DayGreeting('Zen/Afternoon/z-a-2',
            "Mm mm ah ah~ How does my voice sound, great right?",
            "음음 아아 내 목소리 어때, 끝내주지?"),
            DayGreeting('Zen/Afternoon/z-a-3',
            "I'm going to nail my afternoon practice.",
            "오후 연습도 완벽하게 해야지.")] }

define evening_greeting = {
    'ja': [ DayGreeting('Jaehee/Evening/ja-e-1',
            "I keep staring at my phone because I want to chat with you.",
            "담당자님과 이야기 하고 싶어서 휴대폰을 보게 되네요."),
            DayGreeting('Jaehee/Evening/ja-e-2',
            "Drinking coffee is making me focus well.",
            "커피를 마시니 집중이 잘 되네요."),
            DayGreeting('Jaehee/Evening/ja-e-3',
            "Do you like watching musicals? I will lend you Zen's performance DVD if you want.",
            "뮤지컬 좋아하시나요? 괜찮으다면 젠 씨 공연 DVD를 빌려드리죠")],

    'ju': [ DayGreeting('Jumin/Evening/ju-e-1',
            "You've waited quite long, haven't you, Elizabeth the 3rd?",
            "엘리자베스 3세, 오래 기다렸지."),
            DayGreeting('Jumin/Evening/ju-e-2',
            "Hope you enjoy your meal tonight as well.",
            "그대도 완벽한 저녁 식사를 하길."),
            DayGreeting('Jumin/Evening/ju-e-3',
            "I wanted to talk with you.",
            "그대와 이야기를 하고 싶었어.")],

    's': [ DayGreeting('Seven/Evening/s-e-1',
            "Taking ma baby out for a joy ride~~",
            "우리 베이비 타고 드라이브 중~"),
            DayGreeting('Seven/Evening/s-e-2',
            "I wanna play with both Elly and you!",
            "나도 엘리랑 님이랑 놀고 싶어요!"),
            DayGreeting('Seven/Evening/s-e-3',
            "Do you think it's possible to teach cats how to hack?",
            "고양이한테도 해킹을 가르칠 수 있을까요?")],

    'u': [ DayGreeting('Unknown/Evening/u-e-1',
            "Darkness shall fall soon.",
            "이제 곧 어둠이 찾아올 거야"),
            DayGreeting('Unknown/Evening/u-e-2',
            "I'm the \"nice person\" who will guide you.",
            "난 너를 안내할 아주 '착한 사람'이야."),
            DayGreeting('Unknown/Evening/u-e-3',
            "You shouldn't trust them too much.",
            "너무 그들을 믿지마.")],

    'v': [ DayGreeting('V/Evening/v-e-1',
            "Traveling soothes us.",
            "여행은 사람을 달래주죠"),
            DayGreeting('V/Evening/v-e-2',
            "Thank you for joining RFA.",
            "RFA에 들어와줘서 고마워요."),
            DayGreeting('V/Evening/v-e-3',
            "You want to see my photos?",
            "제 사진이 보고 싶다구요?")],

    'y': [ DayGreeting('Yoosung/Evening/y-e-1',
            "Gonna play LOLOL as soon as I finish this assignment!",
            "과제만 끝나면 바로 롤롤 켤 거예요!"),
            DayGreeting('Yoosung/Evening/y-e-2',
            "I was waiting for you to log on.",
            "그 쪽이 접속하길 기다리고 있었어요!"),
            DayGreeting('Yoosung/Evening/y-e-3',
            "Let's go shop for cooking ingredients!",
            "요리할 거 장보러 가요!")],

    'z': [ DayGreeting('Zen/Evening/z-e-1',
            "It would be great if I could just chug a can of beer.",
            "맥주 한 잔 하면 딱 좋겠다."),
            DayGreeting('Zen/Evening/z-e-2',
            "\"Goddess divine, I missed you.\" What do you think? Sounds okay?",
            "\"나의 여신님, 보고 싶었소.\" 대사 어때? 괜찮아?"),
            DayGreeting('Zen/Evening/z-e-3',
            "You want to hear me sing?",
            "내 노래가 듣고 싶어?")] }

define night_greeting = {
    'ja': [ DayGreeting('Jaehee/Night/ja-n-1',
            "Logging more hours for work is what's awaiting me.",
            "야근과 잔업이 절 기다리네요."),
            DayGreeting('Jaehee/Night/ja-n-2',
            "You should take it easy today.",
            "오늘 하루 수고하셨습니다."),
            DayGreeting('Jaehee/Night/ja-n-3',
            "Sweet dreams",
            "좋은 꿈 꾸세요")],

    'ju': [ DayGreeting('Jumin/Night/ju-n-1',
            "I want to wrap up today by talking to you.",
            "오늘 하루는 그대와 대화하면서 마무리 짓고 싶군."),
            DayGreeting('Jumin/Night/ju-n-2',
            "I can hear your voice well as it's night time.",
            "밤이 되니 그대 목소리가 더 잘 들리는군."),
            DayGreeting('Jumin/Night/ju-n-3',
            "Should I check the chatroom?",
            "채팅방에 들어가볼까?")],

    's': [ DayGreeting('Seven/Night/s-n-1',
            "Hurry and ride the train to dreamland!",
            "얼른 꿈나라 기차 탑승하세요!!"),
            DayGreeting('Seven/Night/s-n-2',
            "My time has come! The Lord of Darkness! Defender of Justice 707!",
            "이제 나의 시간이 왔도다! 밤의 지배자! 정의의 사도 707!"),
            DayGreeting('Seven/Night/s-n-3',
            "Honey Buddha Chips and PHD Pepper are the best as midnight snacks!",
            "야식은 뭐니뭐니해도 허니봤다 칩과 닭털페퍼죠!")],

    'u': [ DayGreeting('Unknown/Night/u-n-1',
            "I wonder what will happen if I went to see you.",
            "만약 내가 널 만나러 가면 어떻게 될까?"),
            DayGreeting('Unknown/Night/u-n-2',
            "If I visit you in your dreams, I won't be a ghost or villain, but an angel.",
            "내가 꿈에 나와도 그건 귀신이나 괴한이 아니야. 천사지."),
            DayGreeting('Unknown/Night/u-n-3',
            "BAMMMM! Hehehehehe. Did I surprise you?",
            "빵! 크크크 놀랐어?")],

    'v': [ DayGreeting('V/Night/v-n-1',
            "When the sun sets, countless emotions comes forth.",
            "태양이 사라지면 많은 감정들이 밀려와요."),
            DayGreeting('V/Night/v-n-2',
            "I guess you probably had dinner by now. You should always eat well.",
            "저녁은 드셨겠죠? 잘 챙겨 드셔야해요."),
            DayGreeting('V/Night/v-n-3',
            "Good Night.",
            "잘 자요.")],

    'y': [ DayGreeting('Yoosung/Night/y-n-1',
            "Yawn··· sleepy···",
            "하아암...졸려요..."),
            DayGreeting('Yoosung/Night/y-n-2',
            "Rank #2 Superman Yoosung is currently playing LOLOL!",
            "랭킹 2위 유성짱짱맨이 롤롤 접속중!"),
            DayGreeting('Yoosung/Night/y-n-3',
            "Wow! A meteor just fell from the sky!",
            "와! 방금 하늘에서 유성이 떨어졌어요!")],

    'z': [ DayGreeting('Zen/Night/z-n-1',
            "Can't sleep? Do you want me to sing a lullaby?",
            "잠이 안 와? 자장가 불러줄까?"),
            DayGreeting('Zen/Night/z-n-2',
            "This hour is the most important time of day for our skin.",
            "지금이 가장 피부에 중요한 시간이래"),
            DayGreeting('Zen/Night/z-n-3',
            "History is made during the night.",
            "위대한 역사는 밤에 만들어지는 법이지")] }
