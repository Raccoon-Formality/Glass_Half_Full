# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define e = Character("Eileen")


"""You are mad at the world and he's an eternal optimist. While on a business trip, you get stranded in the same hotel room (thanks to a hurricane) and the ensuing hilarious encounters convince you to join him in romance (and optimism)."""

default pos_name = "John"
default neg_name = "Steve"

define posi = Character("John", color="#e98537")
define neg = Character("Steve", color="#5ab552")
define hot_lady = Character("Hotel Employee", color="#ffa2ac")
define bell_emp = Character("Taco Bell Employee", color="#9a4d76")

default pos_species = "lion"
default neg_species = "capybara"

default preferences.text_cps = 40

###images###

image john normal = "sprites/john/john_normal.png"
image john blush = "sprites/john/john_blush.png"
image john normal flip = im.Flip("sprites/john/john_normal.png", horizontal="True")
image john blush flip = im.Flip("sprites/john/john_blush.png", horizontal="True")


image steve normal = im.Flip("sprites/steve/steve_normal.png", horizontal="True")
image steve sad = im.Flip("sprites/steve/steve_sad.png", horizontal="True")
image steve normal flip = "sprites/steve/steve_normal.png"
image steve sad flip = "sprites/steve/steve_sad.png"

image car background = "scenes/lexus.png"

image bg wet_highway = "scenes/wet_highway.jpg"
image bg gas_station = "scenes/gas_station.jpg"
image bg store = "scenes/store.jpg"
image bg hotel = "scenes/hotel.jpeg"
image bg lobby = "scenes/lobby.jpg"
image bg hotel_room = "scenes/hotel_room.jpg"
image bg taco_bell = "scenes/taco_bell.jpg"
image bg black = Solid("#000")


image white = Solid("#fff")
image black = Solid("#000")
image dark = Solid("#000000c7")
image darkish = Solid("#00000088")

