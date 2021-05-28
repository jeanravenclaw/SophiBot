import random

ts_lyrics = \
"""
But when you think Tim McGraw, I hope you think my favorite song. the one we danced to all night long
The moon like a spotlight on the lake
When you think happiness, I hope you think that little black dress
Think of my head on your chest and my old faded blue jeans
When you think Tim McGraw, I hope you think of me
""" + \
"""
I hate that stupid old pickup truck you never let me drive
You're a redneck heartbreak who's really bad at lying
So watch me strike a match on all my wasted time
As far as I'm concerned, you're just another picture to burn""" +\
"""
He's the reason for the teardrops on my guitar
The only thing that keeps me wishing on a wishing star
He's the song in the car I keep singing, don't know why I do""" +\
"""
I'm alone, on my own, and that's all I know
I'll be strong, I'll be wrong, oh, but life goes on
Oh, I'm just a girl trying to find a place in this world""" +\
"""
Oh, what a shame, what a rainy ending given to a perfect day
Just walk away, ain't no use defending words that you will never say
And now that I'm sittin' here thinkin' it through, I've never been anywhere cold as you""" +\
"""
So, how can I ever try to be better? Nobody ever let's me in
And I can still see you, this ain't the best view on the outside looking in
I've been a lot of lonely places. I've never been on the outside""" +\
"""
Hold on, baby; you're losing it
The water's high, you're jumping into it, and letting go. and no one knows 
That you cry; but you don't tell anyone, that you might not be the golden one
And you're tied together with a smile, but you're coming undone""" +\
"""
You're beautiful, every little piece, love
Don't you know? You're really gonna be someone, ask anyone
And when you find everything you've looked for, I hope your love leads you back to my door
Oh, but if it don't, stay beautiful""" +\
"""
You should've said, 'No', you should've gone home
You should've thought twice 'fore you let it all go
You should've known that word 'bout what you did with her
Get back to me (get back to me)
And I should've been there. in the back of your mind
I shouldn't be asking myself, 'Why?''
You shouldn't be beggin' for forgiveness at my feet
You should've said, 'No', baby, and you might still have me""" +\
"""
Take me back to the house in the backyard tree
Said you'd beat me up, you were bigger than me, you never did, you never did
Take me back when our world was one block wide
I dared you to kiss me and ran when you tried
Just two kids, you and I
Oh my my my my""" +\
"""
Our song is the slamming screen door
Sneakin' out late, tapping on your window
When we're on the phone and you talk real slow 'cause it's late and your mama don't know
Our song is the way you laugh
The first date; 'Man, I didn't kiss her, and I should have'
And when I got home, 'fore I said 'Amen', asking God if he could play it again""" +\
"""
I'm only up when you're not down
Don't wanna fly if you're still on the ground, it's like no matter what I do
Well, you drive me crazy half the time
The other half I'm only trying to let you know that what I feel is true
And I'm only me when I'm with you""" +\
"""
And I just wanna show you, she don't even know you
She's never gonna love you like I want to
And you just see right through me but if you only knew me
We could be a beautiful, miracle, unbelievable, instead of just invisible""" +\
"""
Why would you wanna break a perfectly good heart
Why would you wanna take our love and tear it all apart now
Why would you wanna make the very first scar
Why would you wanna break a perfectly good heart"""

ts_lyrics = ts_lyrics.split("\n")

def random_lyric():
	return ts_lyrics[random.randint(0, len(ts_lyrics))]