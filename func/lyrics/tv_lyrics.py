import random

ts_lyrics = \
"""And I don't know how it gets better than this
You take my hand and drag me head first, Fearless
And I don't know why, but with you I'd dance 
In a storm in my best dress, Fearless""" + \
"""'
Cause when you're fifteen and somebody tells you they love you, you're gonna believe them
And when you're fifteen feeling like there's nothing to figure out
Count to ten, take it in
This is life before you know who you're gonna be at fifteen""" + \
"""
Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story, baby, just say, 'Yes' """ + \
"""
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain, so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmh, I can't help myself""" + \
"""
I'm not a princess, this ain't a fairy tale
I'm not the one you'll sweep off her feet. lead her up the stairwell
This ain't Hollywood, this is a small town
I was a dreamer before you went and let me down
Now it's too late for you and your white horse to come around""" + \
"""
If you could see that I'm the one who understands you, been here all along, so why can't you see?
You belong with me""" + \
"""
And I can't breathe without you, but I have to
Breathe without you, but I have to""" + \
"""
I'm sick and tired of your attitude
I'm feeling like I don't know you
You tell me that you love me, then you cut me down
And I need you like a heartbeat
But you know you got a mean streak
Makes me run for cover when you're around
Here's to you and your temper
Yes, I remember what you said last night
And I know that you see what you're doing to me
Tell me why""" + \
"""
You don't have to call anymore, I won't pick up the phone
This is the last straw, don't wanna hurt anymore
And you can tell me that you're sorry
But I don't believe you baby like I did before
You're not sorry, no no, no no""" + \
"""
But I miss screaming and fighting and kissing in the rain
And it's 2:00 a.m. and I'm cursing your name
So in love that you act insane
And that's the way I loved you
Breakin' down and coming undone
It's a roller coaster kinda rush
And I never knew I could feel that much
And that's the way I loved you""" + \
"""
And I stare at the phone, he still hasn't called
And then you feel so low you cant feel nothing at all
And you flashback to when he said, 'Forever and always'
Oh, and it rains in your bedroom, everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said, 'Forever and always' """ + \
"""
I'll leave my window open 'cause I'm too tired tonight to call your name
Just know I'm right here hoping that you'll come in with the rain""" + \
"""
So dim that spotlight
Tell me things like 'I can't take my eyes off of you'
I'm no one special, just another wide-eyed girl who's desperately in love with you
Give me a photograph to hang on my wall, superstar""" + \
"""
I said, 'Leave', but all I really want is you to stand outside my window, throwin' pebbles
Screamin', 'I'm in love with you'
Wait there in the pourin' rain, comin' back for more
And don't you leave, 'cause I know all I need is on the other side of the door""" + \
"""
Can you feel this magic in the air?
It must have been the way you kissed me
Fell in love when I saw you standing there
It must have been the way today was a fairytale
It must have been the way today was a fairytale""" + \
"""
I lived, and I learned
Had you, got burned
Held out, and held on
God knows, too long
And wasted time, lost tears
Swore that I'd get out of here
But no amount of freedom gets you clean
I've still got you all over me""" + \
"""
Hello Mr. Perfectly Fine
How's your heart after breaking mine?
Mr. Always At The Right Place At The Right Time, baby
Hello Mr. Casually Cruel
Mr. Everything Revolves Around You
I've been Miss Misery since your goodbye
And you're Mr. Perfectly Fine """ + \
"""
When it was good, baby, it was good, baby
We showed 'em all up
No one could touch the way we laughed in the dark
Talkin' 'bout your daddy's farm we were gonna buy someday
And we were happy""" + \
"""
And you said, that's when, when I wake up in the mornin'
That's when, when it's sunny or stormin'
Laughin' when I'm cryin'
And that's when I'll be waitin' at the front gate
That's when, when I see your face
I'll let you in, and baby that's when""" + \
"""
But don't you
Don't you smile at me and ask me how I've been
Don't you say you've missed me if you don't want me again
You don't know how much I feel I love you still
So why don't you, don't you?""" + \
"""
Bye, bye, to everything I thought was on my side
Bye, bye, baby
I want you bad but it's come down to nothing
And all I have is your sympathy
'Cause you took me home but you just couldn't keep me
Bye, bye, baby
Bye, bye, baby"""

ts_lyrics = ts_lyrics.split("\n")

def random_lyric():
    """
    Returns a random lyric.
    """
    return ts_lyrics[random.randint(0, len(ts_lyrics))]