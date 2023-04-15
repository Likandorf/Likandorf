print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

part1 = input("In this island you are inside of a jungle looking for the famous treasure, you come across a ruin with the same markings as the one in your map. you try to open the stone door but its shut tight, next thing you know you start hearing noises coming from behind you. What will you do?\n\n1-Force open the door with your sword\n2-Hide yourself in the nearby bushes\n3-Ready your weapon and charge at the noise\n")

if part1 == "1":
  print("""   _________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                                         -_- _-   -| \   
  |                            _-  _--                      | 
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |          
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |  
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \
/   -_- _ -             _- _---                       -_-  -_ \
""")
  part2 = input("As you are trying to force the door to open you notice an opening on the side of the stone slab door and you decide to jab your sword while you push with all your might. The slab moves and makes enough space for you fit in through. You make it to the other side and the door shuts with great force. Your sword breaks, you are unarmed and you decide to take a breather as you hear wierd noises on the other side of the door. There are two paths ahead of you. Which path will you choose?\n\n1-Right\n2-Left\n")
  
  if part2 == "1":
    print("""
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888(FL)888""")
    part3 = input("You chose Right and you continued until you reached a wall with 2 buttons with diferent colors. Which will you press?\n\n1-Blue\n2-Red\n")
    
    if part3 == "2":
      print(""""  
  \ \_\ .----------.     /
   \   (  ||    ||  )   /..
|\  \   ~-||====||-~_  ///\\
| \  \    ||    || // /((()))
 \|  |    ||====|| ~ / \\\///
     |__  ||    ||   |  `|''
     | |\ ||====|| __|  _|_
     | | \`'    `'/| |  =O=
     | | |_ `    / | |   ~
     | | ||\____|  | |_
 _   | | || ____|  | |_]
| |  | | |l/::::|  | |
|/   | | |::::::\  | |
     | | /:::::::\ | |
     |_|/:::::::::\|_|
  /|/|:.:.:.:.:.:.:.:|
 | / |.:.:.:.:.:.:.:.|
 |/| /...............\ |\
   |/.................\ \|
   /. . . . . . . . . .\
  /. . . . . . . . . . .\"""")
      part4 = input("You decided to press the Red button and it opened a passage way. Now you can barely see the treasure on the other side of this room. You notice some ropes that you can use to swing by with but the fall the fall would be fatal, there is also a great pool of water that you can use to swim across to the teasure. There is also one more path crawling with creatures, confrontation is innevitable in this path and you are unarmed. What will you do?\n\n1-Swing\n2-Swim\n3-Confront\n")
      
      if part4 == "2":
        print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
        you_won = print("You decide to swim across, as you start swimming you feel as if something was behind you so you start swiming at full speed. You made it to the other side and you look back and nothing was there. Must have been your imagination, now you have made it to the treasure.\n\nYOU WON!")
        
      elif part4 == "1":
        print("""                           ,---._
                                         ,~~,-._  `._
                                          v'~   `-.  `.
                                               _,- ~.  \
                                             .'  ,--`.  `\_
                                             V-'~ ,'~~~`-. `-.
                                 ___             /_/~~~) ` `. `._
                        ____,---'   ;            V     `.__ `--, `;
                         `-._    ;  `.                ____)       :
                             `.;  ; .'              ,'        _    |
                              ; |   ;              ,';'~~~`--' `;  :
                             ,': .-'               `,'  __ __   :  |
                             )_  `-, ___     __        (__:__)   ; ;
                        _,---. \___,'` ~`---;  `-.       |||    ;  ;
                    _,-/   :;     !   `     `|    `-.   |~~~~|   ; :
                _,-' /~   .,'  ;  !!  `..    ``.    `.  :    ;  | :
              ,'  ,-'    .;   `; !!   _,'-' ,--._    ====\__/===: `.
            .'  ,-'   ,--.  ~~`-. !!  ~    ,'    `     `./  \   |  |
           .'  :;   ,'    \        !: .   ;--.__   `;.  |. ~.|   : ;
          .'  ,;    ' ,-'~~`-.     ,!  ;-'     #;   `;. \____/  : `.
         .'  ,;      /__      `-._,'!!( _(0'~~`-'    `;.  `.     ; ;
        .'  ,;    ,'    `---._(0))  !! ~   _,-,        `;  `.   ;  :
        ;  ,;    ,' ;;-.__,-._~~~   !!__,--::::|.      `;:  :   `; )
        ;  :|   ,'  ;/;;; :::;;;;----'|:: |::;\/#.      `;  |    ) ;
        :  |:  ,'  ,' :/  :;; \/))):;;::/  ::' ##:      ;;  ;    ; |
        |  :|  :;  :      `'    \/ \/ `'   `'  ##;      ;  .'  ,'  ;
        :  |;  || .'        ;\.   ____ __,--._ ##;     ;' .'--'   ;
    _,--`. `.  :: `./;   /\/;:;,-'    `-.     `--.__     .'~   ,'~
   /     ;. `; ``. :::;\;.-'~~`./~~\/\ ..    _  :::  --. ' ,-'~
  /    .  `. `; `   ~~~ ;~      ~~~~~~`--.__~~`-. :::   ) ~
 /'    ;`--`. `. `.    :;      `;       ;   `---`._    ,'
 `.  \/      `-.` `_,_ `:,-'-. `.      :_,_    ;   `--'
  `.  `.        ` (___)-: ( ) :--,-'- -(___),'~~~`.
   {_  `.               `.___.' ( ; ;)      :((:)):
     `.  `                       `--'       `.___.'
       `. `.                 ;;:::;
        `-  `.              ;;;. .;
          `-. `.__        \\;;; - ;; //
             `. ` `--..___ \\,--v-, //      Killer  Jack !!!
               `--._   ~~~~~`)____(//
                    )    ~~   ~~~~~~;
                    `.    ~~  ------;
                     `.~~_   ______,' targon
                      `. `.--';: |:
                       ;  `. Cc; Cc
                       `.  ;  __
                        `. `-'  ~\
                         `-.__,--'~""")
        print("You decided to swing across. You start grabbing the ropes tightly as you swing like Tarzan. You can see the treasure, you are half way through. Then as you grab the next rope it snaps and breaks. You are falling into a pit with creatures and as you land your body goes flat. Now you are dinner.\n\nGAME OVER")
              
      elif part4 == "3":
        print("""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
""")        
        print("You decided to confront the creatures. You charge with nothing but your fists. As you punch your way through, one creature after another they pounce at you with ferocious fury. You feel as if your winning, you push through with pure adrenaline. You defeat one after another until you finally reach the other side. You take a moment of rest now that the fight was over, or so you thought. A creature like none other, squid head, 4 arms, 2 like massive blades and it is 10 times your size. You are already exhausted because of the fight with the creatures. Your instinct is telling you to run but before you do, you get grabbed by his tentacles and you are slammed against the floor multiple times. Then he opens his gaping mouth that looks like a grinder of sorts and he slowly starts eating away at you. As you fall into a deep sleep, all you can feel is your body getting grinded to mush.\n\nGAME OVER")
      else:
        print("""
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`     ZEUS
  ________________________________________""")
        print("You fell in a hole and died :)\n\nGAME OVER")
        
    else:
      print("""
 ---.----.__..----.----| _|_||___||___||___||___||___||___||_|_ |
    |        |    |    | -.-..---..---..---..---..---..---..-.- |--.-
 ---'--.-----'----'--.-|  | ||   ||   ||   ||   ||   ||   || |  | `|
       |:           (| |  | ||   ||   ||   ||   ||   ||   || |  |--'-
       |:.           | | _|_||___||___||___||___||___||___||_|_ |
 ------'----.-.,----.'-| -.-..---..---..---..---..---..---..-.- |-.--
        ,/) |       |  |  | ||   ||   ||   ||   ||   ||   || |  | |`
 ----.---8--'--.----'--|  | ||   ||   ||   ||   ||   ||   || |  | |
     |   8     |:      | _|_||___||___||___||___||___||___||_|_ |-'--
     | ,)//    |:.     | -.-..---..---..---..---..---..---..-.- |:.
 ----'-`=;'--.-'-.----.|  | ||   ||   ||   ||   ||   ||   || |  |--.-
       //   /_ _( \    |  | ||   ||   ||   ||   ||   ||   || |  | /|
 ---.-//----)/\,'_/----| _|_||___||___||___||___||___||___||_|_ | `|
    |/|     `;=.(      | -.-..---..---..---..---..---..---..-.- |--'-
 (  |`.`.   |`,-/      |,-'-||---||---||---||---||---||---||-'-.|
 -`-'-.`.`-.';'=`.-..--'-.--------.-------------.--.-------.----'--.-
      |  `-./.}{-'\.)    |        )             |   `)     |       \
      |    :`-}{-''||    |:.      |   ,_        |          |:.     |
 ---'`'-.--|`-}{-'||)----'-.------'--'.,`--.----'--------.-'-------'-
        |  :`-`'-'/)|      |               |:.           |
 -.-----'--;`.}{,`.||----,-'--------.------'---.--------,'--.,-------
  |:     ,'/.`..'_(/(    |:         |          |             \
  |:.  ,',' |`--`.('))   |:.        |          |             |:
 -'--,' <.._|__,. >`,----'----------'--------.,'-------------'----SSt
     ``----....(','
            _,'>'
            )/
            `'""")
      print("You decided to press the blue button. The other button sinked into the wall and you start hearing a strange sound. As you breath it gets harder and harder to do so, like if the air was getting pushed out of the room. Your hand starts burning up as your body starts to decompose. You scream in agony until you can't scream any more.\n\nGAME OVER")
      


  else:
    print("""                          _____-------_____
                  ___-----      00000      -----___
               ---           00000 00000           ---
            ---            000000   000000            ---
        _---              000000     000000              ---_
        -___              000000     000000              ___-
            ---            000000   000000            ---
               ---           00000 00000           ---
                  ---_____      00000      _____---
                          -----_______-----          
""")
    print("You decided to go left and it led to a dark path. As you step on to the next stone slab, the slab sinks and your leg falls through and gets chopped off by some unseen force. You decide to crawl your way with one leg and then something comes out of the stone slab and drags you into the stone slab, turning you into red pile of pulp.\n\nGAME OVER")
    