label start:
    neg "Are you sure you know where you are going?"
    posi "Trust me, {w}I have no idea where I am going, but I put my full faith and trust into the GPS in my phone."
    "The [pos_species] says with a laugh and a smile."
    play music "audio/music/car_rain.wav" fadein 3.0 fadeout 1.0
    $ renpy.music.set_volume(0.6, channel="music")
    window hide
    pause 3
    centered "{size=100}Glass Half Full{/size}"
    pause 1
    centered "{size=56}created by: Raccoon Formality{p=1.0}\nproudly powered by: Renpy{/size}"
    pause 1
    centered "{size=100}Chapter 1: The Drive{/size}"
    pause 1
    window show
    scene bg wet_highway with Dissolve(1.0)
    show car background:
        linear 1.0 yalign 0.1
        linear 1.0 yalign 0.0
        repeat
    #TODO: play background sound and generic pop music
    "[pos_name] and [neg_name] are flying down the highway twords their destination."
    show john normal at left with Dissolve(1.0):
        yalign 0.0
        zoom 1.5
    posi "Hey, what's your favorite snack?"
    show steve normal flip at right with Dissolve(1.0):
        yalign 0.0

    neg "Uhhhh, Funyuns and Pepsi, why do you ask?"
    posi "I dunno, just wondering."
    neg "Uhhhh... {w}okay..."
    neg "Hey, what are we going to do at this place again?"
    posi "We are going to show this company the fantastic opportunities and capabilities our products have to serve for this company {w}and hopefully come out of it with a big commission check."
    neg "So... {w}a sales pitch?"
    posi "Yes, {w}a sales pitch."
    neg "You could've just said that, you know?"
    posi "And you could've just stayed at the office, but instead you decided to spend the day with me."
    neg "Come on, we both know I did this just for the commission."
    #TODO: show negative character at right
    neg "In this economy, I'll be lucky if I'm not living paycheck to paycheck."
    posi "..."
    "The [neg_species] sighs."
    neg "Okay, I guess I'd be lying if I didn't say that part of the reason I came was because I knew that spending the day with you would be much better than staying in the office and staring at a computer screen all day."
    "The [pos_species] smiles."
    #TODO: show negative character flip at right
    posi "Just try to loosen up a bit, {w}boss-man doesn't offer many opportunities to leave the office these days."
    neg "Ah yes, I was blessed with the opportunity to leave the office."
    "The [neg_species] says sarcastically."
    "The [pos_species] laughs again."
    neg "Plus it's an overnight so it's like more work than the usual amount of work."
    posi "Yeah, I suppose so, but it's more drawn out so it seems easier."
    neg "I guess that's true... {w}anyways... {w}do you think we can pull off the highway so I can use the restroom?"
    posi "Yeah, for sure, man. {w}I'm also getting pretty hungry, wanna also grab a bite to eat?"
    neg "Uhhhh... yeahhhh... {w}no..."
    posi "Huh? Why not?"
    #TODO: make next line of diolouge a lot faster than the rest
    neg "You remember when I said that money was tight? Well... {p=1.0}{cps=*2}I don't have the money to eat out anymore so I packed some ramen to cook while we are in our hotel room.{/cps}"
    posi "Hey, it's okay dude, don't worry."
    posi "I'll pay, it'll be my treat."
    neg "Oh, I can't let you do that."
    posi "I insist."
    neg "..."
    "The [neg_species] considers the proposition."
    posi "How about I write it off as a business expense and we call it even, deal?"
    neg "Alright... {w}deal."
    posi "Awesome!"
    #TODO: flip neg
    neg "I'm sorry, I'm just not used to people offering me things."
    posi "It's alright, you don't have to apologize, I get it."
    posi "My family got hit pretty hard during the last recession."
    neg "Oh dang, I'm sorry to hear that..."
    posi "It's whatever, water unter the bridge at this point, {w}my point is that I know what it's like. So like, if there is any way that I can help, I'm here for you, dude."
    neg "Oh... Well, thanks, [pos_name]. I really appreciate that."
    posi "Yeah, no problem."
    posi "Thank you for joining me for this, I really didn't wanna do it alone."
    neg "Yeah dude, no problem..."
    neg "Can I use the bathroom now?"
    posi "Oh, yeah, right."
    #TODO add turn signal noise
    "The [pos_species] exits the highway and pulls up to the closest convenience station" 

    ### day 2 ###
    scene bg gas_station
    show car background:
        yalign 0.0
    show john normal at left:
        yalign 0.0
        zoom 1.5
    show steve normal flip at right:
        yalign 0.0
    posi "Hey, I'm gonna top up on gas, you can go use the restroom while I do that."
    neg "Okay."
    "The [neg_species] gets out of the car and walks into the convenience station."
    scene bg store with Dissolve(1.0)
    play music "audio/music/rain.wav" fadein 1.0 fadeout 1.0
    $ renpy.music.set_volume(0.6, channel="music")
    show steve normal at center:
        xalign -0.5
        yalign 0.0
        ease 2.0 xalign 0.5
    neg "Okay, okay. Bathroom, bathroom, where is it?"
    #TODO: lightning strike
    show white
    hide white with Dissolve(1.0)
    play sound "audio/music/thunder.wav" fadein 1.0
    $ renpy.sound.set_volume(1.0, channel="sound")
    "Lightning strikes outside, flooding the store with a bright flash of light and a loud boom."
    neg "Jesus Christ!"
    show steve normal:
        ease 2.0 xalign 2.0
    "The [neg_species] rushes to the back of the store. Which is, conveniently, where the bathroom is."
    "..."
    #TODO: man walks in
    show john normal at center:
        zoom 1.5
        xalign -0.8
        yalign 0.0
        ease 2.0 xalign 0.5
    "[pos_name] walks into the store and buys Pepsi and Funyuns and walks back out."
    show john normal flip at center:
        zoom 1.5
        yalign 0.0
        ease 2.0 xalign -0.8
    "..."
    show steve normal flip:
        ease 2.0 xalign -0.8
    "The [neg_species] rushes back out shortly thereafter."
    #TODO: car background
    scene bg gas_station
    play music "audio/music/car_rain.wav" fadein 1.0 fadeout 1.0
    $ renpy.music.set_volume(0.6, channel="music")
    show car background:
        yalign 0.0
    show john normal at left:
        yalign 0.0
        zoom 1.5
    show steve normal flip at center:
        xalign 1.5
        yalign 0.0
        ease 1.0 xalign 1.0
    posi "Hey."
    neg "H-hey"
    posi "Hey. {w}Are you alright?"
    #day 2 take 2
    neg "Y-yeah, I'm just a bit afraid of-"
    show white
    hide white with Dissolve(1.0)
    play sound "audio/music/thunder2.wav" fadein 1.0
    $ renpy.sound.set_volume(1.0, channel="sound")
    show steve normal flip:
        yalign -0.1
        ease 1.0 xalign 0.8
    "Lightning strikes again with a loud boom and flash that lights up the whole area. The [neg_species] lunges forward and covers his head with his hands."
    show john normal:
        ease 1.0 xalign 0.1
    posi "Oh dude, it's alright..."
    "The [pos_species] thinks for a moment on how to comfort the [neg_species]."
    "Then, he gets an idea."
    posi "Hey, {w}how about you put on your headphones and take a nap for the rest of the ride?"
    neg "O-okay, yeah, that's a good idea."
    "The [neg_species] does what the [pos_species] had suggested and put on some lo-fi hiphop beats to relax to."
    scene bg wet_highway with Dissolve(1.0)
    show car background:
        linear 1.0 yalign 0.1
        linear 1.0 yalign 0.0
        repeat
    show john normal at left:
        yalign 0.0
        zoom 1.5
    show steve normal at right:
        yalign 0.0
    "The [pos_species] quietly makes his way back onto the highway."
    "The [pos_species] quickly realized that he had forgotten to get food, but he decided to worry about that later."

    #chapter 2: The Business Deal
    scene black with Dissolve(1.0)
    window hide
    pause 1
    centered "{size=100}Chapter 2: The Business Deal{/size}"
    pause 1
    window show
    posi "Alright, we're here."
    scene bg hotel with Dissolve(1.0)
    show car background:
        yalign 0.0
    show john normal at left:
        yalign 0.0
        zoom 1.5
    show steve normal flip at right:
        yalign 0.0
    "The [pos_species] nudges the [neg_species] to wake him up."
    neg "Huh? Where am I?"
    posi "At the hotel, silly."
    posi "I was thinking we could check in first and then go over to the business deal."
    neg "Oh... {w}okay."
    "The two of them walk into the hotel to get checked in."
    #TODO: show hotel background
    scene bg lobby with Dissolve(1.0)
    play music "audio/music/rain.wav" fadeout 1.0 fadein 1.0 
    $ renpy.music.set_volume(0.3, channel="music")
    show steve normal at center:
        xalign -0.5
        yalign 0.0
        ease 2.0 xalign 0.3
    show john normal at center:
        xalign -0.5
        yalign 0.0
        zoom 1.5
        ease 2.0 xalign 0.9
    posi "Good evening, ma'am, I am here to check me and my business associate in please."
    hot_lady "Yes, of course, I just need to see your ID to check you in our system"
    posi "Okie dokie"
    "The [pos_species] gives his ID card to the lady behind the counter and she scans it in."
    hot_lady "Fantastic, we have you down for one queen and your room number is 427."
    posi "Wait, hold on, one queen? That can't be right, there are two of us."
    neg "Did you remember to tell boss-man that I would be tagging along?"
    posi "..."
    neg "*sigh*"
    posi "Is there any way we can change rooms?"
    hot_lady "I am sorry, sir, but we are currently all booked up for the night."
    posi "Okay well... does the room have a couch?"
    hot_lady "Yes sir, it does."
    posi "Well okay, that'll work..."
    posi "Thank you"
    hot_lady "No problem! Have a great rest of your evening!"
    show steve normal flip:
        ease 2.0 xalign -0.8
    show john normal flip:
        ease 2.0 xalign -0.8
    "The two walk up to their room."
    #TODO: show hotel room background
    scene hotel_room
    show steve normal flip at center:
        xalign 1.5
        yalign 0.0
        ease 2.0 xalign 0.3
    show john normal flip at center:
        xalign 1.5
        yalign 0.0
        zoom 1.5
        ease 2.0 xalign 0.9
    posi "You can have the bed, queen. I'll sleep on the couch."
    show steve normal
    neg "Oh wow, thank you, that is mighty generous of you."
    posi "It's alright, it was kinda my fault to begin with haha."
    "The [pos_species] chuckles."
    "Just then, they both get an alert on their phones."
    "{b}ALERT: TORNADO WATCH CURRENTLY IN EFFECT IN...{/b}"
    show steve normal:
        yalign -0.1
    "The [neg_species] yelps."
    posi "Hey now, don't worry, it's just a watch. You only really need to worry if it is a warning."
    neg "O-okay."
    posi "We have about an hour to kill before we go to the business deal, what do you wanna do?"
    neg "Hmmm..."
    "The [neg_species] stomach grumbles."
    posi "Heh, I guess I've got my answer."
    neg "Yeah, heh."
    "They chuckle together."
    posi "Come on, [neg_name], let me get you some food."
    show john normal:
        ease 2.0 xalign 1.8
    show steve normal:
        ease 2.0 xalign 1.8
    "They both shuffle back out of the hotel room and back into the car."
    #TODO: show car background
    hide john
    hide steve
    show bg hotel with Dissolve(1.0)
    show car background:
        yalign 0.0
    show john normal at left:
        yalign 0.0
        zoom 1.5
        xalign -0.8
        ease 2.0 xalign 0.0
    show steve normal flip at right:
        yalign 0.0
        xalign 1.8
        ease 2.0 xalign 1.0
    play music "audio/music/car_rain.wav" fadein 3.0 fadeout 1.0
    $ renpy.music.set_volume(0.6, channel="music")
    posi "Does Taco Bell sound good to you?"
    neg "Absolutely, sounds great, thank you."
    show bg taco_bell with Dissolve(2.0)
    "The two drive over to the local Taco Bell."
    #TODO: show local taco bell background
    show john normal flip
    bell_emp "What can I get for you today?"
    posi "Can I get a Deluxe Cravings Box with a large Pepsi."
    neg "Make that two of those please!"
    "The [neg_species] awkwardly talks over the driver's seat and into the speaker box."
    bell_emp "Absolutely, that'll be $15.21 at the window."
    "They drive around to the window, pay, and get their food shortly thereafter."
    bell_emp "Have a nice day."
    posi "Thank you, you too."
    "At that moment, their phones go off again."
    "{b}ALERT: TORNADO WARNING CURRENTLY IN EFFECT IN...{/b}"
    show john normal
    neg "Oh shit..."
    posi "Okay, don't freak out, we will just go back to the hotel and stay away from the windows."
    "The [neg_species] starts to look anxious."
    show john normal:
        ease 1.0 xalign 0.1
    "The [pos_species] looks into the [neg_species]'s eyes and confidently says:"
    posi "It's all going to be okay, you don't have to worry."
    posi "I'll make sure you're safe, okay?"
    neg "O-okay, I trust you."
    show bg hotel with Dissolve(1.0)
    "With that, the [pos_species] quickly, but safely, drives the car back to the hotel."

    ###DAY 3###
    #TODO: show hotel room background
    hide bg
    play music "audio/music/rain.wav" fadeout 1.0 fadein 1.0 
    $ renpy.music.set_volume(0.3, channel="music")
    scene hotel_room
    show steve normal flip at center:
        xalign 1.5
        yalign 0.0
        ease 2.0 xalign 0.3
    show john normal flip at center:
        xalign 1.5
        yalign 0.0
        zoom 1.5
        ease 2.0 xalign 0.9
    "The two set down their food on the coffee table in the room and sit down on the couch together."
    posi "Okay, now just try to stay away from the windows and we should be just fine."
    show steve normal
    neg "But what about the business deal-"
    #TODO: show dark background
    show dark with Dissolve(0.1)
    "Before the [neg_species] can finish his thought, the power goes out and it goes dark." 
    show steve normal:
        ease 0.1 yalign -0.1
    "The [neg_species] yelps."
    posi "I think we're going to have to reschedule, heh."
    "The [pos_species] thinks for a moment."
    show john normal
    posi "I'm gonna go check out what's going on with the hotel staff."
    neg "C-can I come with? I'd rather not be alone in the dark, heh."
    posi "Yeah, sure."
    #show dark hallway
    show steve:
        ease 2.0 xalign 1.8
    show john:
        ease 2.0 xalign 1.8
    "The two of them start walking down the dark hallway to make their way down to the lobby." 
    hide john
    hide steve
    hide dark
    show bg black
    show john normal flip at center:
        xalign 1.5
        yalign 0.0
        zoom 1.5
        ease 2.0 xalign 0.3
    show steve normal flip at center:
        xalign 1.5
        yalign 0.0
        ease 2.0 xalign 0.8
    show dark
    "While walking down the hall, the [neg_species] stumbles."
    show steve normal flip with vpunch:
        ease 0.5 xalign 0.5 yalign -0.3
    show john normal with vpunch
    #SCREEN SHAKE
    "He grabs onto the [pos_species]'s arm to catch himself."
    posi "Oh shit, you alright, dude?"
    neg "Y-yeah, I'm okay... {w}can I hold onto your arm on the way down to the lobby? I can't see as well as you can."
    show john blush flip:
        ease 1.0 xalign 0.1
    "Unbeknownst to the [neg_species] because he cannot see, the [pos_species] blushes and turns away."
    posi "Y-yeah, for sure."
    show steve:
        ease 1.0 yalign 0.0
    neg "Thanks dude."
    show john normal flip:
        ease 2.0 xalign -0.8
    show steve:
        ease 2.0 xalign -0.8
    "The two make their way down the stairs and to the lobby. The [pos_species] using this time to compose himself."

    #Chapter 3: The Power Outage
    show bg black
    window hide
    pause 1
    centered "{size=100}Chapter 3: The Power Outage{/size}"
    pause 1
    window show
    "When the two make it to the lobby, there is already a group of around thirty to forty other people who were in the hotel trying to scout out the situation."
    "There are quite murmurs going around as to what to do and where to go."
    hot_lady "Attention valued hotel residence! Obviously, there has been a power outage and we're currently working to get the backup generator up and running!"
    hot_lady "We advise that you all go back to your rooms! As they will be a safer place to be in case of a flash flood!"
    hot_lady "Thank you for choosing Holiday Inn and we will have the power back on as soon as possible!"
    posi "Well, {w}back up the stairs we go, heh."
    neg "F-flash flood?"
    posi "Hey now, don't worry, remember when I said everything's going to be okay?"
    posi "I still mean that."
    posi "If we are in our hotel room, we should have nothing to worry about because it's almost impossible that flooding will get up to our floor, alright?"
    neg "A-alright."
    posi "Now, just hold onto my arm again and I will lead you back up to our room."
    "The [neg_species] does as he's told and they both make their way back up to their hotel room."
    #TODO: show hotel room dark
    show dark
    show bg hotel_room with Dissolve(2.0)
    show john normal flip at center:
        xalign 1.5
        yalign 0.0
        zoom 1.5
        ease 2.0 xalign 0.9
    show steve normal flip at center:
        xalign 1.5
        yalign 0.0
        ease 2.0 xalign 0.3
    neg "Well, fuck, what do we do now?"
    posi "Uhhh well, {w}eating the food we got would a good first step."
    "The [pos_species] chuckles."
    show steve normal
    neg "*sigh*"
    neg "O-okay, sounds good."
    "The two sit down on the couch and dig into their meals."
    "In-between eating, the [neg_species] strikes up a conversion."
    neg "How are you so calm about this situation?"
    posi "Well... {w}I grew up in the mid-west, this kind of thing happened all the time."
    neg "Ah, I see."
    neg "What was that like?"
    posi "Well, {w}there was a lot of corn haha."
    posi "It was fine, can't complain too much."
    neg "Why did you leave?"
    "The [pos_species] pauses for a moment, {w}contemplating his previous life."
    posi "It... {w}just wasn't a good fit..." 
    "The [neg_species] expects him to continue, but he doesn't."
    "[neg_name] considers asking further, but decides against it."
    neg "Do you like it here?"
    posi "Yeah, I'd say so."
    neg "That's good."
    posi "Yeah..."
    show john normal:
        ease 1.0 xalign 1.0
    "They both finish their food and throw their garbage away."
    show steve normal flip:
        ease 1.0 xalign 0.1
    "The [neg_species] stares out the window, the storm shows no sign of slowing down."
    neg "Damn..."
    neg "Damnit!"
    show john normal flip
    "The [pos_species] turns around in shock."
    show steve sad flip:
        ease 1.0 yalign -0.1
    "The [neg_species] starts to sob on the couch."
    neg "Fuck dude, like, what are we gonna do?"
    posi "What, about the tornado? Wait for it to pass."
    posi "I mean, that's pretty much all we can do-"
    "The [neg_species] cuts him off."
    show steve sad
    neg "N-no, I mean about the business deal."
    posi "uhhh postpone or maybe cancel, I really don't know, I guess that's for bossman and that company to decide."
    show steve sad flip:
        ease 1.0 yalign -0.2
    "The [neg_species] turns away and continues to sob."
    neg "Damn dude, I could've really used that commission money, I'm gonna be stuck living off of ramen for weeks."
    neg "I am such a fuckin failure, dude."
    show john:
        ease 1.0 xalign 0.35 yalign -0.05
    "The [pos_species] slides closer to the [neg_species] and begins rubbing his back."
    posi "Hey now, don't talk to yourself like that."
    posi "I'm sure it's not that bad-"
    "The [neg_species] cuts him off again."
    show steve sad
    neg "It's pretty bad."
    posi "Well... {w}just because you are going through some financial hardships or lose a business deal, doesn't mean that you are a failure."
    posi "Especially in this situation, it wasn't at all your fault that we couldn't go make this deal, there's a tornado going on."
    "The [pos_species] chuckles a bit."
    neg "Y-yeah... {w}I suppose you're right."
    posi "How about we find something to do to get your mind off of things for a while, hey?"
    neg "I-i don't know if I'm feeling up to that right now-"
    #TODO: lighting
    show white
    hide white with Dissolve(1.0)
    play sound "audio/music/thunder.wav" fadein 1.0
    $ renpy.sound.set_volume(1.0, channel="sound")
    show steve:
        ease 1.0 xalign 0.15 yalign -0.25
    "Lighting strikes, filling the whole room with a flash, followed shortly thereafter by a loud boom of thunder."
    "The [neg_species] lunges into the [pos_species] arms and holds onto him tight."
    "The [pos_species] pauses for a moment before wrapping his arms around the [neg_species]."
    "The [pos_species] pets and rubs the [neg_species]'s back trying to comfort him."
    "The [neg_species] whimpers and continues to cry."
    posi "There there, it's allll gonna be okay."
    "The [pos_species] says while continuing to pet and comfort the [neg_species]."
    posi "Deep breaths, big guy, deep breaths. It's gonna be okay."
    "The [neg_species] breaths as deeply as he can muster."
    posi "Good boy, that's it, you're doing great~"
    "They stay like this for a while as the [neg_species] continues sob into the [pos_species] chest."
    posi "That's it, let it all out, big guy~"
    "After a good while, the [neg_species] starts to settle down and takes his face out of the [pos_species]'s chest."
    neg "Th-thank you..."
    posi "It's no problem, dude."
    neg "I'm s-sorry you had to see that, I j-just really let m-my anxiety get the b-best of me s-sometimes..."
    posi "It's completely fine dude, I understand, seriously."
    neg "Y-yeah, {w}c-can we do something else now?"
    posi "Absolutely, dude."
    "The [pos_species] says in a calm and caring voice."

    ### day 3 ###
    show john normal:
        ease 2.0 xalign 0.9 yalign 0.0
    "The [pos_species] gets up and walks over to his bag."
    posi "I've got a portable DVD player, would you like to watch a movie with me?"
    neg "Y-yes please..."
    neg "W-what movies do you have?"
    "The [pos_species] takes out a small booklet of DVDs."
    show john normal flip
    posi "Uhhh... {w}It's mainly Studio Ghibli, is that alright with you?"
    show steve normal:
        ease 1.0 yalign 0.0
    neg "I-i fucking love Studio Ghibli!"
    posi "Oh! Alrighty then"
    neg "Do you have Ponyo?"
    show john:
        ease 1.0 xalign 0.8 yalign 0.0
    posi "Of course I have Ponyo"
    neg "Yayyyyy"
    show john normal
    "The [pos_species] sets up his portable DVD player on the bed with Ponyo ready to play."
    posi "Alright, big guy"
    show john normal flip:
        ease 1.0 xalign 0.35 yalign -0.05
    posi "Here, let me help you into bed."
    show steve normal:
        ease 1.0 xalign 0.5
    show john:
        ease 1.0 xalign 0.75 yalign 0.0
    "The [pos_species] leads the [neg_species] into bed."
    show john:
        ease 1.0 xalign 0.7 yalign 0.0
    show steve normal flip
    "He tucks the [neg_species] into bed and sets him up to watch the movie."
    show john normal:
        ease 1.0 xalign 1.0 yalign 0.0
    "He starts to walk over to the couch and lay down."
    show steve normal
    show john normal flip
    neg "H-hey, wanna watch this with me?"
    show john blush flip
    "The [pos_species] blushes."
    show john:
        ease 1.0 xalign 0.9 yalign 0.0
    posi "I'd love to~"
    show steve normal flip
    show john:
        ease 1.0 xalign 0.7 yalign 0.0
    "The [pos_species] walks over to the bed and big spoons the [neg_species]."  
    show john blush
    posi "Oh hey, I almost forgot"
    show john blush flip
    "The [pos_species] reaches into his bag and pulls out the Pepsi and Funyuns and hands it to the [neg_species]."
    neg "omg... {w}you remembered~"
    posi "Of course I did~"
    "The [pos_species] pets the [neg_species] gently."
    "The two watch the movie together until they both eventually drift off into a deep slumber."
    scene black with Dissolve(3.0)
    window hide
    pause 1
    centered "{size=100}The End{/size}"
    pause 1
    centered "{size=56}Thank you for reading and have great rest of your day.{/size}"
    window show

    return


