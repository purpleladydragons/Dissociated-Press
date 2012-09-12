# -*- coding: utf-8 -*-
import random


def dissociate(originale,new,chunks,chunksize):
    if len(new.split()) >= chunks * chunksize:
        return new

    original = originale.replace(".","").replace(",","").split()
    occurs = []

    if new != "":
        occurs = teststring(new.split()[len(new.split())-chunksize:],original)

    if new == "" or len(occurs) < 2: 
        appendablestart = random.randint(0,len(original)-chunksize)
        appendableend = appendablestart + chunksize
        appendable = [word for word in original[appendablestart:appendableend]] #OB1?
        for word in appendable:
            new += word+" "

    else:
        occurrences = teststring(new.split()[len(new.split())-chunksize:],original)
        choice = random.choice(occurrences)
        appendables = original[choice+chunksize:choice+chunksize+chunksize]
        for word in appendables:
            new += word+" " 





    return dissociate(originale,new,chunks,chunksize)


def teststring(phrase,original):
    choices = []
    if len(phrase) == 1:
        return [i for i, x in enumerate(original) if x == phrase[0]]
    else:
        possibles = [i for i, x in enumerate(original[:len(original)-len(phrase)]) if x == phrase[0]]
        for possible in possibles:
            valid = True
            for x in range(len(phrase)):
                if phrase[x] != original[possible+x]:
                    valid = False
            
            if valid:
                choices.append(possible)
                
        return choices

def main():
    orig = """LONDON – Somewhere in the midst of their relaxing afternoon stroll to the gold medal, Team USA looked up and found themselves in a fight. Spain rained 3-pointers over the Americans' heads. Pau and Marc Gasol bullied the U.S. frontline. And after U.S. center Tyson Chandler became entangled with Sergio Rodriguez in the second quarter, the little Spanish point guard stepped up and jabbed his right index finger into Chandler's face.
    Rodriguez's message was clear: For all your NBA talent, for all your American dominance, you will not push us around.
    Yes, Team USA's gold-medal rematch with Spain proved nearly as difficult as their battle in Beijing four years ago. Just like in 2008, the Americans finally separated themselves from Spain in the closing minutes of the fourth quarter, holding on for a 107-100 victory that gave them their second straight Olympic gold medal.
    [ Photos: Team USA fights off Spain for gold ]
    Mike Krzyzewski coached his final game for Team USA, joining Henry Iba as the only men to guide the U.S. to consecutive golds. He'll stay involved with USA Basketball but has no plans to continue coaching the national team. Krzyzewski helped USA Basketball managing director Jerry Colangelo rebuild the national team after the U.S. finished sixth at the 2002 world championships and won only bronze at the 2004 Athens Games. As Sunday's game ended, LeBron James showered his coach with
    water.
    Krzyzewski and Colangelo reshaped the national team program by getting a core group of NBA stars to commit to playing – and staying – together. This too, might have been the final game for several of them. James isn't sure he'll play in the 2016 Games in Rio. Kobe Bryant declared Sunday his last appearance in the red, white and blue.
    "This is it for me," Bryant said after scoring 17 points in the victory. "The other guys are good to go."
    Kevin Durant showed throughout the tournament he's more than capable of taking ownership of Team USA if he wants. Durant wasn't on the U.S. roster in 2008, but has since become one of the NBA's biggest stars. He played like one against Spain, totaling 30 points and nine rebounds. Durant's Oklahoma City Thunder lost the NBA Finals to the Miami Heat, but he leaves the summer with his first Olympic gold medal.
    "I'm going to look back and remember how fun it was for all of us to be around each other," Durant said. "I'm excited to cap it off with a gold medal."
    James had 19 points and seven rebounds and hit a late 3-pointer to finish off Spain. He only strengthened his reputation as the game's greatest player during these Olympics. He now joins Michael Jordan as the only players to win the NBA regular-season MVP, NBA Finals MVP, NBA title and Olympic title in the same year.
    "It was a great ride for me," James said. "I could have never scripted it any better."
    [ Related: Team USA delivers Olympic spirit, not tanking and groin shots ]
    From Las Vegas to London, Team USA had rolled through its competition. Only Lithuania gave the U.S. anything close to resembling a scare before the gold-medal game. Spain, though, was different, and the Americans had only to remember back four years to know this.
    Team USA coasted past Spain in an exhibition in Barcelona shortly before the start of these Olympics, but neither team considered it to be a true barometer of Spain's competitiveness should the teams meet in London. Even after Spain blew a large fourth-quarter lead against Brazil in pool play, opposing teams suggested the Spaniards had pulled back to avoid facing the U.S. before the gold-medal game. Everyone here knew the obvious: The only team that had any chance of beating Team USA
    was Spain. From the size of the Gasol brothers and Serge Ibaka to its many shooters, Spain had a formidable roster. 
    Celebrities in attendance. (ITSLUDACRIS via Instagram)
    And for much of the first 3½ quarters, Spain gave the U.S. a fight. Juan Carlos Navarro scored 19 points in the half while making all three of his 3-pointers. Even after Marc Gasol exited with his fourth foul midway through the second quarter, Spain clung to the U.S. When Pau Gasol threw down a dunk early in the third quarter, the Americans trailed by a point.
    From the opening minutes, Spain made clear it wasn't going to just concede the gold to the U.S. Navarro's shooting buoyed Spain, which also played the Americans physically. Rudy Fernandez wrestled Chandler to the floor. Durant streaked to the basket for a layup attempt only to be flung to the court hard by Jose Calderon. Pau (24) and Marc Gasol (17) also took advantage of their size inside to combine for 41 points.
    In the end, though, Spain wasn't helped by a couple of curious decisions by its coach, Sergio Scariolo. Scariolo left Marc Gasol on the floor too long after his third foul in the first half. And with Marc Gasol then saddled with four fouls at halftime, Scariolo didn't play him at all in the third quarter. Pau Gasol also said Spain's defensive breakdowns in the final minutes could be attributed to the team going to a scheme it had not practiced.
    "We were close at times, but we couldn't play the perfect game we needed to beat them," Pau Gasol said.
    The Americans never panicked. Time and again in the tournament, they'd overwhelmed their opponents in the second half. Their talent, their depth couldn't be matched. They took Spain's best punch and brushed it off.
    As the crowd at North Greenwich Arena chanted "U-S-A! U-S-A!" Sunday evening, Bryant, James and the rest of their teammates waved and acknowledged the cheers. They finished these Olympics standing in the same position they stood four years ago in Beijing. On the podium's top step, gold medals draped around their necks."""

    print dissociate(orig,"",50,1)
        
if __name__ == "__main__":
    main()