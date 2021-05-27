import random

ts_lyrics = """
When you think Tim McGraw, I hope you think of me.
You're just another picture to burn.
He's the reason for the teardrops on my guitar.
Oh I'm just a girl trying to find a place in this world.
I've never been anywhere cold as you.
I've never been on the outside.
You're tied together with a smile but you're coming undone.
Stay beautiful.
You should've said no, should've gone home.
Take me back to the house in the backyard trees.
Our song is a slamming screen door.
And I'm only me when I'm with you.
We could be a beautiful miracle, instead of just invisible.
Why would you wanna break a perfectly good heart?

I'd dance in a storm in my best dress, fearless.
But I didn't know it at fifteen.
It's a love story, baby just say 'yes'.
Hey Stephen.
It's too late for you and your white horse.
Why can't you see, you belong with me.
I can't breathe without you, but I have to.
I know that you see what you're doing to me, tell me why.
You're not sorry, no.
That's the way I loved you.
Flashback to when he said 'forever and always'.
I know I had the best day with you today.
These things will change, can feel it now.
'Cause I'mma stay through it all, so jump then fall.
Untouchable, burning brighter than the sun.
I'm right here hoping you'll come in with the rain.
Gimme a photograph to hang on my wall, superstar.
I know all I need is on the other side of the door.
Today was a fairytale, you were the prince.
I've still got you all over me.
Hello, Mr Perfectly Fine.
And we were happy.
That's when, when I wake up in the morning.
Don't you smile at me and ask me how I've been.
Bye bye baby.

You are the best thing that's ever been mine.
I see sparks fly whenever you smile.
I go back to December all the time.
Speak now or forever hold your peace.
Dear John, I see it all now that you're gone.
Why you gotta be so mean?
The story of us looks a lot like a tragedy now.
Please try to never grow up.
I was enchanted to meet you.
There is nothing I do better than revenge.
You're still an innocent.
Can't go back now I'm haunted.
Never thought we'd have our last kiss.
Long live the walls we crashed through.
This love is ours.
Come back to like you would if this was a movie.
I watched Superman fly away.

This is a state of grace.
Loving him was red.
This slope is treacherous.
I knew you were trouble when you walked in.
I remember it all too well.
I dunno about you, but I'm feeling 22.
Everytime I don't, I almost do.
We are never ever ever getting back together.
Stay stay stay.
This is the last time I'm asking you this.
Right there where we stood was holy ground.
What a sad, beautiful, tragic love affair.
Let me tell you now you're the lucky one.
Everything has changed.
We were dancing like we're made of starlight.
I watched it begin again.
And that was the moment I knew.
Come back... be here.
Don't look at me, you've got a girl at home.

Welcome to New York - it's been waiting for you!
But I've got a blank space, baby.
We never go out of style.
Are we out of the woods yet?
All you had to do was stay.
I shake it off.
I wish you would come back.
Now we've got bad blood.
In your wildest dreams.
It's how you get the girl.
This love is good, this love is bad.
I know place we can hide.
I think I am finally clean.
We've found Wonderland; you and I got lost in it.
You are in love, true love.
Baby we're the New Romantics.

Are you ready for it?
I wanna be your end game.
I did something bad, so why's it feel so good?
Don't blame me, love made me crazy.
'Cause I know that it's delicate.
Ooh, look what you made me do.
So it goes...
You're so gorgeous.
We were riding, in a getaway car.
King of my heart, body and soul.
Dancing with our hands tied.
Flashback when you met me.
This is why we can't have nice things.
Call it what you want.
I'll be cleaning up bottles with you on New Year's Day.

I forgot that you existed.
It's a cruel summer with you.
You're my, my, my, my lover.
If I was a man, then I'd be The Man.
I've been the archer, I've been the prey.
Ain't gonna tell him, I think he knows.
Miss Americana and the Heartbreak Prince.
I'd marry you with paper rings.
I'd never walk Cornelia Street again.
Saying goodbye is death by a thousand cuts.
You know I love a London boy.
Soon you'll get better.
Still I worship this love, even if it's a false god.
You need to calm down.
Meet me in the afterglow.
I'm the only one of me.
It's nice to have a friend.
It's golden, like daylight.

It would've been fun if you would've been the 1.
I felt like I was an old cardigan under someone's bed.
There goes the last great American dynasty.
You were my crown, now I'm in exile seeing you out.
Look at how my tears ricochet.
I'm a mirrorball.
I hit my peak at seven feet in the swing.
August slipped away into a moment in time.
I just wanted you to know that this is me trying.
That's the thing about illicit affairs.
Some invisible string tying you to me.
No one likes a mad woman.
But you dream of some epiphany.
Betty, won't make assumptions.
Would it be enough if I can never give you peace?
Your faithless love's the only hoax I believe in.
Take me to the lakes where all the poets went to die.

Life was a willow and it bent right to your wind.
You won't remember all my champagne problems.
I don't like a gold rush.
'Tis the damn season, write this down.
You tolerate it.
No, no body no crime.
Leave it all behind, and there is happiness.
Hey dorothea, do you ever stop to think about me?
I'm sitting on a bench in Coney Island.
Your ivy grows, now I'm covered in you.
You're a cowboy like me.
Long story short, I survived.
Watched as you signed your name marjorie.
I don't need your closure.
This pain would be for evermore.

I remember your bare feet down the hallway.
This life is sweeter than fiction.
Keep your eyes open.
You and I'll be safe and sound.
You make me crazier, crazier, crazier.

"""

ts_lyrics = ts_lyrics.split("\n")
random_lyric = ts_lyrics[random.randint(0, len(ts_lyrics))]