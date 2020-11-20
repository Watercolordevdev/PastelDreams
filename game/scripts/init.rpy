init python:
    config.overlay_screens.append("keymap_screen")
    if not persistent.set_volumes:
        persistent.set_volumes = True
        try:
            _preferences.volumes['music'] *= .50
        except KeyError:
            _preferences.volumes['music'] = .50        
    
init:
#this changes skip to mousewheel
    $ config.keymap['rollforward'].remove('mousedown_5')
    $ config.keymap['rollback'].remove('mousedown_4')
    $ config.keymap['dismiss'].append('mousedown_5')
    $ config.keymap['rollforward'].append('K_q')
    $ config.keymap['rollback'].append('K_w')
define config.game_menu_music = "../audio/music/gamemenu.ogg"
screen keymap_screen():
    key "K_y" action ShowMenu('history')
define gui.name_text_outlines = [ (0, "#000000", 2, 2) ]
# Declare characters used by this game. The color argument colorizes the name of the character.
define t = Character("Twilight Sparkle", color="#800080")
define a = Character(_("[povname]"), color="#228B22", who_outlines=[ (2, "#ffffff") ])
define z = Character(_("Zecora"), color="#696969", who_outlines=[ (2, "#ffffff") ])
define l = Character(_("Lyra"), color="#98ff98", who_outlines=[ (2, "#ffffff") ])
define s = Character(_("Spike"), color="#DA70D6", who_outlines=[ (2, "#ffffff") ])
define c = Character(_("Celestia"), color="#808080", who_outlines=[ (2, "#ffffff") ])
define r = Character(_("Rarity"), color="#808080", who_outlines=[ (2, "#ffffff") ])
define prd = Character(_("Pinkie and Rainbow Dash"), color="#bdcda8", who_outlines=[ (2, "#ffffff") ])
define p = Character(_("Pinkie"), color="#FF69B4", who_outlines=[ (2, "#ffffff") ])
define rd = Character(_("Rainbow Dash"), color="#48D1CC", who_outlines=[ (2, "#ffffff") ])
define f = Character(_("Fluttershy"), color="#FFFF66", who_outlines=[ (2, "#ffffff") ])
define aj = Character(_("Applejack"), color="#FFA500", who_outlines=[ (2, "#ffffff") ])


default povname = "Anonymous"

image chapter = ParameterizedText(xalign=0.5, yalign=0.3)

# The game starts here.

#default a = 2
#label start:
#  $ a = 3
#  if a == 2:
#    e "Do a thing"
#  else:
#    e "Do another thing"

#Zecora images

image zecora = "characters/zecora/zecora.png"
image zecora standing = "characters/zecora/zecora_stand.png"
image zecora back = "characters/zecora/zecora_back.png"
image zecora front = "characters/zecora/zecora_front.png"
image zecora sit = "characters/zecora/zecora_sit.png"

image zecora standing2 = im.MatrixColor(
    "characters/zecora/zecora_stand.png", 
    im.matrix.tint(.44,.65,.75)
    *im.matrix.brightness(-0.07))
    
image zecora sit2 = im.MatrixColor(
    "characters/zecora/zecora_sit.png", 
    im.matrix.tint(.44,.65,.75)
    *im.matrix.brightness(-0.07))
    
image zecora2 = im.MatrixColor(
    "characters/zecora/zecora.png", 
    im.matrix.tint(.44,.65,.75)
    *im.matrix.brightness(-0.07))
    
screen party():
  imagebutton:
    focus_mask "pinkiebutton_idle_img.png"
    idle "pinkiebutton_idle_img.png"
    hover "pinkiebutton_hover_img.png"
    pos (583,27)
    action Jump("pinkieparty")
  imagebutton:
    focus_mask "dashbutton_idle_img.png"
    idle "dashbutton_idle_img.png"
    hover "dashbutton_hover_img.png"
    pos (0,70)
    action Jump("applejackparty")
  imagebutton:
    focus_mask "raritybutton_idle_img.png"
    idle "raritybutton_idle_img.png"
    hover "raritybutton_hover_img.png"
    pos (927,369)
    action Jump("rarityparty")
  imagebutton:
    focus_mask "twilightbutton_idle_img.png"
    idle "twilightbutton_idle_img.png"
    hover "twilightbutton_hover_img.png"
    pos (1267,360)
    action Jump("twilightparty")
  imagebutton:
    focus_mask "fluttershybutton_idle_img.png"
    idle "fluttershybutton_idle_img.png"
    hover "fluttershybutton_hover_img.png"
    pos (661,406)
    action Jump("fluttershyparty")
  imagebutton:
    focus_mask "ajbutton_idle_img.png"
    idle "ajbutton_idle_img.png"
    hover "ajbutton_hover_img.png"
    pos (160,405)
    action Jump("applejackparty")
  imagebutton:
    focus_mask "spikebutton_idle_img.png"
    idle "spikebutton_idle_img.png"
    hover "spikebutton_hover_img.png"
    pos (0,538)
    action Jump("spikeparty")
    