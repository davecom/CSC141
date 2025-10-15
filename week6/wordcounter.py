article = """
'Puerto Rican pop star Bad Bunny has confirmed will headline next year's Super Bowl half-time show in Santa Clara, California.

The 31-year-old, who has topped Spotify's most-streamed artist list three times in the last five years, said in a football-themed statement: "What I'm feeling goes beyond myself.

Full Mouth Restoration In Just 24HRS
Ad
Full Mouth Restoration In Just 24HRS
Nuvia
call to action icon
more
"It's for those who came before me and ran countless yards so I could come in and score a touchdown... this is for my people, my culture, and our history."

It comes after the Chambea singer and rapper recently said in an interview with i-D magazine that he is avoiding the US on his current world tour out of concerns that Immigration and Customs Enforcement (ICE) agents might conduct raids on fans at his concerts.

Switching into his native Spanish, Bad Bunny - whose real name is Benito Antonio Martinez Ocasio - added in his statement: "Ve y dile a tu abuela, que seremos el halftime show del Super Bowl," - which roughly translates as: "Go tell your grandma we're going to be the Super Bowl half-time show."

The star, who this year released the album Debí Tirar Más Fotos (I Should Have Taken More Photos), was the third most-streamed artist in the world last year, behind Taylor Swift and The Weeknd.

Only $39 To Get All TV Channels?
Ad
Only $39 To Get All TV Channels?
Trends & Finds
call to action icon
more
The Grammy winner is the leading nominee once again at November's Latin Grammy Awards.

In 2022, his Un Verano Sin Ti [A Summer Without You], became the first all-Spanish language US number one album.

Earlier this month, he concluded a residency in his native Puerto Rico instead, which drew more than 500,000 fans.

Puerto Rico is a US territory but which exercises substantial internal self-govenance.

His Super Bowl performance will take place at the Levi's Stadium on 8 February in Santa Clara, in the San Francisco Bay Area.

Other recent Super Bowl half-time show performers have included Kendrick Lamar, The Weeknd and Rihanna, as well as Shakira and Jennifer Lopez.'
"""
counter = {}
words = article.split(" ")
print(len(words))
for original_word in words:
    word = original_word.lower().strip()
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)
print(len(counter))