elif part1 == "2":
  print(""".. ........... .............  ........... . ..... ........ .......
 ......  ....................%.... .... ..... .........%............
 .@@@ ........ @@.... @@@@  . ............................  *  .....
 ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
 .....\@\....@ .... @ ............................. #  .. *****  ...
  @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  *******
 ....@-@..@ ..@......@@@\...... %...... ....... <## ####>********
   @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********
 ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
 ...... .@-@@@@ ...V......     .... %.......... {#######}******* ***
 ...... .  @@ .. ..v.. .. . { } ............<###############>*******
 ......... @@ .... ........ {^^,     .......   {## ######}***** ****
 ..%..... @@ .. .%.... . .. (   `-;   ... <###################> ****
 . .... . @@ . .... .. _  .. `;;~~ ......... {#############}********
 .... ... @@ ... ..   /(______); .. ....<################  #####>***
 . .... ..@@@ ...... (         (  .........{##################}*****
 ......... @@@  ....  |:------( )  .. <##########################>**
  @@@@ ....@@@  ... _// ...... \\ ...... {###   ##############}*****
 @@@@@@@  @@@@@ .. / /@@@@@@@@@ vv  <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
  print("You decide to hide yourself in the bushes. The noises were coming from some long nailed creature you can bearly see. Next thing you see is pure darkness as your head comes clean off.\n\nGAME OVER")

elif part1 == "3":
  print("""                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
   -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
    -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```
""")
  print("You decide to charge at the noise only to find yourself vomiting blood from a stab wound made by the creature.\n\nGAME OVER")
  
else:
  print("GAME OVER!")


















